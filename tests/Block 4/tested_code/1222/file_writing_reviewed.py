



import random
random.seed()


'''
Prints a "diamond" of x's with the given width
    inputs:
        out_file  (a file open for writing)
        width     (Positive odd integer that determines width of diamond)
'''
def write_diamond_pattern(out_file, width):
    rows = (width + 1) // 2
    for top_rows in range(1, rows + 1):
        space = ' ' * (rows - top_rows)
        diamond = 'x' * (2 * top_rows - 1)
        out_file.write(space + diamond + '\n')
    for bottom_row in range(rows - 1, 0, -1):
        space = ' ' * (rows - bottom_row)
        diamond = 'x' * (2 * bottom_row - 1)
        out_file.write(space + diamond + '\n')

'''
Rewrites names with last names first and first names second
    inputs:
        in_file  (a file open for reading)
        out_file (a file open for writing)
'''

def last_name_first(in_file, out_file):
    temp_name = []
    for line in in_file:
        words = line.split() # Splits the line up into seperate words
        temp_name = (words[1] + ', ' + words[0] + '\n') # Reverses the order of the name
        out_file.write(temp_name)

'''
Writes to a file the solution of a math problem
The new file should include both the problem and solution
    inputs:
        in_file  (a file open for reading)
        out_file (a file open for writing)    
'''
def add_and_write(in_file, out_file):
    full_problems = []
    for line in in_file:
        problem = str(line) # Finds the problem as a string
        split = problem.split() # Splits the problem up into multiple pieces
        solution = int(split[0]) + int(split[2]) # Adds the two numbers
        full_problems = (str(split[0]) + ' + ' + str(split[2])
                         + ' = ' + str(solution) + '\n') # Prints the problem and solution
        out_file.write(full_problems)

'''
Replaces everything past 15 characters in a line with 'blah blah blah'
Only if the line is longer than 20 characters
    inputs:
        in_file_name  (a file open for reading)
        out_file_name (a file open for writing)    
'''

def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file_name:
        if len(line) > 20:
            new_line = (str(line[:15]) + ', blah blah blah' + "\n")
        else:
            new_line = line
    out_file_name.write(new_line)

# ------------------------------------Open & Run--------------------------------------------
def main():
    # T11
    out_file_name = 'Text Files/file_writing_tests.txt'
    with open(out_file_name, 'w') as out_file:
        width = 10
        draw_a_diamond =  write_diamond_pattern(out_file, width)

    # T12
    in_file_name = 'Text Files/names.txt'
    out_file_name = 'Text Files/file_writing_tests.txt'
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        reorganize_name = last_name_first(in_file, out_file)


    # T13
    in_file_name = 'Text Files/addition.txt'
    out_file_name = 'Text Files/file_writing_tests.txt'
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        solution_to_problem = add_and_write(in_file, out_file)

    
    in_file_name = "Text files/some_tests.txt"
    out_file_name = "Text files/test output.txt"
    with (open(in_file_name, "r") as file_in,
            open(out_file_name, "w") as file_out):
        (blah_blah_blah(file_in, file_out))

if __name__ == "__main__":
    main()
