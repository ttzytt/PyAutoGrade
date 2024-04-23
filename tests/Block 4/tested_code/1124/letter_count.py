







def letter_counts(read_file):
    
    character_dict = {}
    for line in read_file:
        for character in line:
            if character not in character_dict: 
                character_dict[character] = 1
            else:
                character_dict[character] += 1
    
    return character_dict



    






file_name = 'Text files/test.txt'
with open(file_name, 'r') as my_file:
    character_dict = letter_counts(my_file)



letter = ord('A')
while letter <= ord('Z'):
    total_current_letter = 0
    
    for key in character_dict.keys():
        if key.lower() == chr(letter).lower():
            total_current_letter += character_dict[key]

    
    print(chr(letter) + ' ' + str(total_current_letter))
    letter += 1
