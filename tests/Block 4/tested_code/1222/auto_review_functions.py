



import random
random.seed()



'''
Inserts a line of code above a function if it doesn't have a comment already
    inputs:
        in_file     (A File that is open for reading)
        out_file    (A new temp file that is created for storing information)
        
'''

def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    new_lines = []
    comment_needed = False
    comment_above = False
    for line in range(len(list_of_lines)):
        j = 0  
        if 'def '  == list_of_lines[line][:4]:
            comment_needed = True
            if list_of_lines[0] == '\n':
                comment_needed = True
            else:
                while j < line:
                    if '
                        comment_above = True
                        comment_needed = False
                        j += 1
                    elif comment_above == False:
                        comment_needed = True
    print(comment_needed, comment_above)
    if comment_needed == True:
        new_lines.append('#R(auto): Add a comment that says what this function does!')
    out_file.writelines(new_lines)
    out_file.writelines('\n')
    out_file.writelines(list_of_lines)
    

'''
Inserts a blank line above a function and comments if there isn't already one
    inputs:
        in_file     (A File that is open for reading)
        out_file    (A file that is open for writing)
'''

# ------------------------------------Open & Run--------------------------------------------
def main():
    in_file_name = 'Text Filesfile_practice.py'
    out_file_name = 'Text Files/auto_comment.txt'
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        auto_comment = comments_for_functions(in_file, out_file)
    print('T15 Completed')
if __name__ == "__main__":
    main()

                
