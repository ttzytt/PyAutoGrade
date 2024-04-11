def write_diamond_pattern(width):
    with (open(out_file_name, 'w') as out_file):
        space = (width - 1) // 2
    for i in range(1, width + 1, 2):
        first_half = (' ' * space + 'x' * i)
        space -= 1

    space = 1   
    for i in range(width - 1, 0, -2):
        second_half = print(' ' * space + 'x' * (i - 1) )
        width -= 1
        space += 1
    out_fine.write_diamond(first_half + "n/" + second_half)



def last_name_first(in_file, out_file):
    in_file_name = 'Text files/names.txt'
    out_file_name = 'Text files/last_name_first.txt'
    with open(in_file, 'r') as input_file,open(out_file, 'w') as output_file:
        for line in input_file:
            first_name, last_name = line.strip().split()  
            reversed_name = f"{last_name}, {first_name}"  
            output_file.write(reversed_name + '\n')  



