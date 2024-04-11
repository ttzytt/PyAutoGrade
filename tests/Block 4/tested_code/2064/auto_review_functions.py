







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
                    out_file.write('#R(auto): Add a comment that says what this '
                                   'function does!\n')
        else:
            word_two = ''
            
        word_one = word_two
        out_file.write(line)


'''
If there are no blank lines around functions (or around  function and comment),
adds a blank line for every place there isn't. CAUTION opens entire file
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def blank_lines_around_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if (list_of_lines[i][:4] == 'def '):
            j = 0
            while (i > j):
                print(list_of_lines[i - j][:1])
                if(list_of_lines[i - j] == '\n'):
                    j += i
                elif(list_of_lines[i - j][:1] == '
                    print('hello')
                    print(list_of_lines[i - j][:1])
                    j += 1
                else:
                    j += i
                    list_of_lines.insert(i - j, '\n')
                    
    for i in range(len(list_of_lines)):
        out_file.write(list_of_lines[i])
                    

            
        
    

                    
            




        



def main():
    in_file_name = 'Text files/workshopped_test_file.txt'
    out_file_name = 'Text files/writingtestsfile.txt'
    with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
        blank_lines_around_functions(in_file, out_file)


if __name__ == "__main__":
    main()

