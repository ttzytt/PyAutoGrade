







def write_diamond_pattern(out_file, width):
    num_x = 1
    while num_x < width:
        out_file.write(' ' * ((width - num_x) // 2) + 'x' * num_x + '\n')
        num_x = num_x + 2
    out_file.write('x' * width + '\n')
    while num_x <= width and num_x > 0:
        num_x = num_x - 2
        out_file.write(' ' * ((width - num_x) // 2) + 'x' * num_x + '\n')



def last_name_first(in_file, out_file):
    for line in in_file:
        words = line.split()
        first_name = words[0]
        last_name = words[1]
        out_file.write(last_name + ', ' + first_name + '\n')



def add_and_write(in_file, out_file):
    for line in in_file:
        words = line.split()
        answer = int(words[0]) + int(words[2])
        
        if line[-1] == '\n':
            line = line[:-1]
        out_file.write(line + ' = ' + str(answer) + '\n')




def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file:
        if len(line) > 20:
            out_file.write(line[:15] + ', blah blah blah')




def main():
 
    file_name = 'Text files/diamond.txt'
    with open(file_name, 'w') as my_file:  
        write_diamond_pattern(my_file, 11)

    in_file_name = 'Text files/names.txt'
    out_file_name = 'Text files/last_name_first_name.txt'

    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        last_name_first(in_file, out_file)

    in_file_name = 'Text files/addition.txt'
    out_file_name = 'Text files/addition_sum.txt'

    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        add_and_write(in_file, out_file)

if __name__ == "__main__":
    main()

