





def write_diamond_pattern(out_file, width):
    width = 5
    # Determines the rows
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
    

    



def last_name_first(in_file, out_file):
    new_name = []
    for line in in_file:
        words = line.split()
        new_name = (words[1] + ', ' + words[0] +'\n')
        out_file.write(new_name)



def add_and_write(in_file, out_file):
    for line in in_file:
        expression = line.split('+')
        addition_list = []
        for adding in expression:
            addition_list.append(int(adding))
        result = sum(addition_list)
        out_file.write(str(expression[0]) + '+' + str(expression[1]) + ' = ' + str(result) + '\n')
        
              



def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file_name:
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
