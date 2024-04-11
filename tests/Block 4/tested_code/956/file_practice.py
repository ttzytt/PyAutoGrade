



file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
print('Line 20 says: ' + list_of_lines[20])
print()

with open(file_name, 'r') as my_file:
    
    
    one_line = my_file.readline()
    two_line = my_file.readline()
print('The second line says: ' + two_line)
print()

with open(file_name, 'r') as my_file:
    character_count = 0
    
    
    
    
    for line in my_file:  
        character_count += len(line)
print('Total characters: ' + str(character_count))
print()
