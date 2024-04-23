






'''
T11
Writes a diamond pattern in a file with given widths to draw the diamond
out_file - A text file. Doesn't matter if there is pre-existing text
width - max width of the diamond

A width = 3 diamond would look like
 x
xxx
 x
Keep in mind you need to manually set the width
    inputs:
        width The width of the diamond
    outputs:
        out_file A file that will be modified
'''

def write_diamond_pattern(out_file, width):
    width = 5
    # Determines the rows(doesnt give like 3.0, it will give 3)
    rows = (width + 1) // 2
    # Prints upper part of diamond
    for top_rows in range(1, rows + 1):
        space = ' ' * (rows - top_rows)
        diamond = 'x' * (2 * top_rows - 1)
        out_file.write(space + diamond + '\n')
    # Prints the lower part of the diamond
    for bottom_row in range(rows - 1, 0, -1):
        # Calculates the spaces and diamond count for each row depending on the width
        space = ' ' * (rows - bottom_row)
        diamond = 'x' * (2 * bottom_row - 1)
        out_file.write(space + diamond + '\n')
    

    

'''
T12
Instead of writing first name, space and last name, this function will print the last name
a coma, a space and first name.
    inputs:
        in_file  A file that is open for reading
    outputs:
        out_file A file that will be the result 
'''

def last_name_first(in_file, out_file):
    new_name = []
    for line in in_file:
        words = line.split()
        new_name = (words[1] + ', ' + words[0] +'\n')
        out_file.write(new_name)


'''
T13
Takes in a expression and will find the result of it
    inputs:
        in_file  A file that is open for reading
    outputs:
        out_file A file that will be the result 
'''
def add_and_write(in_file, out_file):
    for line in in_file:
        if line[-1] == '\n':
            line = line[:-1]
        expression = line.split('+')
        first_num = int(expression[0])
        second_num = int(expression[1])
        result = first_num + second_num
        out_file.write(line + ' = ' + str(result) + '\n')
        
              

'''
T14
When a line gets longer than 20 characters, it will replace everything after the 15th
character with the string 'blah blah blah'
    inputs:
        in_file_name name of the file that is being input
    outputs:
        out_file_name name of the file that is being output
'''

def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file_name:
        # Checks for the line length
        if len(line) > 20:
            new_line = (str(line[:15]) + ', blah blah blah' + "\n")
        else:
            new_line = line
    out_file_name.write(new_line)
                    
    

        
def main():
    
    my_file_name = "Text files/diamond.txt"
    with open(my_file_name, "w") as read_file:
        write_diamond_pattern(read_file, 5)

            
    in_file_name = "Text files/names.txt"
    out_file_name = "Text files/names_reversed.txt"
    with (open(in_file_name, "r") as file_in,
            open(out_file_name, "w") as file_out):
        last_name_first(file_in, file_out)
        
    in_file_name = "Text files/addition.txt"
    out_file_name = "Text files/addition_answers.txt"
    with (open(in_file_name, "r") as file_in,
            open(out_file_name, "w") as file_out):
        add_and_write(file_in, file_out)


    in_file_name = "Text files/test file.txt"
    out_file_name = "Text files/test file output.txt"

    with (open(in_file_name, "r") as file_in,
            open(out_file_name, "w") as file_out):
        (blah_blah_blah(file_in, file_out))

        
if __name__ == "__main__":
    main()
