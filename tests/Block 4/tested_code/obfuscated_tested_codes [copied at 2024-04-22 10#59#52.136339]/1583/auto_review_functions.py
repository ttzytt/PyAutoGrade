






def is_blank_line(line):
    return line.strip() == ''







def count_leading_spaces(line):
    character_index = 0
    while line[character_index] == ' ':
        character_index += 1

    return character_index











def comments_for_functions(in_file, out_file):
    in_file_contents = in_file.readlines()
    line_index = 0

    
    while line_index < len(in_file_contents):
        line = in_file_contents[line_index]
        if 'def ' in line:

            
            prev_line = in_file_contents[line_index-1].strip()
            if not ('#' in prev_line or "'''" in prev_line or '"""'
                    in prev_line):

                num_spaces = count_leading_spaces(line)
                    
                in_file_contents.insert(line_index,
                                        ' '*num_spaces + '#R(auto): '
                                        + 'Add a comment that says '
                                        + 'what this function does!\n')
                
                line_index += 1

        line_index += 1

    out_file.writelines(in_file_contents)


def blank_lines_around_functions(in_file, out_file):
    in_file_contents = in_file.readlines()
    line_index = 0
    in_function = False 
                        

    
    while line_index < len(in_file_contents) - 1:
        line = in_file_contents[line_index]

        
        
        
        
        
        next_line = in_file_contents[line_index+1]
        if (count_leading_spaces(line) == 0 and count_leading_spaces(next_line) == 0
            and not is_blank_line(next_line) and in_function == True and not is_blank_line(line):
            print('end insert: ' + str(line_index))
            in_function = False
            in_file_contents.insert(line_index, '\n')
            line_index += 1

        line = in_file_contents[line_index]
        
        
        if 'def ' in line:
            in_function = True
            
            
            prev_line_index = line_index - 1
            prev_line = in_file_contents[prev_line_index].strip()

            
            while not is_blank_line(prev_line) and prev_line[0] == '#':
                print(prev_line)
                print(prev_line_index)
                prev_line_index -= 1
                prev_line = in_file_contents[prev_line_index].strip()

            prev_line = in_file_contents[prev_line_index].strip()
            
            if not is_blank_line(prev_line):
                print('start insert: ' + str(prev_line_index))
                in_file_contents.insert(prev_line_index+1, '\n')
                line_index += 1
       
        line_index += 1

    out_file.writelines(in_file_contents)

def main():

    
    
    with (open('Text files/get_auto_reviewed.py', 'r') as in_file,
          open('Text files/get_auto_reviewed_comments.py', 'w') as out_file):
        comments_for_functions(in_file, out_file)


    
    
    with (open('Text files/get_auto_reviewed.py', 'r') as in_file,
          open('Text files/get_auto_reviewed_blank_lines.py', 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)

if __name__ == "__main__":
    main()
