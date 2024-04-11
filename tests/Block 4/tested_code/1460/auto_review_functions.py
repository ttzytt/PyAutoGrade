



def count_spaces_before_text(text):
    index = 0
    while text[index] == ' ':
        index += 1
    return index

def is_line_empty(line):
    return line.strip() == ''

def is_index_in_string(line, index):
    is_string_single_quotes = False
    is_string_double_quotes = False
    for i in range(len(line)):
        if line[i] == "'":
            is_string_single_quotes = not is_string_single_quotes
        elif line[i] == '"':
            is_string_double_quotes = not is_string_double_quotes
        if i == index:
            return is_string_single_quotes or is_string_double_quotes


def comments_for_functions(in_file, out_file):
    in_file_lines = in_file.read().splitlines()
    list_of_lines = []
    for i, line in enumerate(in_file_lines):
        if 'def ' == line.strip()[:4]:
            
            if i == 0 or '#' not in in_file_lines[i-1]:
                list_of_lines.append(count_spaces_before_text(line) * ' ' +
                                '#R(auto): Add a comment that says what this function does!')
        list_of_lines.append(line)
    writing_lines = []
    for line in list_of_lines:
        writing_lines.append(line + '\n')
    out_file.writelines(writing_lines)

def blank_lines_around_functions(in_file, out_file):
    in_file_lines = in_file.read().splitlines()
    list_of_lines = []
    in_function = 0
    in_class = 0
    indent_order = []
    for i, line in enumerate(in_file_lines):
        if 'def ' == line.strip()[:4]:
            if in_function:
                print("oh lord there's nested functions i can't do this...")
            in_function += 1
            if is_line_empty(in_file_lines[i-1]):
                list_of_lines.append('')
        elif 'class ' == line.strip()[:6]:
            in_class += 1
        elif count_spaces_before_text(line) != (in_function + in_class) * 4 and not is_line_empty:
            print("AÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ")
            for i in range(count_spaces_before_text(line) / 4 - (in_function + in_class)): 
                indent_order.append('')
            in_function -= 1
            list_of_lines.append('')
            
def break_up_long_lines(in_file, out_file):
    in_file_lines = in_file.read().splitlines()
    list_of_lines = []
    for line in in_file_lines:
        if len(line) > 79:
            list_of_lines.append('')
        list_of_lines.append(line)
    writing_lines = []
    for line in list_of_lines:
        writing_lines.append(line + '\n')
    out_file.writelines(writing_lines)
            

class Eat:
    def test():
        pass

    

with (open('auto_review_functions.py', 'r') as in_file, open('peepee.py', 'w') as out_file):
    comments_for_functions(in_file, out_file)
                
                
