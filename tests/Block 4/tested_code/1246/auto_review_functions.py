






def comments_for_functions(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
          open(out_file_name, 'w') as out_file):

        list_of_lines = in_file.readlines()

        

        line_counter = 0

        while line_counter < len(list_of_lines):

            line = list_of_lines[line_counter]

            print()
            print('loop')
            print(line)
            print(len(line))

            print('loop number: ' + str(line_counter))

            if 'def' in line:
                print('function found')
                if line_counter == 0:
                    list_of_lines.insert(line_counter, '# R(auto) Add a comment that says what this function does!\n')
                    line_counter += 1

                elif len(list_of_lines[line_counter - 1]) <= 1 or list_of_lines[line_counter - 1].split()[0][0] != '#':

                    print('len of previous line: ')
                    print(len(list_of_lines[line_counter - 1]))
                    print(list_of_lines[line_counter - 1])

                    list_of_lines.insert(line_counter, '# R(auto) Add a comment that says what this function does!\n')
                    line_counter += 1
                print('len of previous line: ')
                print(len(list_of_lines[line_counter - 1]))
                print(list_of_lines[line_counter - 1])
            
            
            

            

            line_counter += 1

        out_file.writelines(list_of_lines)




def blank_lines_around_functions_old_ver(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
          open(out_file_name, 'w') as out_file):

        list_of_lines = in_file.readlines()

        
        line_counter = 0

        while line_counter < len(list_of_lines):

            print('len:' + str(len(list_of_lines)))

            
            line = list_of_lines[line_counter]
            print()
            print('loop')
            print()
            print(line)

            

            
            
            if 'def ' == line[:4]:
                print('function found')

                function_line = line_counter

                while list_of_lines[function_line] == '\n' or list_of_lines[function_line][0] == ' ':
                    function_line += 1

                have_blank_after = False

                if list_of_lines[function_line - 2] != '\n' or list_of_lines[function_line - 1][0] != ' ':
                    list_of_lines.insert(function_line, '\n')
                    print('insert')
                    have_blank_after = True

                    

                
                

                prev_line = list_of_lines[line_counter - 1]

                
                if line_counter == 0:
                    list_of_lines.insert(line_counter, '\n')

                
                elif '#' not in prev_line:
                    if prev_line != '\n':
                        
                        have_blank = False
                        
                        for i in range(len(prev_line)):
                            if prev_line[i] != ' ':
                                list_of_lines.insert(line_counter, '\n')
                                have_blank = True
                                break

                        
                        if not have_blank:
                            list_of_lines.insert(line_counter, '\n')

                
                elif '#' in prev_line:
                    num_line = line_counter - 1
                    while '#' in list_of_lines[num_line]:
                        num_line -= 1

                    if list_of_lines[num_line] != '\n':
                        
                        
                        
                        
                        list_of_lines.insert(num_line + 1, '\n')
                        line_counter += 1
                if have_blank_after:
                    line_counter += 1

            

            print('line_counter' + str(line_counter))
            line_counter += 1

        out_file.writelines(list_of_lines)



def blank_lines_around_functions(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
          open(out_file_name, 'w') as out_file):
        list_of_lines = in_file.readlines()
        
        line_counter = 0

        
        while line_counter < len(list_of_lines):
            print('line_counter: ' + str(line_counter))

            
            list_counter_line = list_of_lines[line_counter]

            if list_counter_line[:4] == 'def ':
                print()
                print("Function found")
                print()

                

                if line_counter == 0:
                    list_of_lines.insert(line_counter, '\n')

                before_counter = line_counter - 1

                while list_of_lines[before_counter][0] == '#':
                    print('    before_counter: ' + str(before_counter))
                    before_counter -= 1

                
                
                
                if list_of_lines[before_counter] != '\n' and list_of_lines[before_counter][0] != ' ':
                    
                    
                    list_of_lines.insert(before_counter + 1, '\n')
                    print()
                    print('line inserted at line ' + str(before_counter))
                    print()
                    
                    line_counter += 1

                
                after_counter = line_counter + 1

                
                
                while list_of_lines[after_counter] == '\n' or list_of_lines[after_counter][0] == ' ':
                    print('    after_counter: ' + str(after_counter))
                    after_counter += 1

                
                if list_of_lines[after_counter - 1] != '\n' and list_of_lines[after_counter][0] != ' ':
                    
                    
                    
                    
                    list_of_lines.insert(after_counter, '\n')
                    print()
                    print('line inserted at line ' + str(after_counter - 1))
                    print()
                    line_counter += 1

            line_counter += 1

        out_file.writelines(list_of_lines)


def main():
    in_file_name = 'Text files/auto_comment.py'
    out_file_name = 'Text files/auto_comment_add.py'
    comments_for_functions(in_file_name, out_file_name)
    blank_lines_around_functions('Text files/auto_comment_2.py', 'Text files/auto_comment_2_add.py')


if __name__ == "__main__":
    main()
