




'''
T15
Detects if there a function definition in a file without a comment starting with #
on the line before it. The function will then add a line of code that says
'
    inputs:
        in_file a file that is open for reading
    outputs:
        out_file a file that will be the result
'''

def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    new_lines = []
    comment_needed = False
    comment_above = False
    for line in range(len(list_of_lines)):
        j = 0  # Counter to go through lines
        if 'def '  == list_of_lines[line][:4]:
            comment_needed = True
            if list_of_lines[0] == '\n':
                comment_needed = True
            else:
                while j < line:
                    if '
                        comment_above = True
                        comment_needed = False
                        j += 1
                    elif comment_above == False:
                        comment_needed = True
    if comment_needed == True:
        new_lines.append('#R(auto): Add a comment that says what this function does!')
    out_file.writelines(new_lines)
    out_file.writelines('\n')
    out_file.writelines(list_of_lines)

'''
T16
Adds a blank line where there should be one. Such as before each function, after each function
before the comment, etc.
    inputs:
        in_file a file that is open for reading
    outputs:
        out_file a file that will be the result
'''

def add_blank_lines_around_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    output_lines = []
    inside_function = False
    for line in list_of_lines:
        if 'def' in line:
            inside_function = True
            if inside_function == True and list_of_lines[0] != '\n':
                output_lines.append('\n')
            output_lines.append(line)
    
        if '#' in line:
            if list_of_lines[0] != '\n':
                output_lines.append('\n')
            output_lines.append(line)
        else:
            output_lines.append(line)

        out_file.writelines(output_lines)
                            
                

def main():
    in_file = "Text files/code_test.py"
    out_file = "Text files/code_test_output.py"
    with (open(in_file, "r") as file_in,
            open(out_file, "w") as file_out):
        comments_for_functions(file_in, file_out)

    in_file = "Text files/code_test.py"
    out_file = "Text files/code_test_output_lines.py"
    with (open(in_file, "r") as file_in,
            open(out_file, "w") as file_out):
        add_blank_lines_around_functions(file_in, file_out)
if __name__ == "__main__":
    main()
