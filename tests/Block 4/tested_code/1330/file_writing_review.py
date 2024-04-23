









'''
Returns a “diamond” of x’s with the given width in the out_file. 
    inputs:
        out_file    A file that will print diamond in it.
        width    the width of diamond.
'''

def write_diamond_pattern(out_file, width):
    diamond = ""
    for i in range(width):
        row = ""
        for j in range(width):
            if abs(width // 2 - i) + abs(width // 2 - j) <= width // 2:
                row += 'x'
            else:
                row += ' '
        diamond += row + '\n'
    return diamond


'''
    rows = []
    total = []
    for i in range(width):
        rows.append(' ')
    for i in range(width):
        total.append(rows)
    #print(total)
    x_numbers = 1
    while x_numbers <= width:
        total[0][2] = 'x'
        print(total)
        # print x
        row = int((x_numbers+1)/2 - 1)
        print('row = ' + str(row))
        x_min_place = int((width - x_numbers)/2)
        print('x_min = ' + str(x_min_place))
        #print (x_place)
        x_place = int((width - x_numbers)/2)
        x_max_place = int(width-x_min_place)
        while x_place < x_max_place:
            print('x_place = ' + str(x_place))
            print(row)
            #print(total[1])
            total[row][x_place] = 'x'
            x_place += 1
            print(total)
        x_numbers += 2
        x_place += 1

out_file = 'Text files/blank.txt'
width = 5


with open(out_file, 'w') as my_file:  # Open for writing. 
my_file.write(lists + '\n')
'''


'''
Returns a “diamond” of x’s with the given width in the out_file. 
    inputs:
        out_file    A file that will rewrite names in it.
        in_file    A file gives you a list of names. 
'''

def last_name_first(in_file, out_file):
    name_list = ""
    with open(in_file, 'r') as f_in:
        for line in f_in:
            names = line.strip().split()
            if len(names) != 2: 
                print(f"'{line.strip()}'does not contain exactly two names.")
                continue 
            first_name, last_name = names 
            name = f"{last_name}, {first_name}\n"
            name_list += name
    with open(out_file, 'w') as f_out:
        f_out.write(name_list)





'''
Returns the results of an addition
    inputs:
        in_file    A file that will give you problems
        out_file    A file gives you the answer of problems

'''

def add_and_write(in_file, out_file):
    with open(in_file, 'r') as f:
        problems = f.readlines()
    with open(out_file, 'w') as f:
        for problem in problems:
            num1, operator, num2 = problem.split()
            num1 = int(num1)
            num2 = int(num2)
            result = num1 + num2
            f.write(f"{num1} {operator} {num2} = {result}\n")
    



'''
Returns the file with blah blah blah
    inputs:
        in_file_name    A file that will give you many texts
        out_file_name    A file gives you texts with blah
'''

def blah_blah_blah(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        lines = in_file.readlines()
    with open(out_file_name, 'w') as out_file:
        for line in lines:
            if len(line) > 20:
                new_line = line[:15] + ', blah blah blah\n'
                out_file.write(new_line)
            else:
                out_file.write(line)
            



def main():
    
    

    
    print('T11 begins:')
    out_file = 'Text files/blank.txt'
    width = 5

    resulting_diamond = write_diamond_pattern(out_file, width)
    with open(out_file, 'w') as my_file:  
        my_file.write(resulting_diamond)
    print()

    
    print('T12 begins:')
    in_file = 'Text files/names.txt'
    out_file = 'Text files/out_file_name.txt'
    last_name_first(in_file, out_file)
    print()

    
    print('T13 begins:')
    input_file = 'Text files/addition.txt'
    output_file = 'Text files/answers.txt'
    add_and_write(input_file, output_file)
    print()

    
    print('T14 begins:')
    in_file_name = 'Text files/greeneggs.txt'
    out_file_name = 'Text files/shrinked_paragraph.txt'
    blah_blah_blah(in_file_name, out_file_name)


if __name__ == "__main__":
    main()






        


