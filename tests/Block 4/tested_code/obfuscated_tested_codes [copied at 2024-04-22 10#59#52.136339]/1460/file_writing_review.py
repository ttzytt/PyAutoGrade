








def write_diamond_pattern(out_file, width):
    if width % 2 == 0:
        raise(ValueError, "width cannot be an even integer.")
    
    list_of_lines = []
    for i in range(1, width + 1, 2):
        space_buffer = int((width - i)/2) * ' '
        line = space_buffer + (i * '*') + '\n'
        list_of_lines.append(line)
    for i in range(width - 2, 0, -2):
        space_buffer = int((width - i)/2) * ' '
        line = space_buffer + (i * '*') + '\n'
        list_of_lines.append(line)
    out_file.writelines(list_of_lines)






def last_name_first(in_file, out_file):
    names = in_file.read().splitlines()
    list_of_lines = []
    for name in names:
        name_parts = name.split(' ')
        list_of_lines.append(name_parts[-1] + ', ' + name_parts[0] + '\n')
    out_file.writelines(list_of_lines)






def add_and_write(in_file, out_file):
    equations = in_file.read().splitlines()
    list_of_lines = []
    for equation in equations:
        
        equation_parts = equation.split("+")
        equation_sum = 0
        for part in equation_parts:
            equation_sum += int(part)

        
        list_of_lines.append(equation + " = " + str(equation_sum) + "\n")
    out_file.writelines(list_of_lines)







def blah_blah_blah(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        in_file_content = in_file.read()
    list_of_lines = []
    for line in in_file_content.splitlines():
        if len(line) > 20:
            list_of_lines.append(line[:15] + ", blah blah blah\n")
        else:
            
            list_of_lines.append(line)

    with open(out_file_name, 'w') as out_file:
        out_file.writelines(list_of_lines)



def main():
    with (open("Text files/twinkletwinklelittlestar.py", 'w') as out_file):
        write_diamond_pattern(out_file, 71)
        print("Diamond pattern written to twinkletwinklelittlestar.py")
    with (open('Text files/names.txt', 'r') as in_file, open("Text files/COOLER_NAMES.py", 'w') as out_file):
        last_name_first(in_file, out_file)
        print("Last name first written to COOLER_NAMES.py")
    with (open('Text files/addition.txt', 'r') as in_file, open("Text files/adittionED.py", 'w') as out_file):
        add_and_write(in_file, out_file)
        print("Add and write to adittionED.py")
    blah_blah_blah('Text files/greeneggs.txt', "Text files/blahs.py")
    print('Blah blah blahed greeneggs to blahs.py')

if __name__ == "__main__":
    main()


    
