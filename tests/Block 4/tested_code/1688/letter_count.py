


def letter_count(read_file):

    letter_count = {}

    for line in read_file:

        words = line.split()

        for word in words:
            for i in range(len(word)):
                if word[i] not in letter_count:
                    letter_count[word[i]] = 1
                else:
                    letter_count[word[i]] += 1

    return letter_count

def main():

    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        letter_dictionary = letter_count(read_file)

        for i in range(ord('A'), (ord('Z') + 1)):

            count = 0

            for letter in letter_dictionary:
                if ord(letter.upper()) == i:
                    count += letter_dictionary[letter]

            print(chr(i) + '    ' + str(count))

    print()
    print(letter_dictionary)


if __name__ == "__main__":
    main()
