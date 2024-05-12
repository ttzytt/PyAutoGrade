import sys 
sys.path.append('./../../src/')
from test_case import  PrewrittenFileCase as pf, PrewrittenScriptCase as ps
from test_case import *
from stdIO_simulator import *
import random
from parse import search
import numpy as np
def test_case_constructor() -> list[TestCase]:
    random.seed(0)
    print("constructor called")
    test_cases = []
    fruit_dict = {
        "red"    : 6, 
        "blue"   : 5,
        "yellow" : 7,
        "orange" : 7, 
        "purple" : 4, 
        "green"  : 6
    }    


    TOT_TEST_CNT = 2
    LINES_PER_TEST_HIGH = 8
    line_cnt_in_tests = list(np.linspace(1, LINES_PER_TEST_HIGH, TOT_TEST_CNT, dtype=int))
    for i in range(TOT_TEST_CNT):
        lines_per_test = line_cnt_in_tests[i]
        def evaluator(tested_func, stdio_simulator : StdIOSimulator) -> PrewrittenScriptCase.EvaluatorResult:
            for l in range(lines_per_test):
                selected_fruit_cnt = random.randint(1, len(fruit_dict))
                selected_fruits = random.sample(list(fruit_dict.keys()), selected_fruit_cnt)  # type: ignore
                ans = 0
                for f in selected_fruits:
                    ans += fruit_dict[f]
                # in case the tested code put some prompt for input
                print("selected fruits: ", selected_fruits)
                stdio_simulator.write_input(" ".join(selected_fruits) + "\n")

                try:
                    while stdio_simulator.tested_code_ans_count() <= 0: pass
                except TimeoutError: 
                    stdio_simulator.write_input("quit")
                    return PrewrittenScriptCase.EvaluatorResult(False, "TimeoutError")
                ans_from_tested_code = stdio_simulator.tested_code_ans.get()
                stdio_simulator.clear_all()
                print("ans_from_tested_codef:", ans_from_tested_code)
                try: 
                    ans_num = search("{:d}", ans_from_tested_code)[0] # type: ignore
                except Exception as e:
                    stdio_simulator.write_input("quit")
                    return PrewrittenScriptCase.EvaluatorResult(False, f"Error: {e}")
                print("tested_ans: ", ans_num, "ans: ", ans)
                if ans_num != ans:
                    stdio_simulator.write_input("quit")
                    return PrewrittenScriptCase.EvaluatorResult(False, f"Expected {ans}, but got {ans_num}")
            stdio_simulator.write_input("quit")
            return PrewrittenScriptCase.EvaluatorResult(True)
        test_cases.append(ps(evaluator))
    return test_cases