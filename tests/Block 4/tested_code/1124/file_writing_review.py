










def write_diamond_pattern(out_file, width):
    
    num_x = 1
    changing_width = width

    
    while changing_width//2 >= 0:
        
        num_spaces = changing_width//2
        
        out_file.write(' ' * num_spaces + 'X' * num_x + ' ' * num_spaces) 
        
        out_file.write("\n") 
        changing_width -= 2
        num_x += 2

    
    num_x -= 4
    changing_width += 4

    
    while changing_width//2 <= width//2:
        num_spaces = changing_width//2
        out_file.write(' ' * num_spaces + 'X' * num_x + ' ' * num_spaces)
        out_file.write("\n") 
        
        
        
        changing_width += 2
        num_x -= 2







def last_name_first(in_file, out_file):
    
    for line in in_file:
        list_line = line.split()
        out_file.write(list_line[1] + ', ' + list_line[0] + "\n")

        




def add_and_write(in_file, out_file):
    solved_equation = 0
    
    for line in in_file:
        equation = line.split()
        
        solved_equation = int(equation[0]) + int(equation[2])
        
        out_file.write(line[:-1] + ' = ' + str(solved_equation))
        out_file.write("\n") 







def blah_blah_blah(in_file_name, out_file_name):
    
    with open(out_file_name, 'w') as out_file, open(in_file_name, 'r') as in_file:
        
        for line in in_file:
            
            if len(line) - 1 > 20:
                out_file.write(line[:16] + ', blah blah blah')
                out_file.write("\n")
            
            else:
                out_file.write(line)


file_name = 'Text files/out_file_diamond.txt'
with open(file_name, 'w') as my_file:
    write_diamond_pattern(my_file, 101)

out_file_name = 'Text files/out_file_last_name_first.txt'
in_file_name = 'Text files/names.txt'
with open(out_file_name, 'w') as out_file, open(in_file_name, 'r') as in_file:
    last_name_first(in_file, out_file)

out_file_name = 'Text files/out_file_addition.txt'
in_file_name = 'Text files/addition.txt'
with open(out_file_name, 'w') as out_file, open(in_file_name, 'r') as in_file:
    add_and_write(in_file, out_file)

blah_blah_blah('Text files/greeneggs.txt', 'Text files/out_file_blah.txt')
