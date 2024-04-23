







file_name = 'Text files/my_cool_new_file.txt'
with open(file_name, 'w') as my_file:  
    big_string = ('This is a large string that even has multiple\n'
                  + 'lines in it. Hooray for that.')
    
    my_file.write(big_string)
    
    another_string = 'More text!'
    
    
    
    my_file.write(another_string)

    
    









in_file_name = 'Text files/names.txt'
out_file_name = 'Text files/lowercase_names.txt'




with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    for line in in_file:  
        line = line.lower()  
        out_file.write(line)  
        '''Note that 'line' still has the '\n' character at the end, so each
        name writes to a separate line in the new file. I never remember
        whether which read functions keep the '\n' character and which don't.
        1. If you're not sure, test it out!
        2. Make sure the code does whatever someone reading it would expect,
            and write a comment if you mean to do something that might be
            surprising.
        '''










in_file_name = 'Text files/names.txt'
out_file_name = 'Text files/lowercase_names_2.txt'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    list_of_lines = in_file.readlines()
    
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].lower()

    out_file.writelines(list_of_lines)  

'''Despite the name, writelines does NOT automatically put each string
on its own line. In particular, the code
    out_file.writelines(['lines', 'of', 'text'])
writes 'linesoftext' to the file. To write on separate lines, you want
    out_file.writelines(['lines\n', 'of\n', 'text\n'])
However, readlines keeps the '\n' character, so they work great together.
'''



def write_diamond_pattern(out_file, width):
    num_spaces = width // 2
    num_xs = 1
    out_file.write(' ' * num_spaces + 'x' * num_xs + '\n') 
    for line in range(width // 2): 
        num_spaces -= 1
        num_xs += 2
        out_file.write(' ' * num_spaces + 'x' * num_xs + '\n')
    for line in range(width // 2): 
        num_spaces += 1
        num_xs -= 2
        out_file.write(' ' * num_spaces + 'x' * num_xs + '\n')

file_name = 'Text files/diamonds.txt'
with open(file_name , 'w') as my_file:
    write_diamond_pattern(my_file, 5)


def last_name_first(in_file, out_file):
    for line in in_file: 
        words = line.split()
        out_file.write(word[1] + ', ' + word[0] + '\n') 



def add_and_write(in_file, out_file):
    for line in in_file:
        function = line 
        words = line.split()
        result = int(word[0]) + int(word[2]) 
        out_file.write(str(function) + ' = ' + str(result)) 



def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file:
        if len(line) > 20:
            out_file.write(line[15:] == ', blah blah blah')








        








        
