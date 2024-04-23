





"""
T11 Function prints a "diamond" of x's with the given width.
ex. width = 5
  x
 xxx
xxxxx
 xxx
  x
    inputs:
        out_file                    A file that is open to write in
        width                       a positive, odd integer determining the max number of x's
                                    in the diamond
"""
def write_diamond_pattern(out_file, width):
    diamond_pattern = '' 
    spaces = (width - 1) / 2 
    x_count = 1 
    
    while spaces > 0 and x_count < width: 
        diamond_pattern = diamond_pattern + ' ' * int(spaces) + 'x' * int(x_count) + '\n'
        spaces -= 1
        x_count += 2
        
    diamond_pattern = diamond_pattern + 'x' * width + '\n' 
    spaces = 1
    x_count = width - 2
    
    while spaces < width and x_count > 0: 
        diamond_pattern = diamond_pattern + ' ' * int(spaces) + 'x' * int(x_count) + '\n'
        spaces += 1
        x_count -= 2
        
    return diamond_pattern

"""
T12 Function takes a name written in the form First Last (ex. James Bond) and rewrites it in
the form Last, First (ex. Bond, James)
    inputs:
            out_file                    A file that is open to write in
            in_file                     A file that is open for reading  
"""
def last_name_first(in_file, out_file):
    for line in in_file: 
        
        words = line.split() 
        formatted_name = words[1] + ', ' + words[0] 
        out_file.write(formatted_name + '\n') 


"""
T13 Function with an input file in which each line contains an addition problem (ex. 2 + 3)
and writes in a new file the problem along with the answer, (ex. 2 + 3 = 5)
    inputs:
            out_file                A file that is open to write in
            in_file                 A file that is open for reading
"""
def add_and_write(in_file, out_file):
    for line in in_file: 
        
        reactants = line.split('+') 
        products = int(reactants[0]) + int(reactants[1]) 
        
        out_file.write(line.strip() + ' = ' + str(products) + '\n') 


"""
T14 Function with an input file that contains a lot of text. Any line which has more than 20
characters is replaced with the first 15 characters followed by the string ', blah blah blah'.
If the line has less than 20 characters, it is left the same
    inputs:
            out_file_name                The name of a file that is open to write in
            in_file_name                 The name of a file that is open for reading
"""
def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file_name: 
        
                if len(line) > 20: 
                    
                    modified_line = line[:15] + ', blah blah blah' + '\n' 
                    out_file_name.write(modified_line)
                    
                else: 
                    out_file_name.write(line)


"""
Runs every function and writes the results in different text files
"""

def main():

    
    out_file_wdp = 'Text files/diamond_writing_practice.txt' 
    with open(out_file_wdp, 'w') as out_file:
        out_file.write(write_diamond_pattern(out_file, 7))


    
    out_file_nfwp = 'Text files/name_format_writing_practice.txt'
    in_file_lnf = 'Text files/names.txt'

    with open(in_file_lnf, 'r') as in_file, open(out_file_nfwp, 'w') as out_file:
        last_name_first(in_file, out_file)


    
    out_file_awp = 'Text files/addition_writing_practice.txt'
    in_file_aaw = 'Text files/addition.txt'
    
    with open(in_file_aaw, 'r') as in_file, open(out_file_awp, 'w') as out_file:
        add_and_write(in_file, out_file)


    
    out_file_name_bbb = 'Text files/blah_blah_blah_practice.txt'
    in_file_name_bbb =  'Text files/greeneggs.txt'

    with open(in_file_name_bbb, 'r') as in_file_name, open(out_file_name_bbb, 'w') as out_file_name:
        blah_blah_blah(in_file_name, out_file_name)


        
if __name__ == "__main__":
    main()









