







'''
Write a diamond pattern to the given file.
Inputs:
out_file: A file open for writing.
width: A positive odd integer representing the width of the diamond.
'''
def write_diamond_pattern(outfile, width):
    
    for i in range(1, width // 2 + 2):
        out_file.write(' ' * (width // 2 + 1 - i))
        out_file.write('x' * (2 * i - 1))
        out_file.write('\n')

    
    for i in range(width // 2, 0, -1):
        out_file.write(' ' * (width // 2 + 1 - i))
        out_file.write('x' * (2 * i - 1))
        out_file.write('\n')

'''
Write a code to make the name sequence reverse and add comma between.
Inputs: names.txt
outfile: A file open for writing.
'''
def last_name_first(in_file, out_file):
    for line in in_file:
        
        first_name, last_name = line.strip().split()
        
        out_file.write(f'{last_name}, {first_name}\n')

'''
Write a code to solve the addition problem that appears at the above line.
Inputs: 
outfile: A file open for writing.
'''
def add_and_write(in_file, out_file):
    for line in in_file:
        adds = line.strip().split('+')
        if len(adds) == 2:
            num1, num2 = adds
            if num1.isdigit() and num2.isdigit():
                result = int(num1) + int(num2)
                out_file.write(f'{line.strip()} = {result}\n')


'''
Write a code to replace the characters that are longer than 20 with "blah blah
blah".
Inputs:
Outfiles: A file open for writing.
'''
def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file:
        if len(line.strip()) > 20:
            extra = line[:20] + ' blah blah blah\n'
            out_file.write(extra)
        else:
            out_file.write(line)


file_name = 'Text files/diamond_pattern.txt'
width = 5
with open(file_name, 'w') as out_file:
    write_diamond_pattern(out_file, width)


in_file_name = 'Text files/name.txt'
out_file_name = 'Text files/lowercase_names_2.txt'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    
    last_name_first(in_file, out_file)


in_file_name = 'Text files/addition.txt'
out_file_name = 'Text files/addition_answer_2.txt'
with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    add_and_write(in_file, out_file)


in_file_name = 'Text files/words.txt'
out_file_name = 'Text files/words_2.txt'
with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    blah_blah_blah(in_file_name, out_file_name)


