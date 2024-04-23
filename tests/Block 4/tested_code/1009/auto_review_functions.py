





def comments_for_functions(in_file, out_file):
    lines = in_file.readlines()

    for line in lines:
        
        if line.startswith('def ') and not line.startswith('#'):
            out_file.write("#R(auto): Add a comment that says what this function does!\n")

        out_file.write(line)

in_file_name = 'file_writting.py'
out_file_name = 'Text files/file_output.py'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    comments_for_functions(in_file, out_file)


def blank_lines_around_functions(in_file, out_file):
    lines = in_file.readlines()

    is_function = False
    
    for line in lines:
        
        line_stripped = line.strip()
        
        if line_change.startswith('def '):
            if is_function:
                
                out_file.write('\n')
                is_function = True
        
        elif is_function:
            out_file.write('\n')
            is_function = False

        out_file.write(line)
            
in_file_name = 'file_writting.py'
out_file_name = 'Text files/file_output_2.py'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    blank_lines_around_functions(in_file, out_file)
        


def break_up_long_lines(in_file, out_file):
    lines = in_file.readlines()

    for line in lines:
        if len(line) > 79:
            out_file.write('#R(auto): Line of code is too long. Break it up!\n')

        out_file.write(line)
        
in_file_name = 'file_writting.py'
out_file_name = 'Text files/file_output_3.py'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    break_up_long_lines(in_file, out_file)


def spaces_after_commas(in_file, out_file):
    lines = in_file.readlines()

    for line in lines:
        parts = line.split(',')
        modified_line = ''

        for part in parts[:-1]:
            modified_line += part.strip() + ', '
            modified_line += parts[-1].strip()
            
            out_file.write(modified_line + '\n')
        
in_file_name = 'file_writting.py'
out_file_name = 'Text files/file_output_4.py'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    spaces_after_commas(in_file, out_file)
