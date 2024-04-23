



'''
# --------------------------  Organizing Code  --------------------------

## When we write functions that work with files, it is usually best for
## the function input to be a file rather than a file-name.
## (That is, an already open file, rather than a string that has the
## name of the file.)

## Here is some model code:

'''

    
        
'''
def count_characters(read_file):
    count = 0  # Number of characters seen so far.
    for line in read_file:  # Goes through each line in the file.
        count += len(line)
    return count


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
print()
# ------------------------  Reading a file, new style  ------------------------

## This does the same thing as the above code, but is considered better.
## (The reason it is better is pretty technical, but it has to do with working
## better if something goes wrong while the file is open.)

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    ## At this point, my_file refers to the open file, as before.
    ## Notice the indentation.
    full_content = my_file.read()
print(full_content[:13] + full_content[21:31] + full_content[312:301:-1])  # Print first 100 characters.
print()
print(full_content[:329])

## When we open a file with the 'with' keyword, we do not have to use
##     my_file.close()
## to close the file. The file closes automatically once we stop indenting.
## If we try to call my_file.close(), it will let us, but we will look
## foolish!
'''


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






















