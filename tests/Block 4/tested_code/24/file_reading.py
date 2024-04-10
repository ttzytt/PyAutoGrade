



import random
random.seed()





def average_length(read_file):
    word_length = 0
    word_count = 0
    
    letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    for line in read_file:
        for character in line:
            if character in letters: 
                word_length += 1 
            else:
                word_count += 1
                word_length -= 1
    return word_length/word_count 



def longest_word(read_file):
    long_words = [] 
    current_length = 0
    for line in read_file:
        words = line.split() 
        for word in words:
            word = word.lower()
            word_length = len(word) 
            if word_length > current_length: 
                long_words = [word]
                current_length = word_length
            elif word_length == current_length: 
                if word not in long_words:
                    long_words.append(word)
    return long_words


def longest_palindrome(read_file):
    long_palindrome = []
    current_length = 0 
    for line in read_file:
        words = line.split()
        for word in words:
            word = word.lower()
            word_length = len(word)
            if word[::-1] == word: 
                if word_length > current_length: 
                    long_palindrome = [word] 
                    current_length = word_length
                elif word_length == current_length: 
                    if word not in long_palindrome: 
                        long_palindrome.append(word)
    return long_palindrome



def all_vowels_counter(read_file):
    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            if ('a' in word.lower() and 'e' in word.lower()
                and 'i' in word.lower() and 'o' in word.lower()
                and 'u' in word.lower()):
                count += 1 
    return count



def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file:
        line_length = len(line) 
        if line_length >= min_length: 
            count += 1 
    return count



def random_word(read_file):
    words_list = []
    for line in read_file:
        words = line.split() 
        words_list += words 
    return random.choice(words_list) 




def random_words(read_file, num_words):
    words_list = []
    random_number_of_words = []
    for line in read_file:
        words = line.split()
        words_list += words 
    for i in range(num_words): 
        random_word = random.choice(words_list) 
        random_number_of_words.append(random_word) 
    return random_number_of_words



def specific_word_count(read_file, word):
    count = 0
    for line in read_file:
        words = line.split()
        for _ in words: # Goes through all of the words
            if word == _: # If the word is in the list/line
                count += 1 # Add to the counter
    return count



def starts_with_counter(read_file, word_beginning):
    word_counter = 0
    for line in read_file:
        words = line.split()
        for word in words:
            slice_length = len(word_beginning) # Length that determines how much to slice
            if word_beginning == word[:slice_length]: # Compares the same length of two words
                word_counter += 1 # If the same, add one
    return word_counter
 
# -------------------------------Open & Run-----------------------------------------------
def main():
    min_length = 95
    num_words = 10
    word = 'bob'
    word_beginning = 'the'
    file_name = 'Text Files/some_tests.txt'

    #T2
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        length_average = average_length(list_of_lines)

    #T3
    with open(file_name, 'r') as my_file:
        long_word = longest_word(list_of_lines)

    #T4
    with open(file_name, 'r') as my_file:
        long_palindrome  = longest_palindrome(list_of_lines)

    #T5
    with open(file_name, 'r') as my_file:
        vowel_counter = all_vowels_counter(list_of_lines)

    #T6
    with open(file_name, 'r') as my_file:
        long_line_count = count_long_lines(list_of_lines, min_length)

    #T7
    with open(file_name, 'r') as my_file:
        word_at_random = random_word(list_of_lines)

    #T8
    with open(file_name, 'r') as my_file:
        some_random_words = random_words(list_of_lines, num_words)

    #T9
    with open(file_name, 'r') as my_file:
        specific_words = specific_word_count(list_of_lines, word)

    #T10
    with open(file_name, 'r') as my_file:
        word_that_starts_with = starts_with_counter(list_of_lines, word_beginning)

    #T2
    print('Average Word Length in the file ' + file_name + ' is: ' 
          + str(round(length_average, 3)) + ' characters.')
    print()

    #T3
    print('Longest word(s) in the file ' + file_name + ' is: \n'
          + str(long_word) + '.')
    print()

    #T4
    print('Longest palindrome(s) in the file ' + file_name + ' is: \n'
          + str(long_palindrome) + '.')
    print()

    #T5
    print('Words with all five vowels in the file ' + file_name + ' is: '
          + str(vowel_counter) + '.')
    print()

    #T6
    print('Amount of lines that have at least ' + str(min_length) + ' characters in the file '
           + file_name + ' is: '+ str(long_line_count) + '.')

    print()

    #T7
    print('A random word from the file ' + file_name + ' is: "' + str(word_at_random) + '"')
    print()

    #T8
    print('Here are ' + str(num_words) + ' random words from the file '
           + file_name + ': \n'+ str(some_random_words) + '.')

    print()

    #T9
    print('There are ' + str(specific_words) + ' instances of the word "'
           + str(word) + '" in the file ' + file_name + '.')

    print()

    #T10
    print('There are ' + str(word_that_starts_with) + ' instances of a word starting with "'
           + str(word_beginning) + '" in the file ' + file_name + '.')

    print()
    
if __name__ == "__main__":
    main()
