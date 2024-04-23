







'''
Returns the amount of each letter in a given file.
    inputs:
        read_file    A file that is open for reading.
'''
def letter_counts(read_file):
    characters = {}
    with open(read_file, 'r') as my_file:
        for line in my_file:
            line.split()
            for word in line:
                word = word.upper()
                if word not in characters:
                    characters[word] = 1
                else:
                    characters[word] += 1
    return characters




'''
Returns the amount of each letter in a given file, but in alphabetical order.
    inputs:
        read_file    A file that is open for reading.
'''
def letter_count_in_alphabetical_order(read_file):
    character_sort = { 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    characters = letter_counts('Text files/names.txt')
    start_letter = 'A'
    for i in range(26):
        if start_letter in characters:
            character_sort[start_letter] += characters[start_letter]
        print(start_letter + ':' + str(character_sort[start_letter]))
        start_letter = chr(ord(start_letter) + 1)



def main():
    letter_counts('Text files/names.txt')
    letter_count_in_alphabetical_order('Test files/names.txt')
    
if __name__ == '__main__':
    main()
