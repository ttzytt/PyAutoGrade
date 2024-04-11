



'''
Write a 'diamond' of x's with the given width.
inputs:
    out_file   A file open for writing
    width      A positive odd integer indicating the width of the diamond
'''
def write_diamond_pattern(out_file, width):
    diamond_count = 1 # Tracks the number of X's I have in each row
    while diamond_count < width: 
        spaces = int((width - diamond_count)/2) 
        out_file.write(' ' * spaces + 'x' * diamond_count + '\n')
        diamond_count += 2 
    while diamond_count <= width and diamond_count > 0: 
        spaces = int((width - diamond_count)/2)
        out_file.write(' ' * spaces + 'x' * diamond_count + '\n')
        diamond_count -= 2 

'''
Writes names that contain a first and last name seperated by a space as a last name first and comma in between.
inputs:
    in_file   A file open for reading
    out_file  A file open for writing
'''
def last_name_first(in_file, out_file):
    for line in in_file: 
        name = []
        words = line.split() 
        for word in words: 
            name.append(word)
        if len(name) > 2:
            out_file.write(name[2] + ', ' + name[0] + '\n')
        else:
            out_file.write(name[1] + ', ' + name[0] + '\n')
            
'''
Writes the equation and answer to that addition porblem
inputs:
    in_file  A file open for reading
    out_file A file open for writing
'''    
def add_and_write(in_file, out_file):
    for line in in_file:
        
        equation = str(line[:-1]) 
        numbers = [] 
        words = line.split()
        for word in words:
            numbers.append(word)
        sum_of_line = int(numbers[0]) + int(numbers[2])
        out_file.write(equation + ' = ' + str(sum_of_line))

'''
Writes 'blah blah blah' if a line in the file is longer than 20 characters replace it with just first 15 characters
followed by the string', blah blah blah'.
inputs:
    in_file_name  A file name to open for reading
    out_file_name A file name to open for writing           
'''
def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
      open(out_file_name, 'w') as out_file): 
        list_of_lines = in_file.readlines() 
        for i in range(len(list_of_lines)): 
            if len(list_of_lines[i]) > 20: 
                
                list_of_lines[i] = list_of_lines[i][:15] + ', blah blah blah \n' 
            out_file.write(list_of_lines[i])
        
    








file_name = 'Text files/diamond_pattern.txt'
with open(file_name, 'w') as my_file:
    write_diamond_pattern(my_file, 3)


in_file_name = 'Text files/names.txt'
out_file_name = 'Text files/last_names_first.txt'
with (open(in_file_name, 'r') as in_file,
      open(out_file_name, 'w') as out_file):
    last_name_first(in_file, out_file)


in_file_name = 'Text files/addition.txt'
out_file_name = 'Text files/add_and_write.txt'
with (open(in_file_name, 'r') as in_file,
      open(out_file_name, 'w') as out_file):
    add_and_write(in_file, out_file)


blah_blah_blah('Text files/greeneggs.txt', 'Text files/blah_greeneggs.txt')
    
