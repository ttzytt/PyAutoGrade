




def comments_for_functions(in_file, out_file):
    lines = in_file.readlines()
    for i in range(len(lines)):
        if i-1 < 0 and 'def ' in lines[i]:
            out_file.write('#R(auto): Add a comment that says what this function does!\n')
        if 'def ' in lines[i] and ('#' and '"""' and "'''" not in lines[i-1]):
            out_file.write('#R(auto): Add a comment that says what this function does!\n')
        out_file.write(lines[i])
  



def blank_lines_around_functions(in_file, out_file):
    lines = in_file.readlines()
    print(lines)
    for i in range(len(lines)):
        if 'def ' in lines[i] and lines[i-1] != ' ':
            out_file.write('\n')
        elif '#' in lines[i] and 'def ' in lines[i+1] and lines[i-1] != ' ': 
            out_file.write('\n')
        elif lines[i-1][:4] == '    ' and lines[i][:4] != '    ':
            out_file.write('#R add a blank line\n')

        out_file.write(lines[i])
        


def break_up_long_lines(in_file, out_file):
    lines = in_file.readlines()
    for i in range(len(lines)):
        if '\n' not in line[i]:
            if len(lines[i]) >= 79:
                out_file.write('#R(auto): Line of code is too long. Break it up!')
        elif len(line[i]) >= 77:
            out_file.write('#R(auto): Line of code is too long. Break it up!')
        out_file.write(lines[i])
    

def spaces_after_commas(in_file, out_file):
    lines = in_file.readlines()
    print(lines)
    for i in range(len(lines)):
        out_file.write('\n')

        for j in range(len(lines[i])):
            
            if j+1 < len(lines[i]):
                if lines[i][j] == ',' and lines[i][j+1] != ' ':
                    out_file.write(lines[i][j]+' ')
                else:
                    out_file.write(lines[i][j])
                











def main():
    in_file_name_1 = 'Text files/auto_review_in_file.py'
    out_file_name = 'Text files/auto_review_out_file.py'

    '''
    # T15 auto commenting     
    with (open(in_file_name_1,'r') as in_file,
             open(out_file_name, 'w')as out_file): # run the last name first function
            comments_for_functions(in_file, out_file)
    '''
    
    with (open(in_file_name_1,'r') as in_file,
             open(out_file_name, 'w')as out_file): 
            blank_lines_around_functions(in_file, out_file)
    '''
    # T17 79 character long line
    with (open(in_file_name_1,'r') as in_file,
             open(out_file_name, 'w')as out_file): # run the last name first function
            break_up_long_lines(in_file, out_file)
    
    # T18 spaces after comma
    with (open(in_file_name_1,'r') as in_file,
             open(out_file_name, 'w')as out_file): # run the last name first function
            spaces_after_commas(in_file, out_file)
    '''
main()
