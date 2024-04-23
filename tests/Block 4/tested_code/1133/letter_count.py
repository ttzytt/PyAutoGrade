
def letter_counts(read_file):
    """
    Returns count how many times each character appears in a text file.
    char_counts    A dictionary and values are their counts.
    """

    
    char_counts = []
    
    for line in read_file:
            for char in line:
                char_counts += 1

    return char_counts

def main():
    
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        print("charactor number:", letter_counts(my_file))
    

if __name__ == "__main__":
    main()
