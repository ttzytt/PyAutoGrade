from abc import ABC, abstractmethod
import enum
import dataclasses
from rich.progress import Progress
import yaml
import prctl
from multiprocessing import Process, Pipe
import os
from timeout_decorator import timeout, timeout_decorator
import importlib.util
import time
import psutil
from typing import Generic, TypeAlias, TypeVar, Callable
import sys
import traceback

class TestCase(ABC): 
    # abstract class for all kinds of testers 
    # e.g. pre-written test cases, solution code + data generator, etc.

    class TestResultType(enum.Enum):
        pass_ = 0 # because of the keyword pass
        wrong_answer = 1
        time_limit_exceeded = 2
        memory_limit_exceeded = 3
        syntax_error = 4
        runtime_error = 5
        system_error = 6
        solution_not_found = 7

    @dataclasses.dataclass
    class TestResult:
        result_type : 'TestCase.TestResultType'
        time_used   : float = -1          # in miliseconds
        memory_used : float = -1          # in MB
        expected    : any   = None     # only useful when result_type is wrong_answer
        actual      : any   = None     # only useful when result_type is wrong_answer
        err_message : str   = None     # error message
        stack_trace : str   = None     # stack trace
        test_case_id: int   = -1
        
    @dataclasses.dataclass
    class TestLimits:
        time_limit : float    = 3000
        memory_limit : float  = 512
    
    def __init__(self, test_case, tested_func_name: str, case_name : str = "", test_limits : TestLimits = TestLimits()):
        self.tested_func_name = tested_func_name
        self.case_name = case_name
        self.test_case = test_case
        self.test_results : list[TestCase.TestResult] = []
        self.test_limits = test_limits
    @abstractmethod
    def run_test(self, evaluated_module_path : str) -> TestResult:
        pass
    

class PrewrittenScriptCase(TestCase):
    
    @dataclasses.dataclass
    class EvaluatorResult: 
        is_correct : bool
        expected   : any = None
        actual     : any = None 
        msg        : str = None

    EvaluatorT  = Callable[[Callable], EvaluatorResult]
    def __init__(self, evaluator : EvaluatorT, tested_func_name : str, case_name: str = "", test_limits: TestCase.TestLimits = TestCase.TestLimits()):
        assert callable(evaluator)
        super().__init__(evaluator, tested_func_name, case_name, test_limits)
    def run_test(self, evaluated_module_path: str) -> TestCase.TestResult:
        # start a new process 
        # this is to prevent dangerous behavior from the tested code
        # use chroot and seccomp to do this
        
        # check if /tmp/autograde exists
        # if not present, make folder called /tmp/autograde
        # and chmod it to no permission
        # then chroot to that folder
        if not os.path.exists('/tmp/autograde'):
            os.mkdir('/tmp/autograde')
            os.chmod('/tmp/autograde', 0o000) # no permission to read, write or execute
        
        
        module_specs = importlib.util.spec_from_file_location('module', evaluated_module_path)
        module = importlib.util.module_from_spec(module_specs)
        module_specs.loader.exec_module(module)
        @timeout(self.test_limits.time_limit / 1000)
        def get_test_ret(): 
            evaluated_func = getattr(module, self.tested_func_name)
            return self.test_case(evaluated_func)
        
        def proc_task(children_pipe : Pipe, get_test_ret : type(get_test_ret)): 
            # this is to prevent the tested code from writing anythings to the disk
            try : 
                os.chroot('/tmp/autograde') # limit read and write after loading
                free_nonroot_uid = 65534                    
                os.setuid(free_nonroot_uid)
                st_time = time.time()
                evaluator_ret = get_test_ret()
                ed_time = time.time()
                ret = TestCase.TestResult(self.TestResultType.pass_, (ed_time - st_time) * 1000)
                if not evaluator_ret.is_correct: 
                    ret.result_type = TestCase.TestResultType.wrong_answer
                    ret.expected = evaluator_ret.expected
                    ret.actual = evaluator_ret.actual
                    ret.err_message = evaluator_ret.msg
                children_pipe.send(ret)
                children_pipe.close()
                exit()
            except Exception as e:
                stack_trace_str = traceback.format_exc()
                if isinstance(e, timeout_decorator.TimeoutError):
                    children_pipe.send(TestCase.TestResult(TestCase.TestResultType.time_limit_exceeded, err_message=str(e), stack_trace=stack_trace_str))
                if isinstance(e, SyntaxError):
                    children_pipe.send(TestCase.TestResult(TestCase.TestResultType.syntax_error, err_message=str(e), stack_trace=stack_trace_str))
                children_pipe.send(TestCase.TestResult(TestCase.TestResultType.runtime_error, err_message=str(e), stack_trace=stack_trace_str))
                children_pipe.close()
                exit()
        
        children_pip, parent_pip = Pipe()
        st_time = time.time()
        prog = Process(target=proc_task, args=(children_pip, get_test_ret))
        prog.start()
        max_mem_usage = 0
        while True: 
            # checking the memory usage
            try:
                prog_info = psutil.Process(prog.pid)
                mem_usage = prog_info.memory_info().rss / 1024 / 1024
                max_mem_usage = max(max_mem_usage, mem_usage)
                if mem_usage > self.test_limits.memory_limit:
                    ed_time = time.time()
                    time_usage = (ed_time - st_time) * 1000
                    prog.terminate()
                    return TestCase.TestResult(TestCase.TestResultType.memory_limit_exceeded, time_usage, mem_usage)
                if not prog.is_alive():
                    break
            except psutil.NoSuchProcess:
                break 
            
        prog.join()
        ret = parent_pip.recv()
        assert isinstance(ret, TestCase.TestResult)
        ret.memory_used = max_mem_usage
        parent_pip.close()
        return ret
class PrewrittenFileCase(PrewrittenScriptCase):
    # tester that runs pre-written test cases
    # the test case could be either two files (input and output) 
    # or a function that accept the tested function and return if the output is correct
    
    def _load_test_case(self): 
        assert self.testcase_path.endswith('.yml')
        with open(self.testcase_path, 'r') as f:
            file_case = yaml.load(f, Loader=yaml.FullLoader)
            for arg_str in file_case['args']:
                if isinstance(arg_str, str):
                    self.test_args.append(eval(arg_str))
                else:
                    self.test_args.append(arg_str)
            self.test_expected = file_case['expected']
            if isinstance(self.test_expected, str):
                self.test_expected = eval(self.test_expected)
    
    def __init__(self, testcase_path : str, tested_func_name, case_name: str = "", test_limits: TestCase.TestLimits = TestCase.TestLimits()):
        # test_case is the path to the yml file
        self.testcase_path = testcase_path
        self.test_args = []
        self.test_expected = None
        def file_syle_case_handler(func : callable) -> PrewrittenScriptCase.EvaluatorT: 
            # make sure that this str is indicating the path to a yml file
                output = func(*self.test_args)
                is_correct =(output == self.test_expected)
                if is_correct:
                    return PrewrittenScriptCase.EvaluatorResult(is_correct)
                else:
                    return PrewrittenFileCase.EvaluatorResult(is_correct, self.test_expected, output) 

        super().__init__(file_syle_case_handler, tested_func_name, case_name, test_limits)
        