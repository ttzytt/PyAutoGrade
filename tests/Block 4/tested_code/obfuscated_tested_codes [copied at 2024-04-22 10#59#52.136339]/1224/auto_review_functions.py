




def comments_for_functions(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        list_of_lines = in_file.readlines()
        
        for i in range(len(list_of_lines) - 1):
            out_file.write(list_of_lines[i])
            if list_of_lines[i + 1][0:3] == 'def':
                if list_of_lines[i] != '#':
                    out_file.write('#R(auto): Add a comment that says what this function does! \n')
        out_file.write(list_of_lines[len(list_of_lines) - 1])

def blank_lines_around_functions(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        list_of_lines = in_file.readlines()
        
        for i in range(len(list_of_lines) - 1):
            out_file.write(list_of_lines[i])
            if list_of_lines[i + 1][0] == '#':
                out_file.write('\n')
                
        for i in range(len(list_of_lines) - 1):
            if list_of_lines[i][:3] == 'def':
                while counter < len(list_of_lines) and list_of_lines[counter] == '\n' or list_of_lines[counter] == '\t':

    
                    
                    
        out_file.write(list_of_lines[len(list_of_lines) - 1])

        
in_file = 'Text files/test_file.txt' 
out_file = 'Text files/test_file_redone.txt'
comments_for_functions(in_file, out_file)


in_file = 'Text files/test_file2.txt' 
out_file = 'Text files/test_file_redone2.txt'
blank_lines_around_functions(in_file, out_file)
