



def letter_counts(read_file):
    letter_count = {}
    addition = 1
    for line in read_file:
        words = line.split()
        for word in words:
            for letter in range(len(word) - 1):
                letter_count[letter] = 1
                if word[letter] == word[letter + 1]:
                    letter_count[letter] += 1
                
    print(letter_count)



file_name = 'Text files/test file.txt'
with open(file_name, 'r') as my_file:
    letter_counts(my_file)
