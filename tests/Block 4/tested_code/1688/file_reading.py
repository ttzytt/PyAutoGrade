


'''
Return the average length of all the words.

    inputs:
        read_file    A file that is open for reading.
'''

def average_length(read_file):

    total_word_length = 0
    word_count = 0

    for line in read_file:
        
        words = line.split()
        word_count += len(line.split())
        
        for word in words:
            total_word_length += len(word)

    return total_word_length / word_count


'''
Return the longest word / words in the file.
(Include punctuations)

    inputs:
        read_file    A file that is open for reading.
'''
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

            
    
    for word in words:

        if len(word) == max_length and word not in longest_words:
            longest_words.append(word)

    return longest_words

'''
Return the longest palindormes in the file.
*Palindorme is a word that has same spelling forward and backward

    inputs:
        read_file   A file that is open for reading
'''
def longest_palindrome(read_file):

    longest_palindromes = []
    max_length = 0

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if word[ : :1] == word[ : :-1]:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_palindromes = [word]

                elif len(word) == max_length:
                    longest_palindromes.append(word)

    return longest_palindromes

'''
Return the # of words that contain all five vowels (A, E, I, O, U).

    inputs:
        read_file   A file that is open for reading
'''

def all_vowels_counter(read_file):


    count = 0

    for line in file:
        words = line.split()
        for word in words:
            if 
                count += 1
    return count



'''
Return the # of lines that is longer (in characters) than the minimum length.

    inputs:
        read_file   A file that is open for reading
        min_length   A value 
'''

def count_long_lines(read_file, min_length):

    return



'''
Return the a random word.

    inputs:
        read_file   A file that is open for reading
'''

def random_word(read_file):

    return




'''
Return the a list of random words.

    inputs:
        read_file   A file that is open for reading
        num_words   # of random words returned
'''

def random_words(read_file, num_words):

    return



'''
Return the # of times a word that appears.

    inputs:
        read_file   A file that is open for reading
        word   The target word to check # of appearance
'''

def specific_word_count(read_file, word):

    return



'''
Return the # of words that begins with target string.

    inputs:
        read_file   A file that is open for reading
        word_beginning   A preset string to search for words that begins with this
'''

def starts_with_counter(read_file, word_beginning):

    return




file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as read_file:
    longest_words = longest_word(read_file)

print(longest_words)
print()



