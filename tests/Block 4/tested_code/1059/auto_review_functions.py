def comments_for_functions(in_file, out_file):
    lines = in_file_name.read()
    print(lines)
    line = lines.split()
    i = 0
    '''
    while i < len(line):
        if len(line[i]) > 20:
            temp_str = line[i][0:15] + ', blah blah blah' 
            # From 0-15 words in the orginal sentence.
            out_file_name.write(temp_str)
            out_file_name.write("\n")
            # Change line every time a line is written in the file
        elif len(line[i]) <= 20:
            out_file_name.write(line[i])
            out_file_name.write("\n")
        i += 1
'''

with (open('Text files/T15_read.py', 'r') as in_file_name,
        open('Text files/T15_write.py', 'w') as out_file_name):
