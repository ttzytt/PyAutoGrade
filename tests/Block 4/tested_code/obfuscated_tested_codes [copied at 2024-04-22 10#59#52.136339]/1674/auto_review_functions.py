

"""
Write a comment for each function.

inputs:
    out_file: A file open for writing.
    in_file: A file open for reading.
"""
def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if "def" in list_of_lines[i] and "#" not in list_of_lines[i-1]:
            list_of_lines[i] = comment + '\n' + list_of_lines[i]
    out_file.writelines(list_of_lines) 

comment = '#R(auto): Add a comment that says what this function does!'
in_file_name = 'file_reading.py'
out_file_name = 'reading_files.py'

with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    comments_for_functions(in_file, out_file)




"""
Write a comment for each function that now includes """ """

inputs:
    out_file: A file open for writing.
    in_file: A file open for reading.
"""
def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if "def" in list_of_lines[i] and "#" not in list_of_lines[i-1] or "'''" not in list_of_lines[i-1] or '"""' not in list_of_lines[i-1] :
            list_of_lines[i] = comment + '\n' + list_of_lines[i]
    out_file.writelines(list_of_lines) 

comment = '#R(auto): Add a comment that says what this function does!'
in_file_name = 'file_practice.py'
out_file_name = 'practice_files2.py'

with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    comments_for_functions(in_file, out_file)
    


"""
Write a blank line before and after each function if there isn't one

inputs:
    out_file: A file open for writing.
    in_file: A file open for reading.
"""
def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if "#" in list_of_lines[i] and "        " not in list_of_lines[i]:
            list_of_lines[i] = list_of_lines[i] + '\n'
    out_file.writelines(list_of_lines) 


in_file_name = 'file_reading.py'
out_file_name = 'space_for_comments.py'

with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    comments_for_functions(in_file, out_file)

