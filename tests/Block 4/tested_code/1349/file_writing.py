





import random
random.seed()


'''
Writes a file containing a diamond pattern with a given width.
    inputs:
        out_file    A file address
        width       An integer containing the width of diamond
'''
def write_diamond_pattern(out_file, width):
    for i in range(width):
        
        num_x = width - abs((width-1)/2 - i)*2
        
        num_space = (width - num_x) / 2
        
        line = " " * int(num_space) + "x" * int(num_x) + "\n"
        out_file.write(line)

'''
Writes a file having each name last name first.
    inputs:
        in_file    A file that is open for reading.
        out_file   A file address
'''
def last_name_first(in_file, out_file):
    for line in in_file:
        name = line.split()
        
        new_line = name[1] + ", " + name[0] + "\n"
        out_file.write(new_line)

'''
Writes a file containing the poblems and answers of adding problems.
    inputs:
        in_file    A file that is open for reading.
        out_file   A file address
'''
def add_and_write(in_file, out_file):
    for line in in_file:
        question = line.split()
        answer = int(question[0]) + int(question[2]) 
        
        new_line = line[:-1] + " = " + str(answer) + "\n"
        out_file.write(new_line)

'''
Writes a file replacing any long lines of over 20 characters
into first 15 characters, followed by the string ', blah blah blah'.
    inputs:
        in_file_name    In file address
        out_file_name   Out file address
'''
def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        for line in in_file:
            if len(line) > 20:
                
                out_file.write(line[:15] + ", blah blah blah\n")
            else:
                out_file.write(line)


def main():
    in_file_name = 'Text files/addition.txt'
    out_file_name = 'Text files/written_files.txt'

    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        add_and_write(in_file, out_file)

if __name__ == "__main__":
    main()

