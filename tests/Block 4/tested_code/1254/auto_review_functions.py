



'''
Returns a file with a comment before any functions without a comment before it explaining what it does.
Inputs:
    in_file   A file open for reading
    out_file  A file open for writing
'''
def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if list_of_lines[i][:3] == 'def':
            if list_of_lines[i - 1][2] == "'''":
                
