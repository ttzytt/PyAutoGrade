





    
        



def vowel_count(read_file):
    vowels = 'AaEeIiOoUu'
    count = 0
    for line in read_file:
        for letter in line:
            if letter in vowels:
                count += 1
    return count


def consonant_count(read_file):
    consonants = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
    count = 0
    for line in read_file:
        for letter in line:
            if letter in consonants:
                count += 1
    return count



def character_count(read_file):
    count = 0
    for line in read_file:
        count += len(line)
    return count

file_name = 'Text Files/names.txt'
with open(file_name, 'r') as my_file:
    list_of_lines = my_file.readlines()
    vowels = vowel_count(list_of_lines)
    consonants = consonant_count(list_of_lines)
    characters = character_count(list_of_lines)

print('Character count: ' + str(characters) + '.')
print('Vowel count: ' + str(vowels) + '.')
print('Consonant count: ' + str(consonants) + '.')
print('Other Character Count: ' + str(characters - vowels - consonants) + '.')






















