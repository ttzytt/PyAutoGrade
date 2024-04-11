



import random
out_file_name = 'Text files/my_cool_file.txt'

file_name = 'Text files/in_file.txt'





def write_diamond_pattern(out_file, width):
    a = 1 
    
    while a <= width:
        out_file.write('\n')
        spaces_a = int((width - a)/2)
        for i in range(spaces_a):
            out_file.write(' ')
        for i in range(a):
            out_file.write('x')
        for i in range(spaces_a):
            out_file.write(' ')
        a += 2
    
    b = width - 2
    while b >= 1:
        out_file.write('\n')
        spaces_b = int((width - b)/2)
        for i in range(spaces_b):
            out_file.write(' ')
        for i in range(b):
            out_file.write('x')
        for i in range(spaces_b):
            out_file.write(' ')
        b -= 2
          





in_file_name_1 = 'Text files/names.txt'


def last_name_first(in_file, out_file):
    for line in in_file:
        names = line.split()
        out_file.write(names[1] + ', ' + names[0] + '\n')






in_file_name_2 = 'Text files/addition.txt'


def add_and_write(in_file, out_file):
    for line in in_file:
        numbers = line.split()
        results = str(int(numbers[0]) + int(numbers[2]))
        string = numbers[0] + numbers[1] + numbers[2] + '=' + results +'\n'
        out_file.write(string)







in_file_name_3 = 'Text files/greeneggs.txt'

def blah_blah_blah(in_file, out_file): 
    for line in in_file:
        if len(line) < 20:
            out_file.write(line)
        if len(line) >= 20:
            first_15 = line[:15] 
            out_file.write(first_15 + ', blah blah blah\n')






def main():
    with (open(in_file_name_3,'r') as in_file,
        open(out_file_name, 'w')as out_file): 
        blah_blah_blah(in_file, out_file)
    with (open(in_file_name_2,'r') as in_file,
        open(out_file_name, 'w')as out_file): 
        add_and_write(in_file, out_file)
    with open(file_name,'w') as my_file: 
        write_diamond_pattern(my_file, 5)
    with (open(in_file_name_1,'r') as in_file,
         open(out_file_name, 'w')as out_file): 
        last_name_first(in_file, out_file)


    

    
