



def count_spaces_before_text(text):
    if len(text.strip()) == 0:
        return 0
    index = 0
    while text[index] == ' ':
        index += 1
    return index






def is_line_empty(line):
    return line.strip() == ''







def does_string_start_with(string, start):
    if len(start) == 0:
        return True
    if len(start) > len(string):
        return False
    return string[:len(start)] == start







def does_string_end_with(string, end):
    if len(end) == 0:
        return True
    if len(end) > len(string):
        return False
    return string[-len(end):] == end






def is_full_line_comment(line):
    return does_string_start_with(line.strip(), '#')







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
    list_of_lines = in_file_lines.copy()
    index = 0
    for i, line in enumerate(in_file_lines):
        if 'def ' == line.strip()[:4]:
            
            if i == 0 or not (is_full_line_comment(in_file_lines[i-1]) or
                        does_string_end_with(in_file_lines[i-1], "'''") or
                        does_string_end_with(in_file_lines[i-1], '"""')):
                list_of_lines.insert(index, count_spaces_before_text(line) * ' ' +
                                '#R(auto): Add a comment that says what this function does!')
                index += 1
        index += 1
    writing_lines = []
    for line in list_of_lines:
        writing_lines.append(line + '\n')
    out_file.writelines(writing_lines)

def blank_lines_around_functions(in_file, out_file, spaces_per_tab = 4):

    def delete_elements_geq_than(num_list, num):
        if len(num_list) == 0:
            return False
        i = 1
        while i < len(num_list) and num_list[-i] >= num:
            num_list.pop()
            i += 1
        return True
            
    in_file_lines = in_file.read().splitlines()
    list_of_lines = []
    index = 0
    tabs = 0
    function_indents = [] 
    for i, line in enumerate(in_file_lines):
        list_of_lines.append(line)
        
        line_tabs = count_spaces_before_text(line) / spaces_per_tab
        previous_line = in_file_lines[i-1]
        
        if line_tabs != tabs: 
            if does_string_end_with(previous_line.strip(), ':'):
                tabs = line_tabs
            
            
            elif not is_line_empty(line) and line_tabs <= function_indents[-1]:
                if not is_line_empty(list_of_lines[index-1]):
                    list_of_lines.insert(-1,'')
                index += 1
                delete_elements_geq_than(function_indents, line_tabs)
        
        
        if 'def ' == line.strip()[:4]: 
            
            
            
            target_line = previous_line
            in_multiline_comment = (does_string_end_with(target_line.strip(), "'''") or 
                                    does_string_end_with(target_line.strip(), '"""'))
            j = 1
            
            did_multiline_comment_end = False
            while (in_multiline_comment is True or
                   is_full_line_comment(in_file_lines[i-j]) and
                   i > j): 
                print(in_file_lines[i-j])
                j += 1 
                target_line = in_file_lines[i-j]
                if in_multiline_comment: 
                    in_multiline_comment = not ("'''" in target_line or '"""' in target_line) 
                    if (does_string_start_with(target_line.strip(), "'''") or 
                        does_string_start_with(target_line.strip(), '"""')):
                        j += 1
                        did_multiline_comment_end = True
                else:
                    in_multiline_comment = (does_string_end_with(target_line.strip(), "'''") or 
                                            does_string_end_with(target_line.strip(), '"""'))
            j += 1
            print("J", j, in_file_lines[i-j], "which is before", in_file_lines[i-j+1])
            
            if ((i == 0 or
                 not is_line_empty(list_of_lines[-j]))):
                print("IF THIS SAYS TRUE IM LYING", list_of_lines[-j])
                print(list_of_lines[-j], is_line_empty(list_of_lines[-j]))
                list_of_lines.insert(-j+1,'')
                index += 1
            function_indents.append(tabs)
            tabs += 1
        elif 'class ' == line.strip()[:6]:
            tabs += 1

    writing_lines = []
    for line in list_of_lines:
        writing_lines.append(line + '\n')
    out_file.writelines(writing_lines)
            
def break_up_long_lines(in_file, out_file):
    in_file_lines = in_file.read().splitlines()
    list_of_lines = in_file_lines.copy()
    index = 0
    for line in in_file_lines:
        if len(line) > 79:
            list_of_lines.insert(index,count_spaces_before_text(line) * ' ' +
                                 '#R(auto): Line of code is too long. Break it up!')
        index += 1
    writing_lines = []
    for line in list_of_lines:
        writing_lines.append(line + '\n')
    out_file.writelines(writing_lines)

def spaces_after_commas(in_file, out_file):
    in_file_text = in_file.read()
    edited_text = ''
    i = 0
    while i < len(in_file_text) - 1:
        edited_text += in_file_text[i]
        if in_file_text[i] == ',' and not in_file_text[i + 1] == ' ':
            edited_text += ' '
        i += 1
    out_file.write(edited_text)
        
def one_letter_variables(in_file, out_file):
    in_file_lines = in_file.read().splitlines()
    list_of_lines = in_file_lines.copy()
    index = 0
    variables = []
    for line in in_file_lines:
        pass

def main():
    with (open('t16_test.py', 'r') as in_file, open('peepee.py', 'w') as out_file):
        comments_for_functions(in_file, out_file)

    with (open('t16_test.py', 'r') as in_file, open('t16_test_REQUIEM.py', 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)

    with (open('asudysrtu.py', 'r') as in_file, open('OHLORD.py', 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)

if __name__ ==  '__main__':
    main()


                
                
