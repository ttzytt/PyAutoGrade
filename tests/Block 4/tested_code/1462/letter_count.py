



'''
Returns a dictionary of a file, the keys are the characters and the values
are the number of characters:
    inputs:
        read_file    A file that is open for reading.
'''
def letter_counts(read_file):
    letter_to_numbers = {}

    for line in read_file:
        for letter in line:
            if letter in letter_to_numbers:
                letter_to_numbers[letter] += 1
            else:
                letter_to_numbers[letter] = 1
                    
    return letter_to_numbers



file_name = 'Text files/t22_input.txt'
with open(file_name, 'r') as my_file:
    letter_counted = letter_counts(my_file)



letter_in_order = {}

for i in range(26):
    letter_in_order[chr(ord('A') + i)] = 0

    
    if (chr(ord('A') + i)) in letter_counted:
        letter_in_order[chr(ord('A') + i)] += letter_counted[chr(ord('A') + i)]

    
    if (chr(ord('a') + i)) in letter_counted:
        letter_in_order[chr(ord('A') + i)] += letter_counted[chr(ord('a') + i)]

for key in letter_in_order:
    print(key + ' ' + str(letter_in_order[key]))
