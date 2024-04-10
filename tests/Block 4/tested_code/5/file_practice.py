




print('1')
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    full_content = my_file.read()
print(full_content[:10000])  
print()



print('2')
file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
print('Line 4 says: ' + list_of_lines[4])

with open(file_name, 'r') as my_file:
    
    
    one_line = my_file.readline()
print('The first line says: ' + one_line)

with open(file_name, 'r') as my_file:
    character_count = 0
    
    
    
    
    for line in my_file:  
        character_count += len(line)
print('Total characters: ' + str(character_count))
print()

file = input('Which file do you want to read, greeneggs or names?')
if file == 'greeneggs':
    print('1')
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        full_content = my_file.read()
    print(full_content[:10000])  
    print()
elif file == 'names':
    print('2')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        full_content = my_file.read()
    print(full_content[:10000])  
    print()
character = int(input('How many words do you think is in this file? '))
if file == 'greeneggs':
    if character == 3465:
        print('Congratuation, you are right!')
    else:
        print('Nah, it is 3465')
elif file == 'names':
    if character == 329:
        print('Congratuation, you are right!')
    else:
        print('Nah, it is 329')



print('3')
def count_characters(read_file):
    count = 0  
    for line in read_file:  
        count += len(line)
    return count


file_name = 'Text files/names.txt' 
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
print()

