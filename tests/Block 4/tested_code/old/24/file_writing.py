




def write_diamond_pattern(out_file, width):
    for i in range(width):
        for j in range(int((width + 1)/2) - i):
            out_file.write(' ')
        for j in range(2*i - 1):
            out_file.write('x')
        out_file.write('\n')
        
    for i in range(width, 1, -1): 
        for j in range(int((width + 1)/2) - i):
            out_file.write(' ')
        for j in range(2*i - 1):
            out_file.write('x')
        out_file.write('\n')





def last_name_first(in_file, out_file):
    print('h')





def add_and_write(in_file, out_file):
    print('h')

    
    


      
file_name = 'Text files/writingtestsfile.txt'
with open(file_name, 'w') as my_file:
    write_diamond_pattern(my_file, 3)
    
