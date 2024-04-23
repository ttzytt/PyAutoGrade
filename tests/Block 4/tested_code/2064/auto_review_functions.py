










'''
When there's a function definition in the file without a comment on the line
before, add a line of code that says '#R(auto): Add a comment that says what
this function does!'
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def comments_for_functions(in_file, out_file):
    word_one = ''
    for line in in_file:
        words = line.split()
        if (len(words) > 0):
            word_two = words[0]
            if (word_two == 'def'):
                if ((word_one != '
                        (word_one != '"""')):
                    out_file.write('#R(auto): Add a comment that says what this'
                                   ' function does!\n')
        else:
            word_two = ''
            
        word_one = word_two
        out_file.write(line)


'''
If there are no blank lines around functions (or around  function and comment),
adds a blank line for every place there isn't. If there is not 
CAUTION: opens entire file
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def blank_lines_around_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if (list_of_lines[i][:4] == 'def '):
            # i is the line index
            num_lines_of_comments = 0
            while (i > num_lines_of_comments
                   and list_of_lines[i - (num_lines_of_comments + 1)][:1] == '
                num_lines_of_comments += 1

            if (list_of_lines[i - (num_lines_of_comments + 1)].split() != []):
                list_of_lines.insert(i - num_lines_of_comments, '\n')
                    
    for i in range(len(list_of_lines)):
        out_file.write(list_of_lines[i])


'''
If a line of code is too long, adds a review comment on the line before it that
says '
CAUTION: opens entire file
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def break_up_long_lines(in_file, out_file):
    list_of_lines = in_file.readlines()
    i = 0
    while (i < len(list_of_lines)):
        if (len(list_of_lines[i]) > 81):
            if (i > 0):
                list_of_lines.insert(i, '
                                     'long. Break it up!\n')
            else:
                list_of_lines.insert(0, '#R(auto): Line of code is too '
                                     'long. Break it up!\n')
            i+= 1
                
        elif ((len(list_of_lines[i]) > 79) and (list_of_lines[i][-1] != '\n')):
            if (i > 0):
                print(list_of_lines[i][-1])
                list_of_lines.insert(i, '#R(auto): Line of code is too '
                                     'long. Break it up!\n')
            else:
                list_of_lines.insert(0, '#R(auto): Line of code is too '
                                     'long. Break it up!\n')
            i += 1

        i += 1
        
    for i in range(len(list_of_lines)):
        out_file.write(list_of_lines[i])

                
'''
If a there is a comma not folowed by a space or end of line charecter or ' or ", adds a
space.
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''                
def spaces_after_commas(in_file, out_file):
    for line in in_file:
        for i in range(len(line)):
            if (line[i] == ','):
                
                
                



            
        
    

                    
            



# –––––––––––––––––––––– Main function ––––––––––––––––––––––
        



def main():
    in_file_name = 'Text files/workshopped_test_file.txt'
    out_file_name = 'Text files/writingtestsfile.txt'
    with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
        break_up_long_lines(in_file, out_file)


if __name__ == "__main__":
    main()

