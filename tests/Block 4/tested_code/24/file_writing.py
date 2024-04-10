



import random
random.seed()



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



def last_name_first(in_file, out_file):
    temp_name = []
    for line in in_file:
        words = line.split() # Splits the line up into seperate words
        temp_name = (words[1] + ', ' + words[0] + '\n') # Reverses the order of the name
        out_file.write(temp_name)


def add_and_write(in_file, out_file):
    full_problems = []
    for line in in_file:
        problem = str(line) # Finds the problem as a string
        split = problem.split() # Splits the problem up into multiple pieces
        solution = int(split[0]) + int(split[2]) # Adds the two numbers
        full_problems = (str(split[0]) + ' + ' + str(split[2])
                         + ' = ' + str(solution) + '\n') # Prints the problem and solution
        out_file.write(full_problems)



def blah_blah_blah(in_file_name, out_file_name):
    line_len_list = []
    for line in in_file_name:
        list_of_lines = in_file_name.readlines()
        for i in range(len(list_of_lines)):
            line_len = len(list_of_lines[i])
            line_len_list.append(line_len)
            for j in range(len(line_len_list)):
                if int(line_len_list[j]) > 20:
                    list_of_lines[j] = (str(list_of_lines[j][:15]) + ', blah blah blah' + "\n")

                out_file_name.write(list_of_lines[j])

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

    # T14
    in_file_name = 'Text Files/greeneggs.txt'
    out_file_name = 'Text Files/file_writing_tests.txt'
    blah_blah_blah(in_file_name, out_file_name)

if __name__ == "__main__":
    main()
