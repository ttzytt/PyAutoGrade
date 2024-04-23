


import random


file_name = 'Text files/paper_soccer_functions.py'

large_list = []

with (open(file_name, 'r') as my_file,
        open('Text files/paper_soccer_functions_shuffled.py', 'w') as out_file):
        for line in my_file:
            for character in line:
                large_list.append(character)

        random.shuffle(large_list)
        
        out_file.writelines(large_list)

        print(large_list)
    
    


def letter_counts(read_file):

    character_counts = {}

    for line in read_file:
        line.lower()
        for i in range(len(line)):
            
            if line[i] not in character_counts:
                character_counts[line[i]] = 1
                
            else:
                character_counts[line[i]] += 1

    for character in character_counts:
        
        if character != '\n':
            
            print(character + ' ' + str(character_counts[character]))

        else:
            print('\\n' + ' ' + str(character_counts[character]))

    return character_counts



file_name = 'Text files/paper_soccer_functions_shuffled.py'
with open(file_name, 'r') as my_file:
    character_counts = letter_counts(my_file)

print()
print()

for i in range(26):
    if (chr(ord('a') + i)) in character_counts:
        print(chr(ord('a') + i) + ' ' + str(character_counts[chr(ord('a') + i)]))
    


    
