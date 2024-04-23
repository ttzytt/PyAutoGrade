








def letter_counts(read_file):
    letter_counts = {}
    for line in read_file: 
        for character in line: 
            if character in letter_counts:
                letter_counts[character] += 1
            else:
                letter_counts[character] = 1
    return letter_counts

def main():

    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        answer = letter_counts(my_file)

if __name__ == "__main__":
    main()
