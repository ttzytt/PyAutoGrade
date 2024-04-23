










'''
Writes a diamond pattern with a specified size to a file.

    inputs:
        width - the specified width
    outputs:
        the file being written to
'''
def write_diamond_pattern(out_file, width):
    with open(out_file, 'w') as my_file:
        
        counter = 1
        
        while counter < width:
            my_file.write(' ' * int((width - counter) / 2) + 'x' * counter + '\n')
            counter += 2
        
        while counter >= 1:
            my_file.write(' ' * int((width - counter) / 2) + 'x' * counter + '\n')
            counter -= 2
            

'''
Takes in a file with a list of names and writes it to a file with
the names in a reverse orders. I.E. John Doe becomes Doe, John

    inputs:
        in_file - the file being read
    outputs:
        out_file - the file being written to
'''
def last_name_first(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        for line in in_file:
            
            each_name = line.split()
            out_file.write(each_name[1] + ', ' + each_name[0] + '\n')


'''
Takes in a file with a list of addition equations and writes the 
entirety of each equation including the sum to a file.

    inputs:
        in_file - the file being read
    outputs:
        out_file - the file being written to
'''
def add_and_write(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        number_list = []
        for line in in_file:
            numbers = line.split()
            
            
            num_1 = numbers[0]
            num_2 = numbers[2]
            sum = int(num_2) + int(num_1)
            out_file.write(num_1 + '+' + num_2 + ' = ' + str(sum) + '\n')
            

'''
Takes in a file and writes it to another file, but each line with
more than 20 characters has the characters > 15 replaced with
",blah blah blah"

    inputs:
        in_file - the file being read
    outputs:
        out_file - the file being written to
'''            
def blah_blah_blah(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        for line in in_file:
            if len(line) > 20:
                
                mod_line = line[0:15] + ', blah blah blah'
                
                out_file.write(mod_line + '\n')
            else:
                out_file.write(line)
                

'''
Runs each function in the file.
'''
def main():
    last_name_first('Text files/names.txt', 'Text files/last_names_first.txt')
    write_diamond_pattern('Text files/diamond.txt', 5)
    add_and_write('Text files/addition.txt', 'Text files/add_and_write.txt')
    blah_blah_blah('Text files/greeneggs.txt', 'Text files/blah blah blah')

    

if __name__ == '__main__':
    main()
