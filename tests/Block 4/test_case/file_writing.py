from test_case import *
import sys 
sys.path.append('./../../src/')
from test_case import  PrewrittenFileCase as pf, PrewrittenScriptCase as ps
import random
import io
import string
from scanf import scanf
def gen_random_file(
                    file_len : int,
                    use_punctuation : bool = True, 
                    use_digits : bool = True, 
                    use_whitespace : bool = True, 
                    ) -> io.StringIO: 
    rand_str = ""
    charset = string.ascii_letters
    if use_punctuation: charset += string.punctuation
    if use_digits: charset += string.digits
    if use_whitespace: charset += string.whitespace
    for _ in range(file_len):
        rand_str += random.choice(charset)
    ret = io.StringIO(rand_str)
    ret.seek(0)
    return ret

def cmp_file(f1 : io.StringIO, f2 : io.StringIO): 
    # if f1.getvalue() != f2.getvalue():  
        # print("f1: \n", "'" +  f1.getvalue() + "'")
        # print("f2: \n", "'" + f2.getvalue() + "'")
    return f1.getvalue() == f2.getvalue()

def T11_evaluator(target_file : io.StringIO, *input_args, **input_kwds):
    def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
        empty_file = io.StringIO()
        func(empty_file, *input_args, **input_kwds)
        empty_file.seek(0)
        correct = True
        for line1, line2 in zip(empty_file, target_file):
            # crop trailing newline character and empty spaces 
            # however keep leading spaces
            line1 = line1.rstrip()
            line2 = line2.rstrip()
            if line1 != line2:
                # print("line1: ", line1)
                # num_whitespace = len(line1) - len(line1.lstrip())
                # print("num_whitespace: ", num_whitespace)
                # print("line2: ", line2)
                # num_whitespace = len(line2) - len(line2.lstrip())
                # print("num_whitespace: ", num_whitespace)
                correct = False
                break
        if correct:
            return PrewrittenScriptCase.EvaluatorResult(True)
        else: 
            return PrewrittenScriptCase.EvaluatorResult(False, "correct file content is " + target_file.getvalue() +  " while the program have given "+  empty_file.getvalue())
    return evaluator

def T13_evaluator(input_file, *input_args, **input_kwds):
    def evaluator(func: Callable) -> PrewrittenScriptCase.EvaluatorResult:
        empty_file = io.StringIO()
        func(input_file, empty_file, *input_args, **input_kwds)
        empty_file.seek(0)
        correct = True
        for line in empty_file:
            # crop trailing newline character and empty spaces 
            # however keep leading spaces
            scan_ret = scanf("%d + %d = %d", line)
            if scan_ret == None:
                correct = False
                break
            op1, op2, res = scan_ret
            orig_op1, orig_op2 = scanf("%d + %d = ", line)
            if op1 + op2 != res or op1 != orig_op1 or op2 != orig_op2:
                correct = False
                break
            
        if correct:
            return PrewrittenScriptCase.EvaluatorResult(True)
        else: 
            return PrewrittenScriptCase.EvaluatorResult(False, "the output file have wrong format")
    return evaluator


def T12_14_evaluator(input_file : io.StringIO, target_file : io.StringIO, *input_args, **input_kwds):
    def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
        empty_file = io.StringIO()
        func(input_file, empty_file, *input_args, **input_kwds)
        correct = cmp_file(empty_file, target_file)
        if correct:
            return PrewrittenScriptCase.EvaluatorResult(True)
        else: 
            return PrewrittenScriptCase.EvaluatorResult(False, "correct file content is " + target_file.getvalue() +  " while the program have given "+  empty_file.getvalue())
    return evaluator

# def T13_evaluator(input_file : io.StringIO, *input_args, **input_kwds):
#     def evaluator(func : Callable) -> PrewrittenScriptCase.EvaluatorResult:
#         empty_file = io.StringIO()
#         func(input_file, empty_file, *input_args, **input_kwds)


#         if correct:
#             return PrewrittenScriptCase.EvaluatorResult(True)
#         else: 
#             return PrewrittenScriptCase.EvaluatorResult(False, "correct file content is " + target_file.getvalue() +  " while the program have given "+  empty_file.getvalue())
#     return evaluator

def write_diamond_pattern_sol(out_file : io.StringIO, width):
    """ 
    width = 3:
     x
    xxx
     x
    """
    cur_len = 1
    while cur_len <= width: 
        empty_spaces = (width - cur_len) // 2
        out_file.write(" " * empty_spaces)
        out_file.write("x" * cur_len)
        # change line 
        out_file.write("\n")
        cur_len += 2
    cur_len -= 4
    while cur_len > 0:
        empty_spaces = (width - cur_len) // 2
        out_file.write(" " * empty_spaces)
        out_file.write("x" * cur_len)
        # change line 
        out_file.write("\n")
        cur_len -= 2
    out_file.seek(0)

