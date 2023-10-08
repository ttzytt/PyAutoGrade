import yaml
from tqdm import tqdm 
import os
from pathlib import Path
import importlib.util
from test_case import *
import itertools

class BatchTestManger:
    @dataclasses.dataclass
    class TestSummary: 
        correct_output  : int 
        pass_percent    : float 
        total_test      : int
        wrong_case_details : list[TestCase.TestResult] = None
        def __init__(self, tests : list[TestCase.TestResult]):
            self.total_test = len(tests)
            self.correct_output = 0
            self.wrong_case_details = []
            for t in tests:
                if t.result_type == TestCase.TestResultType.pass_:
                    self.correct_output += 1
                else:
                    self.wrong_case_details.append(t)
            self.pass_percent = self.correct_output / self.total_test * 100
    
    def __init__(self, cfg : str = './config.yml'):
        self.cfg = yaml.load(open(cfg, "r"), Loader=yaml.FullLoader)
        self.cfg_abspath = os.path.abspath(cfg)
        self.cfg_folder  = os.path.join(*Path(self.cfg_abspath).parts[:-1])
        self.tested_code_abs_path = os.path.join(self.cfg_folder, self.cfg['tested_code_path']) if not os.path.isabs(self.cfg['tested_code_path'])\
                                    else self.cfg['tested_code_path']
        self.test_case_abs_path = os.path.join(self.cfg_folder, self.cfg['test_case_path']) if not os.path.isabs(self.cfg['test_case_path'])\
                                    else self.cfg['test_case_path']
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
        pass
    
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
            if not os.path.exists(abs_prob_testcase_path): 
                raise FileNotFoundError(f"Test case at {abs_prob_testcase_path} not found")
            if not os.path.exists(abs_prob_solution_path):
                raise FileNotFoundError(f"Solution at {abs_prob_solution_path} not found")
          
            
            evaluator_module_specs = importlib.util.spec_from_file_location('module', abs_prob_testcase_path)
            evaluator_module = importlib.util.module_from_spec(evaluator_module_specs)
            evaluator_module_specs.loader.exec_module(evaluator_module)
            
            test_cases = getattr(evaluator_module, "test_case_constructor")()
            cases_resuls = []
            for t in tqdm(test_cases):
                assert isinstance(t, TestCase), "test case constructor should return a list of TestCase, instead, it is {}".format(type(t))
                if isinstance(t, PrewrittenFileCase):
                    t.testcase_path = os.path.join(self.test_case_abs_path, t.testcase_path)
                cases_resuls.append(t.run_test(abs_prob_solution_path))
            if prob not in ret: 
                ret[prob] = [0] * len(unique_stu)
            ret[prob][ret['students'].index(stu)] = self.TestSummary(cases_resuls)
        return ret