




'''
Returns a file that adds the comment with '
if there's supposed to be a comment above the 'def' of the function but there isn't.
    inputs:
       in_file    An opened file that we take the inputs from.
       out_file   An opened file that is open for writing.
    
'''
def comments_for_functions(in_file, out_file):

    comment = '
    i = 0
    
    list_of_lines = in_file.readlines() 
    while i < len(list_of_lines):

        if list_of_lines[i][:4] == 'def ':
            
            if list_of_lines[i - 1][0] != '#':
                list_of_lines.insert(i, comment)
                i += 2
            else:
                i += 1
        else:
            i += 1
    out_file.writelines(list_of_lines)
    
                    


'''
Returns a file that adds a blank line above and below a function if there isn't one.
    inputs:
       in_file    An opened file that we take the inputs from.
       out_file   An opened file that is open for writing.

'''
def blank_lines_around_functions(in_file, out_file):

    i = 1

    list_of_lines = in_file.readlines()

    if list_of_lines[0][:4] == 'def ':
        list_of_lines.insert(0, '\n')
                             
    while i < len(list_of_lines):
        current_i = i
        # Before.
        if list_of_lines[i][:4] == 'def ':

            
            while list_of_lines[i - 1] == '
                i += -1

            if list_of_lines[i - 1] != '\n':
                list_of_lines.insert( i, '\n')
                current_i += 1

        i = current_i

        
        if list_of_lines[i][:4] == 'def ':

            i = i + 1
            while i < len(list_of_lines) and (list_of_lines[i][0] == ' ' or '\n'):
                i += 1
            print(1)  
            if list_of_lines[i - 1] != '\n':
                list_of_lines.insert( i, '\n')

        i = current_i + 1
        
    out_file.writelines(list_of_lines)
        
        
 
def main():

    
    
    in_file_name = 'Unit 1/List functions/list_functions.py'
    out_file_name = 'Text files/testingt15.txt'
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        comments_for_functions(in_file, out_file)

    
    in_file_name = 'Text files/t16_input.txt'
    out_file_name = 'Text files/testingt16.txt'
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)

if __name__ == "__main__":
    main()
