




"""
T15, B1
Goes through a python file and finds any function defenition in the file without a comment
on the line before and adds a line of code that says
'#R(auto): Add a comment that says what this function does!'. Assume every comment starts with 
a #. out_file is a copy of the in_file with the additional comments

    inputs:
            in_file                    a file open to read from

            out_file                   a file open to write in
"""
def comments_for_functions(in_file, out_file):
    lines = in_file.readlines() 
    line_number = 1 
    
    while line_number < len(lines): 
        if len(lines[line_number]) > 4:
            if lines[line_number][:4] == 'def ':
                
                prev_lin = lines[line_number - 1]
                
                if prev_lin[:1] != '#' and prev_lin[:5] != '"""\n' and prev_lin[:5] != "'''\n": 
                    lines.insert(line_number - 1,
                             '#R(auto): Add a comment that says what this function does!')
                    
                    if line_number != len(lines):
                        line_number += 1 
        
        if line_number != len(lines): 
            line_number += 1
            
        if line_number == len(lines): 
            out_file.writelines(lines)

"""
T16
Goes through a python file and checks if there is a blank line before the comment and after
every function and adds one if there isn't.
    inputs:
            in_file                    a file open to read from

            out_file                   a file open to write in
"""
def blank_lines_around_functions(in_file, out_file):
    lines = in_file.readlines()
    line_number = 1
    while line_number < len(lines):
        if len(lines[line_number]) > 4:
            if lines[line_number][:4] == 'def ':
                prev_lin = lines[line_number - 1]
                if prev_lin[:2] == '# ': 
                    lines.insert(line_number - 2, '\n')
                    line_number += 1
                else:
                    lines.insert(line_number - 1, '\n')
                    line_number += 1

                end_line_number = line_number
                while lines[end_line_number][:4] == '    ':
                    end_line_number += 1
                    
                lines.insert(end_line_number, '\n')
                line_number += 1
                
                
        if line_number != len(lines): 
            line_number += 1
            
        if line_number == len(lines): 
            out_file.writelines(lines)


def main():

    file_name_CFF_in = 'Text files/comments_for_functions_in.py'
    file_name_CFF_out = 'Text files/comments_for_functions_out.py'
    with open(file_name_CFF_in, 'r') as in_file:
        with open(file_name_CFF_out, 'w') as out_file:
            comments_for_functions(in_file, out_file)

            
    file_name_BLF_in = 'Text files/blank_lines_around_functions_in.py'
    file_name_BLF_out = 'Text files/blank_lines_around_functions_out.py'
    with open(file_name_BLF_in, 'r') as in_file:
        with open(file_name_BLF_out, 'w') as out_file:
            blank_lines_around_functions(in_file, out_file)
        
if __name__ == "__main__":
    main()
