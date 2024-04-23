



def letter_counts(read_file):
    key = {}
    for line in read_file:
        words = line.split()
        for character in words:
            if character in key:
                key[character] += 1
            elif character not in key:
                length_of_key = len(key)
                key[character] = 1
    return key
            
            
read_file = input('What do you want me to read?')
old_key = letter_counts(read_file)

new_key = {}
letter = 'A'

print(old_key)
while letter <= 'Z':

    temp_count = 0
    if letter in old_key == True:
        temp_count = old_key[letter]
        print('yes')
        print(temp_count)

    if letter.lower() in old_key == True:
        temp_count += old_key[letter]
        print('yars')
        print(temp_count)

    if temp_count != 0:
        new_key[letter] = temp_count
    else:
     letter = chr(ord(letter) + 1)

print(new_key)
