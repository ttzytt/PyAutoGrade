



def count_spaces_before_text(text):
    index = 0
    while text[index] == ' ':
        index += 1
    return index

' def test()'


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
        if 'def ' in line and not is_index_in_string(line, line.index('def ')) and \
        ('#' not in line or line.index('#') > line.index('def ')):
            
            if '#' not in in_file_lines[i-1]:
                list_of_lines.append(count_spaces_before_text(line) * ' ' +
                                '#R(auto): Add a comment that says what this function does!')
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
                
                
