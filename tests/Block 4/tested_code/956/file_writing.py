





'''
Suppose out_file is a file open for writing and width is a positive odd integer. This function
should print a “diamond” of x’s with the given width. For example, with width = 3, it should write
x xxx x
to the file and with width = 5, it should write x
 xxx
xxxxx
 xxx
  x
to the file.
    inputs:
        out_file    A file that is open for reading.
        width
'''
def write_diamond_pattern(out_file, width):
    string_d = ''
    for n in range(1,width,2):
        string_d += n * 'x'
        string_d += '\n'
    
    
    for n in range(width,0,-2):
        string_d += n * 'x'
        string_d += '\n'
    
    
    return string_d

'''
Suppose you have a file in which each line contains a first and last name,
separated by a space, as in James Bond. But you need the last names first,
and a comma in between, as in
Bond, James. Write a function that solves this problem (and try it on names.txt).
    inputs:
        out_file    A file that is open for reading.
        width
'''
def last_name_first(in_file, out_file):
    new_names = ''
    for line in in_file:
        splited_line = line.split()
        new_names += str(splited_line[1]) 
        new_names += ', '
        new_names += str(splited_line[0]) 
        new_names += '\n'
    return new_names

'''
Suppose you have a file in which each line contains an addition problem, for example 2 + 3.
You want a new file that has this problem as well as the answer, in this case 2 + 3 = 5.
Write a function that solves this problem (and try it on addition.txt).
    inputs:
        out_file    A file that is open for reading.
        width
'''
def add_and_write(in_file, out_file):
    new_string = ''
    for line in in_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            new_string += splited_line[n]
            new_string += ' '
            
            
        new_string += '= '
        new_string += str(int(splited_line[0]) + int(splited_line[2]))
        new_string += '\n'
        
        
    return new_string

'''
Suppose you have a file that contains a lot of text. Too much.
Whose got time for all that text? Any time a line is longer than 20 characters,
you want to replace it with just the first 15 characters followed by the string ',
blah blah blah'. (If a line is 20 characters or less, leave it alone.)
Write a function that solves this problem.
    inputs:
        out_file    A file that is open for reading.
        width
'''
def blah_blah_blah(in_file_name, out_file_name):
    new_string = ''
    for line in in_file_name:
        characters_in_line = 0
        splited_line = line.split()
        for n in range(len(splited_line)):
            word = splited_line[n]
            
            for i in range(len(word)):
                if word[i] != ',' and word[i] != '.':
                    characters_in_line += 1
                    

        
        if characters_in_line <= 20:
            new_string += line
            '''
            new_string += '\n'
            '''
            
            
        
        elif characters_in_line > 20:
            word_count = 0
            n = 0
            while word_count < 15:
                new_string += line[n]
                if line[n] != ' ' and line[n] != ',' and line[n] != '.' and line[n] != '\'':
                    word_count += 1
                n += 1
            new_string += ', blah blah blah'
            new_string += '\n'
    return new_string

'''
Important note: The inputs to this function are file names, not files.
Make sure your function opens these files.
Also, make sure the comments for each function say whether inputs are file names
or files opened for reading/writing.
'''
    
# –––––––––––––––––––––– Main function ––––––––––––––––––––––

def main():
    print('T11 finished')
    file_name = 'Text files/write_diamond_pattern.txt'
    with open(file_name, 'w') as my_file:
        width = 11
        diamond = write_diamond_pattern(my_file, width)
        my_file.write(diamond)
    print()

    print('T12 finished')
    input_file = 'Text files/names.txt'
    output_file = 'Text files/last_name_first.txt'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        new_name = last_name_first(my_file1,my_file2)
        my_file2.write(new_name)
    print()

    print('T13 finished')
    input_file = 'Text files/addition.txt'
    output_file = 'Text files/addition_solutions.txt'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        solutions = add_and_write(my_file1,my_file2)
        my_file2.write(solutions)
    print()

    print('T14 finished')
    input_file = 'Text files/names.txt'
    output_file = 'Text files/blah blah blah.txt'
    with (open(input_file,'r') as my_file1,
          open(output_file,'w') as my_file2):
        blah = blah_blah_blah(my_file1,my_file2)
        my_file2.write(blah)
    
if __name__ == "__main__":
    main()
