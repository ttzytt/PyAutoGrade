






        
        
def write_diamond_pattern(out_file_name, width):
    with open(out_file_name, 'w') as out_file:
        space = (width - 1) // 2
        for i in range(1, width + 1, 2):
            line = ' ' * space + 'x' * i + '\n'
            out_file.write(line)
            space -= 1
        space = 1
        
        for i in range(width - 2, 0, -2):
            line = ' ' * space + 'x' * i + '\n'
            out_file.write(line)
            space += 1


'''
T12: Reverse first and last names in a file
    Inputs:
           in_file    file that is open for reading
           out_file   A file that is open for printing
            
'''
def last_name_first(in_file, out_file):
    for line in in_file:
        words = line.split()
        for_name = words[1] + "," + words[0]
        out_file.write(for_name + "\n")
'''
#R Function doesnt work
for_name = words[1] + "," + words[0]
IndexError: list index out of range

'''





def add_and_write(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    
        for line in in_file:
            parts = line.strip().split(" + ") 
            total = sum(int(part) for part in parts)
            out_file.write(line.strip() + " = " + str(total) + '\n')




def blah_blah_blah(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    
        for line in in_file:
            if len(line) > 20:
                out_file.write(line[:15] + ', blah blah blah\n')
            else:
                out_file.write(line)




def main():

 if __name__ == "__main__":
    
    write_diamond_pattern('Text files/diamond.txt', 5)
    
    last_name_first('Text files/names.txt', 'Text files/last_name_first.txt')
    
    add_and_write('Text files/addition.txt', 'Text files/addition_solved.txt')
    
    blah_blah_blah('Text files/long_lines.txt', 'Text files/shortened_lines.txt')
