from test_case import *
import random

def test_rand_add(func):
    rand_a = random.randint(0, 100)
    rand_b = random.randint(0, 100)
    return PrewrittenScriptCase.EvaluatorResult(
        rand_a + rand_b == func(rand_a, rand_b), 
        rand_a + rand_b, 
        func(rand_a, rand_b)
    )

    
def test_case_constructor() -> list[TestCase]:
    # return only test case or with the path to the tested code 
    # if not providing the path, will use the default path
    ret = []
    ret.append(PrewrittenFileCase("./addition.yml", "add", "addition file test"))
    ret.append(PrewrittenScriptCase(test_rand_add, "add", "addition random test"))
    return ret