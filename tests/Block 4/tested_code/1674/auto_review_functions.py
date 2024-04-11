

'''
Write a reminder for a comment for each function
inputs:
    out_file   A file open for writing
    in_file    A file open for reading
'''

def comments_for_functions(in_file, out_file):
    for line in in_file:
        words = line.split() 
        if "def" in words and "#" not in line:
            line = line[::] + comment  + '\n'
        out_file.write(line)
                

comment = '#R(auto): Add a comment that says what this function does!'
in_file_name ='file_reading.py'
out_file_name = 'reading_files.py'
with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    comments_for_functions(in_file, out_file)


