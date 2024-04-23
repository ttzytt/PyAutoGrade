



'''
Returns a file with a comment before any functions without a comment before it explaining what it does.
Inputs:
    in_file   A file open for reading
    out_file  A file open for writing
'''
def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if list_of_lines[i][:4] == 'def ':
            if list_of_lines[i - 1][:] != "'''":
                out_file.write('#R(auto): Add a comment that says what this function does!\n')
        out_file.write(list_of_lines[i])


'''
Adds a blank line before and after a function if there isn't one already
Inputs:
    in_file   A file open for reading
    out_file  A file open for writing
'''
def blank_lines_around_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    current_line = 0
    while current_line < len(list_of_lines):
        if list_of_lines[current_line][:4] == 'def ':
            # Adding a blank line before the comments on the functions
            if list_of_lines[current_line - 1][:] == "'''\n":
                comment_line_tracker = current_line - 2
                while list_of_lines[comment_line_tracker] != "'''\n":
                    comment_line_tracker -= 1
                list_of_lines.insert((comment_line_tracker), '\n')
                current_line += 1
            # Adding a blank line before the function if no comment
            elif list_of_lines[current_line - 1][:] != "'''\n":
                list_of_lines.insert((current_line -1), '\n')
                current_line += 1
            # Adding blank line after function
            end_of_function_tracker = current_line + 1
            while list_of_lines[end_of_function_tracker][0] == ' ' or list_of_lines[end_of_function_tracker] == '\n':
                end_of_function_tracker += 1
            if list_of_lines[end_of_function_tracker - 1] != '\n':
                list_of_lines.insert(end_of_function_tracker, '\n')
                current_line += 1
                
        current_line += 1

    for i in range(len(list_of_lines)):
        out_file.write(list_of_lines[i])

'''
Adds a comment before lines of code that are longer than 79 characters (not counting \n character
that reminds the coder to break the line up
'''

            

#----------------------- Testing Section ------------------------
def main():               
    in_file_name = 'Text files/test_auto_review.py'
    out_file_name = 'Text files/testing_comment_review.py'
    with (open(in_file_name, 'r') as in_file,
          open(out_file_name, 'w') as out_file):
        comments_for_functions(in_file, out_file)

    in_file_name = 'Text files/test_auto_review.py'
    out_file_name = 'Text files/testing_blank_line_review.py'
    with (open(in_file_name, 'r') as in_file,
          open(out_file_name, 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)

if __name__ == "__main__":
    main()
