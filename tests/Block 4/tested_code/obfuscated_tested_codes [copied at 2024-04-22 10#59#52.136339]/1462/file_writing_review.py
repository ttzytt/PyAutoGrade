





'''
Prints a diamond of a specific width in an opened file.
    inputs:
        out_file    An opened file that is open for writing.
        width       The width of the printed diamond.
'''
def write_diamond_pattern(out_file, width):

    
    for i in range(1, width + 1, 2):
        out_file.write(" " * int((width - i)/2))
        out_file.write("x" * i)
        out_file.write('\n')
        
    for i in range(2 - width, 0, 2):
        for _ in range(int((width + i)/2)):
            out_file.write(" ")
        for _ in range(-i):
            out_file.write('x')
        out_file.write('\n')
    



'''
Converts and prints (first name last name) into (last name, first name)
in an opened file.
    inputs:
        in_file     An opened file that we take the inputs from.
        out_file    An opened file that is open for writing.
'''
def last_name_first(in_file, out_file):
    for line in in_file:
        name = line.split()
        out_file.write(name[1] + ', ' + name[0] + '\n')




'''
Prints out an addition problem inputed and the answer of it.
    inputs:
        in_file     An opened file that we take the inputs from.
        out_file    An opened file that is open for writing.
'''
def add_and_write(in_file, out_file):
    for line in in_file:
        terms = line.split()
        
        if line[-1] == '\n':
            line = line[:-1]
        out_file.write(line + ' = ' + str(int(terms[0]) + int(terms[2])) + '\n')




'''
Prints the lines from the input file, if one line is more than 20 characters,
we replace it with just the first 15 characters followed by the string ', blah blah blah'
    inputs:
        in_file_name    The opened file name that we take the inputs from.
        out_file_name   The opened file name that we write in.
'''
def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        for line in in_file:
            
            if line[-1] == '\n':
                line = line[:-1]
            count = 0
            words = line.split()
            for word in words:
                count += len(word)

            if count > 20:
                line = line[:15]
                out_file.write(line + ', blah blah blah\n')
            else:
                out_file.write(line + '\n')
              


def main():
    
    file_name = 'Text files/testingt11.txt'
    with open(file_name, 'w') as my_file:
        write_diamond_pattern(my_file, 11)

    
    in_file_name = 'Text files/names.txt'
    out_file_name = 'Text files/testingt12.txt'
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        last_name_first(in_file, out_file)
        
    
    in_file_name = 'Text files/addition.txt'
    out_file_name = 'Text files/testingt13.txt'
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        add_and_write(in_file, out_file)
    
    
    in_file_name = 'Text files/greeneggs.txt'
    out_file_name = 'Text files/testingt14.txt'
    blah_blah_blah(in_file_name, out_file_name) 
    
    
    
    
    


