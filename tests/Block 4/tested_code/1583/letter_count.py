










def letter_counts(read_file):
    character_counts = {}

    
    for line in read_file:
        for character in line:
            if character not in character_counts:
                character_counts[character] = 1
            else:
                character_counts[character] += 1

    return character_counts



def main():
    
    with open('Text files/greeneggs.txt', 'r') as my_file:
        character_counts = letter_counts(my_file)

    
    letters = []
    for i in range(65, 91):
        letters.append(chr(i))

    for letter in letters:
        letter_count = 0
        for character in character_counts:
            
            if character.lower() == letter.lower():
                letter_count += character_counts[character]

        print(letter + ' ' + str(letter_count))


if __name__ == "__main__":
    main()
