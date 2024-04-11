




def average_length(read_file):

    total_word_length = 0
    word_count = 0

    for line in read_file:
        
        words = line.split()
        word_count += len(line.split())
        
        for word in words:
            total_word_length += len(word)

    return total_word_length / word_count




def longest_word(read_file):

    words = []
    longest_words = []

    for line in read_file:
        words += line.lower().split()

    print(words)

    max_length = len(words[0])
    
    for word in words:

        if len(word) > max_length:
            max_length = len(word)

        else:
            max_length = max_length

    for word in words:

        if len(word) == max_length and word not in longest_words:
            longest_words.append(word)

    return longest_words



def longest_palindrome(read_file):

    words = []
    longest_words = []

    for line in read_file:
        words += line.lower().split()

    print(words)

    for word in words:

        



    





def all_vowels_counter(read_file):

    return





def count_long_lines(read_file, min_length):

    return





def random_word(read_file):

    return






def random_words(read_file, num_words):

    return





def specific_word_count(read_file, word):

    return





def starts_with_counter(read_file, word_beginning):

    return




file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as read_file:
    longest_words = longest_word(read_file)

print(longest_words)
print()



