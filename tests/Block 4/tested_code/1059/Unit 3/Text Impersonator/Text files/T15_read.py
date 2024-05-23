





import random
random.seed()




def write_diamond_pattern(out_file, width):
    count = 1 
    count_1 = width - 2 
    for i in range (width):
        i_1 = i +1
        
        if count<=width:
            out_file.write((' '*((width - count)//2)) + (count*'x') + (' '*((width - count)//2)))
            out_file.write("\n")
            count += 2 
        
        elif count_1>0:
            out_file.write((' '*((width - count_1)//2)) + (count_1*'x') + (' '*((width - count_1)//2)))
            out_file.write("\n")
            count_1 -= 2 


def last_name_first(in_file, out_file):
    lines = in_file.read()
    words = lines.split()
    word_index = 0
    while word_index < len(words)-1:
        temp_string = ''
        temp_string = words[word_index+1] + ', ' + words[word_index] 
        
        out_file.write(temp_string)
        out_file.write("\n") 
        word_index += 2


def add_and_write(in_file, out_file):
    lines = in_file.read()
    words = lines.split()
    index = 0
    
    while index < len(words)-2:
        temp_1 = words[index] 
        temp_2 = words[index+2] 
        addition = int(temp_1) + int(temp_2)
        out_file.write(words[index]+ ' '+words[index+1] + ' '+words[index+2] + ' = ')
        out_file.write(str(addition))
        out_file.write("\n")
        index += 3




def blah_blah_blah(in_file_name, out_file_name):
    lines = in_file_name.read()
    line = lines.split()
    i = 0
    while i < len(line):
        if len(line[i]) > 20:
            temp_str = line[i][0:15] + ', blah blah blah' 
            
            out_file_name.write(temp_str)
            out_file_name.write("\n")
            
        elif len(line[i]) <= 20:
            out_file_name.write(line[i])
            out_file_name.write("\n")
        i += 1
    
    

    
width = 11
with open('Text files/out_file.txt', 'w') as out_file:
    task_1 = write_diamond_pattern(out_file, width)

    
with (open('Text files/names.txt', 'r') as in_file,
        open('Text files/names_new.txt', 'w') as out_file):
    task_2 = last_name_first(in_file, out_file)

with (open('Text files/addition.txt', 'r') as in_file,
        open('Text files/addition_new.txt', 'w') as out_file):
    task_3 = add_and_write(in_file, out_file)

with (open('Text files/addition.txt', 'r') as in_file,
        open('Text files/addition_new.txt', 'w') as out_file):
    task_3 = add_and_write(in_file, out_file)
    
with (open('Text files/T14.txt', 'r') as in_file_name,
        open('Text files/T14_new.txt', 'w') as out_file_name):
    task_4 =blah_blah_blah(in_file_name, out_file_name)
