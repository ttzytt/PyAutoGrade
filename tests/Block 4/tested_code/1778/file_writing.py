

'''
Creates a file and prints a diamond pattern of a specified width.
For example, if the specified width is 5:    x
                                            xxx
                                           xxxxx
                                            xxx
                                             x
                                            
    inputs:
        out_file_name    The file that it will print out to.
        width            The width of the diamond.
'''
def write_diamond_pattern(out_file_name, width):
    with open(out_file_name, 'w') as out_file:
        
        counter = 1

        
        while counter < width:

            
            out_file.write(' ' * int(((width - counter)/2)) + 'x' * counter + '\n')
            
            counter += 2

        
        while counter >= 1:
            out_file.write(' ' * int(((width - counter)/2)) + 'x' * counter + '\n')
            counter -= 2
            

'''
Looks at a file of names(first name first), and puts it in form last-name, first-name
                                            
    inputs:
        out_file_name    The file that it will print out to.
        in_file_name     The file that contains the names
'''
def last_name_first(in_file, out_file):


    with (open(in_file, 'r') as in_file,
            open(out_file, 'w') as out_file):
        
        
        for line in in_file:
            names = line.split()

            
            
            out_file.write(names[-1] + ', ' + names[0] + '\n')


'''
Looks at a file of addition problems, and prints out a file with each problem and its
respective solution
                                            
    inputs:
        out_file_name    The file that it will print out to.
        in_file_name     The file that contains the additon problems.
'''        
def add_and_write(in_file, out_file):

    with (open(in_file, 'r') as in_file,
        open(out_file, 'w') as out_file):

        
        for line in in_file:

            
            
            numbers = line.split()
            first_number = numbers[0]
            second_number = numbers[2]

            
            result = int(first_number) + int(second_number)

            
            out_file.write(first_number + ' + ' + second_number + ' = ' + str(result) + '\n')
        
            

'''
Goes through a file and cuts off any line with more than 20 characters at the 15th character.
The words 'blah blah blah' are added at the end
                                            
    inputs:
        out_file_name    The file that it will print out to.
        in_file_name     The file that will be read.
''' 
def blah_blah_blah(in_file_name, out_file_name):

    with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):

        
        for line in in_file:
            if len(line) > 20:
                
                
                out_file.write(line[:15] + 'blah blah blah' + '\n')
                                        
            else:
                out_file.write(line)
                                    

def main():
    write_diamond_pattern('Text files/diamond.txt',7)
    last_name_first('Text files/names.txt', 'Text files/last_name_first.txt')
    add_and_write('Text files/addition.txt', 'Text files/result.txt' )
    blah_blah_blah('Text files/greeneggs.txt', 'Text files/blahblahblah.txt')

if __name__ == "__main__":
    main()

