



import random
random.seed()



'''
T11
Suppose out_file is a file open for writing and width is a positive odd integer. This function
should print a “diamond” of x’s with the given width.

    inputs:
        read_file    A file that is open for reading.
'''

def write_diamond_pattern(out_file, width):

    diamond = ''
    line_space = int((width - 1) / 2) 
    num_x = 1 

    
    for i in range(int((width - 1) / 2)): 
        diamond += line_space * ' ' + num_x * 'x' + '\n'
        line_space -= 1
        num_x += 2

    diamond += num_x * 'x' 

    for j in range(int((width - 1) / 2)): 
        line_space += 1
        num_x -= 2
        diamond += '\n' + line_space * ' ' + num_x * 'x'


    return(str(diamond))




































def main():

    out_file = 'Text files/diamond.txt'

    with open(out_file, 'w') as my_file:  
        width = int(input('How wide would you like the diamond to be (positive odd integer)?: '))
        write_diamond = write_diamond_pattern(out_file, width)
        
        my_file.writelines(write_diamond)  
    















if __name__ == "__main__":
    main()
