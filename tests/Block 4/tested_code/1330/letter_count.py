




print('Start Task 22 letter count: ')

def letter_counts(read_file):
    alphabet = {}
    for i in range(26):
        order = ord('A')+i
        alphabet[chr(order)] = 0 
    
    read_file_2 = read_file.read() 
    
    for character in read_file_2:
        
        character = character.upper() 
        if character in alphabet:
            alphabet[character] += 1 
    for i in range(26):
        order = ord('A')+i
        return (order, ' ', alphabet[chr(order)])

read_file = 'Text files/names.txt'
with open(read_file, 'r') as my_file:
    counts = letter_counts(my_file)
print(counts)