def last_name_first_sol(in_file, out_file):
    for line in in_file:
        # Remove any leading/trailing whitespace and split the line into first and last names
        first_name, last_name = line.strip().split()
        
        # Write the last name followed by a comma, then the first name to the output file
        out_file.write(f"{last_name}, {first_name}\n")
    in_file.seek(0); out_file.seek(0)

def generate_t12_input_file(num_lines, max_single_line_len):
    test_cases = io.StringIO()
    
    for _ in range(num_lines):
        first_name_length = random.randint(1, max_single_line_len)
        last_name_length = random.randint(1, max_single_line_len)
        
        first_name = ''.join(random.choice(string.ascii_letters) for _ in range(first_name_length))
        last_name = ''.join(random.choice(string.ascii_letters) for _ in range(last_name_length))
        
        test_cases.write(f"{first_name} {last_name}\n")
    
    test_cases.seek(0)  # Reset the internal pointer to the beginning of the buffer
    
    return test_cases

def add_and_write_sol(in_file, out_file):
   
    for line in in_file:
        # Remove any leading/trailing whitespace and split the line into operands
        operand1, operand2 = line.strip().split('+')
        
        # Convert operands to integers and calculate the result
        result = int(operand1) + int(operand2)
        
        # Write the original problem followed by = and the result to the output file
        out_file.write(f"{operand1} + {operand2} = {result}\n")
    out_file.seek(0)
    in_file.seek(0)

def generate_t13_cases(num_lines, max_operand_value = int(1e5)):
    test_cases = io.StringIO()
    
    for _ in range(num_lines):
        operand1 = random.randint(0, max_operand_value)
        operand2 = random.randint(0, max_operand_value)
        
        test_cases.write(f"{operand1} + {operand2}\n")
    
    test_cases.seek(0)  # Reset the internal pointer to the beginning of the buffer
    
    return test_cases

def blah_blah_blah_sol(in_file, out_file_name):
    for line in in_file:
        # Remove any leading/trailing whitespace
        # line = line.strip()
        
        # Check if the line length is greater than 20 characters
        if len(line) > 20:
            # Truncate the line to the first 15 characters and append ', blah blah blah'
            line = line[:15] + ', blah blah blah'
        
        # Write the modified or original line to the output file
        out_file_name.write(f"{line}\n")
    in_file.seek(0); out_file_name.seek(0)


def generate_t14_cases(num_lines, max_length):
    test_cases = io.StringIO()
    
    for _ in range(num_lines):
        line_length = random.randint(1, max_length)
        line = ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(line_length))
        
        test_cases.write(f"{line}\n")
    
    test_cases.seek(0)  # Reset the internal pointer to the beginning of the buffer
    
    return test_cases

def test_case_constructor() -> list[TestCase]:

    test_cases : list[TestCase] = []
    peb = ps.EvaluatorBuilder()
    TESTED_FUNC_NAME = "write_diamond_pattern"
    _ps = lambda evaluator, msg = "": ps(evaluator, TESTED_FUNC_NAME, msg)
    # T11
    random.seed(0)

    # select 10 random odd integers from [1, 5001]
    random_integers = random.sample(range(1, 50, 2), 10)
    # random_integers = [5]
    print(random_integers)
    for dwidth in random_integers:
        tar_file = io.StringIO()
        write_diamond_pattern_sol(tar_file, dwidth)
        test_cases.append(_ps(T11_evaluator(tar_file, dwidth), "diamond with width: " + str(dwidth)))

    TESTED_FUNC_NAME = "last_name_first"
    for file_line_cnt in range(1, 500, 50):
        in_file = generate_t12_input_file(file_line_cnt, 100)
        tar_file = io.StringIO()
        last_name_first_sol(in_file, tar_file)
        test_cases.append(_ps(T12_14_evaluator(in_file, tar_file), "file with " + str(file_line_cnt) + " lines"))

    TESTED_FUNC_NAME = "add_and_write"
    for file_line_cnt in range(1, 500, 50):
        in_file = generate_t13_cases(file_line_cnt)
        test_cases.append(_ps(T13_evaluator(in_file), "file with " + str(file_line_cnt) + " lines"))

    # TESTED_FUNC_NAME = "blah_blah_blah"
    # for file_line_cnt in range(1, 500, 50):
    #     in_file = generate_t14_cases(file_line_cnt, 100)
    #     tar_file = io.StringIO()
    #     blah_blah_blah_sol(in_file, tar_file)
    #     test_cases.append(_ps(T12_14_evaluator(in_file, tar_file), "file with " + str(file_line_cnt) + " lines"))

    return test_cases