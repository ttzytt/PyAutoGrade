'''
Written by Alex
TASK 15-18
'''


import random
random.seed()

'''----------------------FUNCTIONS------------------------'''



def comments_for_functions(in_file, out_file):
    
    list_of_lines = in_file.readlines()
    
    n = 0
    while n < len(list_of_lines):
        
        if list_of_lines[n][:4] == 'def ':
            
            if (list_of_lines[n-1][0] != '#' and
                list_of_lines[n-1][0] != "'''" and
                list_of_lines[n-1][0] != '"""'):
                
                
                reminder = '#R(auto): Add a comment that says what this function does!\n'
                list_of_lines.insert(n,reminder)
                
    

        n += 1

    '''            
    new_string = ''
    for i in range(len(list_of_lines)):
        new_string += str(list_of_lines[i])
    return new_string
    '''
    new_file = ''.join(list_of_lines)
    return new_file




def blank_lines_around_functions(in_file, out_file):
    
    list_of_lines = in_file.readlines()
    n = 0

    while n < len(list_of_lines):
        
        if list_of_lines[n][:4] == 'def ': 

            if list_of_lines[n-1][0] != '#': 
                
                if len(list_of_lines[n-1].split()) != 0: 
                
                    blank = '#R(auto): Add a blank line here!\n'
                    list_of_lines.insert(n,blank)
                    n += 1

            else: 

                if len(list_of_lines[n-1].split()) != 0: 

                    blank = '#R(auto): Add a blank line here!\n'
                    list_of_lines.insert(n-1,blank)
                    n += 1

        elif ('return' in list_of_lines[n]) and ('#return' not in list_of_lines[n]): 

            if len(list_of_lines[n+1].split()) != 0: 
                
                blank = '#R(auto): Add a blank line here!\n'
                list_of_lines.insert(n+1,blank)

        n += 1
        
    new_file = ''.join(list_of_lines)

    return new_file




def break_up_long_lines(in_file, out_file):

    mul_lines = in_file.readlines() 
    n = 0    
    while n < len(mul_lines): 

        sin_line = mul_lines[n] 
        

        if len(sin_line) > 79: 
            breaking = '#R(auto): This line is too long. Break it up!\n'
            mul_lines.insert(n, breaking)

        n += 2

        

    new_strings = ''.join(mul_lines)

    return new_strings
    
    




def spaces_after_commas(in_file, out_file):

    mul_lines = in_file.readlines()
    n = 0

    while n < len(mul_lines):

        sin_line = mul_lines[n]

        l = 0
        while l < len(sin_line)-1:

            if sin_line[l] == ',' and sin_line[l+1] != ' ':
                sin_line = sin_line[:l+1] + ' ' + sin_line[l+1:]
                
                mul_lines.insert(n+1, '#R space added\n')

            l += 1
        n += 1

    new_strings = ''.join(mul_lines)
    return new_strings





'''------------------------TESTS-------------------------'''

def main():
    
    
    print('T15 finished')
    input_file = 'file_writing.py'
    output_file = 'Unit 3 Test/T15.py'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        comments = comments_for_functions(my_file1, my_file2)
        my_file2.write(str(comments))
    print()
        
    
    print('T16 finished')
    input_file = 'file_writing.py'
    output_file = 'Unit 3 Test/T16.py'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        blanks = blank_lines_around_functions(my_file1, my_file2)
        my_file2.write(str(blanks))
    print()

    
    print('T17 finished')
    input_file = 'file_writing.py'
    output_file = 'Unit 3 Test/T17.py'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        break_line = break_up_long_lines(my_file1, my_file2)
        my_file2.write(str(break_line))
    print()

    
    print('T18 finished')
    input_file = 'scratch.py'
    output_file = 'Unit 3 Test/T18.py'
    with (open(input_file, 'r') as my_file1,
          open(output_file, 'w') as my_file2):
        space_comma = spaces_after_commas(my_file1, my_file2)
        my_file2.write(str(space_comma))
    print()

    
if __name__ == '__main__':
    main()

