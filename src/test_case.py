from abc import ABC, abstractmethod
import enum
import dataclasses
from rich.progress import Progress
import yaml
from multiprocessing import Process, Pipe
import os
from timeout_decorator import timeout, timeout_decorator
import importlib.util
import time
import psutil
from typing import Generic, TypeAlias, TypeVar, Callable
import sys
import traceback
from typing import Any
import pdb
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
        expected    : Any   = None     # only useful when result_type is wrong_answer
        actual      : Any   = None     # only useful when result_type is wrong_answer
        err_message : str   = None     # error message
        stack_trace : str   = None     # stack trace
        test_case_id: int   = -1
        tested_func_name : str = ""
        
    @dataclasses.dataclass
    class TestLimits:
        time_limit : float    = 3000
        memory_limit : float  = 512
    
    def __init__(self, test_case, tested_func_name: str, case_name : str = "", test_limits : TestLimits = TestLimits()):
        self.tested_func_name = tested_func_name
        self.case_name = case_name 
        self.test_case : Callable[[Callable], TestCase.TestResult] = test_case
        self.test_results : list[TestCase.TestResult] = []
        self.test_limits = test_limits
    @abstractmethod
    def run_test(self, evaluated_module_path : str) -> TestResult:
        pass
    

class PrewrittenScriptCase(TestCase):
    
    @dataclasses.dataclass
    class EvaluatorResult: 
        is_correct : bool
        expected   : Any = None
        actual     : Any  = None 
        msg        : str | None = None

    class EvaluatorBuilder:
        def __init__(self, float_precision : float = 1e-5):
            self.float_precision = float_precision
            self.float_eq = lambda a, b: abs(a - b) < self.float_precision
            self.float_lt = lambda a, b: a < b - self.float_precision
            self.float_gt = lambda a, b: a > b + self.float_precision
            self.float_le = lambda a, b: a < b + self.float_precision
            self.float_ge = lambda a, b: a > b - self.float_precision

        def assert_cond_true(self, cond : Callable, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond_ret = cond(ret)
                if cond_ret:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert cond true evaluator, the return value of the tested function is " + str(ret) + " which does not satisfy the condition")
            return evaluator

        def assert_eq(self, value : Any, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond = ret == value
                if isinstance(ret, float) and isinstance(value, float):
                    cond = self.float_eq(ret, value)
                if cond:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert eq evaluator, the return value of the tested function is " + str(ret) + " of type " + str(type(ret)) + " which does not equal to " + str(value) + " of type " + str(type(value)))
            return evaluator
        
        def assert_eq_correct_sol(self, correct_sol : Callable, *input_args, **input_kwds):
            correct_val = correct_sol(*input_args, **input_kwds)
            return self.assert_eq(correct_val, *input_args, **input_kwds)

        def assert_lt(self, value : Any, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond = ret < value
                if isinstance(ret, float) and isinstance(value, float):
                    cond = self.float_lt(ret, value)
                if cond:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert lt evaluator, the return value of the tested function is " + str(ret) + str(ret) + " of type " + str(type(ret)) +  " which is not less than " + str(value) + " of type " + str(type(value)))
            return evaluator
     
        def assert_gt(self, value : Any, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond = ret > value
                if isinstance(ret, float) and isinstance(value, float):
                    cond = self.float_gt(ret, value)
                if cond:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert gt evaluator, the return value of the tested function is " + str(ret) + " of type " + str(type(ret))+ " which is not greater than " + str(value) + " of type " + str(type(value)))
            return evaluator
        
        def assert_le(self, value : Any, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond = ret <= value
                if isinstance(ret, float) and isinstance(value, float):
                    cond = self.float_le(ret, value)
                if cond:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert le evaluator, the return value of the tested function is " + str(ret) + " of type " + str(type(ret)) + " which is not less than or equal to " + str(value) + " of type " + str(type(value)))
            return evaluator
        
        def assert_ge(self, value : Any, *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                cond = ret >= value
                if isinstance(ret, float) and isinstance(value, float):
                    cond = self.float_ge(ret, value)
                if cond:
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert ge evaluator, the return value of the tested function is " + str(ret) + " of type " + str(type(ret)) +  " which is not greater than or equal to " + str(value) + " of type " + str(type(value)))
            return evaluator

        @staticmethod
        def assert_content_in_set(value : set, ret_to_set_converter : Callable[[str], set], *input_args, **input_kwds):
            def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
                ret = func(*input_args, **input_kwds)
                ret = ret_to_set_converter(ret)
                if ret.issubset(value):
                    return PrewrittenScriptCase.EvaluatorResult(True)
                else:
                    return PrewrittenScriptCase.EvaluatorResult(False, msg="in assert content in set evaluator, the return value of the tested function is " + str(ret) + " of type " + str(type(ret))+ " which is not a subset of " + str(value) + " of type " + str(type(value)))
            return evaluator
                
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
        

        loading_module_exception = None
        try: 
            module_specs = importlib.util.spec_from_file_location('module', evaluated_module_path)
            module = importlib.util.module_from_spec(module_specs)
            module_specs.loader.exec_module(module)
        except Exception as e:
            loading_module_exception = e
        @timeout(self.test_limits.time_limit / 1000)
        def get_test_ret(): 
            if loading_module_exception is not None:
                raise loading_module_exception
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
        ret.tested_func_name = self.tested_func_name
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
        self.testcase_pxath = testcase_path
        self.test_args = []
        self.test_expected = None
        def file_syle_case_handler(func : Callable) -> PrewrittenScriptCase.EvaluatorResult: 
            # make sure that this str is indicating the path to a yml file
                output = func(*self.test_args)
                is_correct =(output == self.test_expected)
                if is_correct:
                    return PrewrittenScriptCase.EvaluatorResult(is_correct)
                else:
                    return PrewrittenFileCase.EvaluatorResult(is_correct, self.test_expected, output) 

        super().__init__(file_syle_case_handler, tested_func_name, case_name, test_limits)
        