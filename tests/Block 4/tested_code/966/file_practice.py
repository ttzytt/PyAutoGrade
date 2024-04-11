








'''
Returns the number of characters in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def count_characters(read_file):
    count = 0  
    for line in read_file:  
        count += len(line)
    return count


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
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

a = 0
e = 0
i = 0
o = 0
u = 0

def count_vowels(read_file):
    for line in range(len(read_file)):
        for line in read_file:
            if line[i] == 'a':
                a += 1
            if line[i] == 'e':
                e += 1
            if line[i] == 'i':
                i += 1
            if line[i] == 'o':
                o += 1
            if line[i] == 'u':
                u += 1
    return a, e, i, o, u



    

















