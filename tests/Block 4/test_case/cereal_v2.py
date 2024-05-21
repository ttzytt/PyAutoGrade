import sys 
sys.path.append('./../../src/')
from test_case import  PrewrittenFileCase as pf, PrewrittenScriptCase as ps
from test_case import *
from stdIO_simulator import *
import random
from parse import search
import numpy as np

def get_rand_str():
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10)))

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


    TOT_TEST_CNT = 10
    LINES_PER_TEST_HIGH = 20
    line_cnt_in_tests = list(np.linspace(1, LINES_PER_TEST_HIGH, TOT_TEST_CNT, dtype=int))
    for i in range(TOT_TEST_CNT):
        lines_per_test = line_cnt_in_tests[i]
        def evaluator(tested_func, stdio_simulator : StdIOSimulator) -> PrewrittenScriptCase.EvaluatorResult:
            for l in range(lines_per_test):
                add_new_fruit_cnt = random.randint(1, 5)
                # always add one new fruit and other fruits are old 
                # gen rand_str until it is not in the fruit_dict
                existing_fruit = get_rand_str()
                while existing_fruit in fruit_dict:
                    existing_fruit = get_rand_str()
                fruit_dict[existing_fruit] = 1
                stdio_simulator.write_input("floor " + existing_fruit + "\n")
                for _ in range(add_new_fruit_cnt - 1):
                    # choose a existing fruit and add one 
                    existing_fruit = random.choice(list(fruit_dict.keys()))
                    fruit_dict[existing_fruit] += 1
                    stdio_simulator.write_input("floor " + existing_fruit + "\n")

                selected_fruit_cnt = random.randint(1, len(fruit_dict))
                selected_fruits = random.sample(list(fruit_dict.keys()), selected_fruit_cnt)  # type: ignore
                ans = 0
                for f in selected_fruits:
                    ans += fruit_dict[f]
                # in case the tested code put some prompt for input
                print("selected fruits: ", selected_fruits)
                stdio_simulator.write_input(" ".join(selected_fruits) + "\n")

                while stdio_simulator.tested_code_ans_count() <= 0: pass
                ans_from_tested_code = stdio_simulator.tested_code_ans.get()
                stdio_simulator.clear_all()
                print("ans_from_tested_codef:", ans_from_tested_code)
                try: 
                    ans_num = search("{:d}", ans_from_tested_code)[0] # type: ignore
                except Exception as e:
                    stdio_simulator.write_input("quit")
                    return PrewrittenScriptCase.EvaluatorResult(False, "the answer from the tested code did not include any number")
                print("tested_ans: ", ans_num, "ans: ", ans)
                if ans_num != ans:
                    stdio_simulator.write_input("quit")
                    return PrewrittenScriptCase.EvaluatorResult(False, f"Expected {ans}, but got {ans_num}")
            stdio_simulator.write_input("quit")
            return PrewrittenScriptCase.EvaluatorResult(True)
        test_cases.append(ps(evaluator, test_limits=TestCase.TestConfig(time_limit=1000)))
    return test_cases