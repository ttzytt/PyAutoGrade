file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    
    
    character_count = 0
    list_of_line = my_file.readline()
    for line in my_file:  
        character_count += len(line)
    full_content = my_file.read()
        
print(list_of_line) 
 
print('Rest characters: ' + str(character_count))
 
print(full_content[:50])
print()
