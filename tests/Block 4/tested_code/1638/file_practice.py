file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
print('Line 4 says: ' + list_of_lines[4])
print()
