









'''
Returns a dictionary with the number of each character in a file, with the key
being said character.
    inputs:
        read_file    A file that is open for reading.
'''
def letter_counts(read_file):
    characters = {}
    for line in read_file:
        for i in range(len(line)):
            if line[i] in characters:
                characters[line[i]] = characters[line[i]] + 1
            else:
                characters[line[i]] = 1
    return characters

        
'''
Prints how many times each letter appears in a file. Capital and lowercase
are counted as the same.
    inputs:
        read_file    A file that is open for reading.
'''
def alphabet_counts(read_file):
    characters = letter_counts(read_file)
    alphabet = {}
    for i in range(65,91):
        alphabet[chr(i)] = 0
    for character in characters:
        if character in alphabet:
            alphabet[character] = characters[character] + alphabet[character]
            
        elif ((ord(character) <= ord('z')) and (ord(character) >= ord('a'))): 
            capital = chr(ord(character) - 32)
            alphabet[capital] = alphabet[capital] + characters[character]

    for letter in alphabet:
        print(str(letter) + ' ' + str(alphabet[letter]))
        


        






def main():
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        alphabet_counts(my_file)

    



if __name__ == "__main__":
    main()
