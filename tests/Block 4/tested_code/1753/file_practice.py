






file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    
    
    full_content = my_file.read()
print(full_content[:100])  
print()







 



file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
print('Line 4 says: ' + list_of_lines[4])
print()

with open(file_name, 'r') as my_file:
    
    
    one_line = my_file.readline()
print('The first line says: ' + one_line)
print()

with open(file_name, 'r') as my_file:
    character_count = 0
    
    
    
    
    for line in my_file:  
        character_count += len(line)
print('Total characters: ' + str(character_count))
print()
    

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    full_content = my_file.readlines()
print(''.join(full_content[2::3]))
    
