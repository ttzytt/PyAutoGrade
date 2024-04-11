







file_name = 'Text files/my_cool_new_file.txt'
with open(file_name, 'w') as my_file:  
    big_string = ('This is a large string that even has multiple\n'
                  + 'lines in it. Hooray for that.')
    
    my_file.write(big_string)
    
    another_string = 'More text!'
    
    
    
    my_file.write(another_string)

    
    









in_file_name = 'Text files/names.txt'
out_file_name = 'Text files/lowercase_names.txt'




with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    for line in in_file:  
        line = line.lower()  
        out_file.write(line)  
        










in_file_name = 'Text files/names.txt'
out_file_name = 'Text files/lowercase_names_2.txt'

with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
    list_of_lines = in_file.readlines()
    
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].lower()

    out_file.writelines(list_of_lines)  



