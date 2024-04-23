


'''
Writes a diamond pattern of 'x' characters with specific width.

    inputs:
        out_file   a file open for writing
        width   a positive odd integer representing the width of the diamond
'''
def write_diamond_pattern(out_file, width):

    half_width = width // 2
    
    for i in range(half_width + 1):
        spaces = " " * (half_width - i)
        diamonds = "x" * (2 * i + 1)
        out_file.write(spaces + diamonds + spaces + "\n")
        
    for i in range(half_width - 1, -1, -1):
        spaces = " " * (half_width - i)
        diamonds = "x" * (2 * i + 1)
        out_file.write(spaces + diamonds + spaces + "\n")


'''
Reads names from in_file,
swaps the first and last names,
writes them to out_file.
'''
def last_name_first(in_file, out_file):

    for line in in_file:
        first_name, last_name = line.split()
        out_file.write(last_name + ", " + first_name + "\n")


'''
Reads addition problems from in_file,
calculates the answers,
writes them to out_file.
'''
def add_and_write(in_file, out_file):
    
    for line in in_file:
        num_1, num_2 = line.split("+")
        num_1 = int(num_1)
        num_2 = int(num_2)
        result = num_1 + num_2
        out_file.write(line + " = " + str(result) + "\n")


'''
Reads addition problems from in_file,
calculates the answers,
writes them to out_file.
'''
def blah_blah_blah(in_file, out_file):

    for line in in_file:
        if len(line) > 20:
            out_file.write(line[ :15] + ", blah blah blah\n")
        else:
            out_file.write(line)


width = int(input('How wide do you want the diamond to be? '))
out_file = 'Text files/Diamonds!.txt'

with open('Text files/Diamonds!.txt', 'w') as my_file:
    write_diamond_pattern(out_file, width)

    

    
