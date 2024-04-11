'''
Written by Alex
TASK 11-14
'''



import random
random.seed()

'''----------------------FUNCTIONS------------------------'''


def write_diamond_pattern(out_file, width):
    string_d = ''
    for n in range(1,width,2):
        string_d += n * 'x'
        string_d += '\n'
    
    
    for n in range(width,0,-2):
        string_d += n * 'x'
        string_d += '\n'
    
    
    return string_d



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




def last_name_first(in_file, out_file):
    new_names = ''
    for line in in_file:
        splited_line = line.split()
        new_names += str(splited_line[1]) 
        new_names += ', '
        new_names += str(splited_line[0]) 
        new_names += '\n'
    return new_names
    




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

        

'''------------------------TESTS-------------------------'''

# T11
print('T11 finished')
file_name = 'Text files/write_diamond_pattern.txt'
with open(file_name, 'w') as my_file:
    width = 11
    diamond = write_diamond_pattern(my_file, width)
    my_file.write(diamond)
print()

# T12
print('T12 finished')
input_file = 'Text files/names.txt'
output_file = 'Text files/last_name_first.txt'
with (open(input_file, 'r') as my_file1,
      open(output_file, 'w') as my_file2):
    new_name = last_name_first(my_file1,my_file2)
    my_file2.write(new_name)
print()

# T13
print('T13 finished')
input_file = 'Text files/addition.txt'
output_file = 'Text files/addition_solutions.txt'
with (open(input_file, 'r') as my_file1,
      open(output_file, 'w') as my_file2):
    solutions = add_and_write(my_file1,my_file2)
    my_file2.write(solutions)
print()

# T14
print('T14 finished')
input_file = 'Unit 2/payphone_lyrics.py'
output_file = 'Text files/blah blah blah.txt'
with (open(input_file,'r') as my_file1,
      open(output_file,'w') as my_file2):
    blah = blah_blah_blah(my_file1,my_file2)
    my_file2.write(blah)
