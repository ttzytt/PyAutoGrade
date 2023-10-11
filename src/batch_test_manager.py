import yaml
from tqdm import tqdm 
import os
from pathlib import Path
import importlib.util
from test_case import *
import itertools
import pandas as pd
from numbers import Number
from datetime import datetime

class BatchTestManger:
    @dataclasses.dataclass
    class TestSummary: 
        correct_output  : int 
        pass_percent    : float 
        total_test      : int
        correct_average_time : float
        correct_average_memory : float
        wrong_case_details : list[TestCase.TestResult] = None
        def __init__(self, tests : list[TestCase.TestResult]):
            self.correct_average_time = 0
            self.correct_average_memory = 0
            self.total_test = len(tests)
            self.correct_output = 0
            self.wrong_case_details = []
            for t in tests:
                if t.result_type == TestCase.TestResultType.pass_:
                    self.correct_output += 1
                    self.correct_average_time += t.time_used
                    self.correct_average_memory += t.memory_used
                else:
                    self.wrong_case_details.append(t)
            self.pass_percent = self.correct_output / self.total_test * 100
            if self.correct_output > 0:
                self.correct_average_memory /= self.correct_output
                self.correct_average_time /= self.correct_output
            else:
                self.correct_average_memory = -1
                self.correct_average_time = -1
                
    def __get_abs_path_in_cfg(self, path : str) -> str:
        # get the absolute path of `path` in the cfg file
        # if `path` is not a relative path, return `path`
        if not os.path.isabs(path):
            return os.path.join(self.cfg_folder, path)
        else:
            return path
    
    def __init__(self, cfg : str = './config.yml'):
        self.cfg = yaml.load(open(cfg, "r"), Loader=yaml.FullLoader)
        self.cfg_abspath = os.path.abspath(cfg)
        self.cfg_folder  = os.path.join(*Path(self.cfg_abspath).parts[:-1])
        self.tested_code_abs_path = self.__get_abs_path_in_cfg(self.cfg['tested_code_path'])
        self.test_case_abs_path = self.__get_abs_path_in_cfg(self.cfg['test_case_path'])
        self.last_test_result = dict[str, list]
    def test_all(self) -> dict[str, list]:
        # test all presented problems with test strategies cofigured
        stus = self.cfg['students_list']
        probs = self.cfg['problems_list']
        return self.test_specific(*itertools.product(stus, probs))
        
    def test_students(self, *students : str) -> dict[str, list]:
        # test all the code of `students`
        return self.test_specific(*itertools.product(students, self.cfg['problems_list']))
    def test_problems(self, *problems : str) -> dict[str, list] :
        return self.test_specific(*itertools.product(self.cfg['students_list'], problems))
    def test_students_with_problem(self, students : list[str], problems : list[str]) -> dict[str, list]:
        # test all `problems` that implemented by students listed in `students`
        return self.test_specific(*itertools.product(students, problems))
    
    def test_specific(self, *stu_prob_pair : tuple[str, str]) -> dict[str, list]:
        # test a specific student's specific problem
        # students are in column, problems are in row
        unique_stu = set()
        unique_prob = set()
        for stu, prob in stu_prob_pair: unique_stu.add(stu) ; unique_prob.add(prob)
        pbar = tqdm(list(stu_prob_pair))
        ret = {
            "students" : list(unique_stu),
        }
        """ 
            students | prob1    | prob 2
            stu1     | sumary 1 | summary 2
        """
        for i, (stu, prob) in enumerate(pbar):
            assert not os.path.isabs(prob), "prob path should be the relative path from the `test_case_path` or `tested_code_path` provided in the cfg file"
            pbar.set_description(f"Testing {stu}'s {prob}")
            abs_prob_testcase_path = os.path.join(self.test_case_abs_path, prob + '.py')
            abs_prob_solution_path = os.path.join(self.tested_code_abs_path, stu, prob + '.py')
            multiple_cases_results = []
            if not os.path.exists(abs_prob_testcase_path): 
                raise FileNotFoundError(f"Test case at {abs_prob_testcase_path} not found")
            if not os.path.exists(abs_prob_solution_path):
                multiple_cases_results.append(
                    TestCase.TestResult(
                    TestCase.TestResultType.solution_not_found))
            else:
                evaluator_module_specs = importlib.util.spec_from_file_location('module', abs_prob_testcase_path)
                evaluator_module = importlib.util.module_from_spec(evaluator_module_specs)
                evaluator_module_specs.loader.exec_module(evaluator_module)
                
                test_cases = getattr(evaluator_module, "test_case_constructor")()
                for i, t in enumerate(tqdm(test_cases)):
                    assert isinstance(t, TestCase), "test case constructor should return a list of TestCase, instead, it is {}".format(type(t))
                    if isinstance(t, PrewrittenFileCase):
                        t.testcase_path = os.path.join(self.test_case_abs_path, t.testcase_path)
                        t._load_test_case()
                    case_result = t.run_test(abs_prob_solution_path)
                    case_result.test_case_id = i
                    multiple_cases_results.append(case_result)
            if prob not in ret: 
                ret[prob] = [0] * len(unique_stu)
            ret[prob][ret['students'].index(stu)] = self.TestSummary(multiple_cases_results)
        self.last_test_result = ret 
        return ret

    def export_file(self, export_test_result : dict[str, list] = None, export_path : str = None) -> pd.DataFrame:
        # export testing results in the format of file 
        # if export_test_result is None, export the last test result
        # if export_path is None, export to the output path provided in the cfg config file
        if export_test_result is None: export_test_result = self.last_test_result
        if export_path is None: export_path = self.__get_abs_path_in_cfg(self.cfg['output_path'])

        tmp_dict = {"students" : export_test_result['students'][:]} 
        tmp_test_result = self.TestSummary([TestCase.TestResult(TestCase.TestResultType.pass_)])
        tested_problems = []
        for col_name, _ in export_test_result.items():
            if col_name == 'students': continue
            tested_problems.append(col_name)
        
        for prob in tested_problems:
            for t_summary_entries, _ in vars(tmp_test_result).items():
                col_name = f"{prob}_{t_summary_entries}"
                tmp_dict[col_name] = []
                for stu_idx, stu in enumerate(export_test_result['students']):
                    entry_val = getattr(export_test_result[prob][stu_idx], t_summary_entries)
                    entry_val = entry_val if isinstance(entry_val, Number) else str(entry_val)
                    tmp_dict[col_name].append(entry_val)
        
        file_name = "test result@" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        df = pd.DataFrame(tmp_dict)
        # save to csv file
        df.to_csv(os.path.join(export_path, file_name), index=False)
    
        return df 