






import random
random.seed()


def average_length(read_file):
    
    
    total_words = 0
    total_word_length = 0
    for line in my_file: 
        words = line.split() 
        for word in words: 
            total_words += 1
            total_word_length += len(word)

    return float(total_word_length / total_words)



def longest_word(read_file):
    longest_words = [''] 
    for line in my_file: 
        words = line.split() 
        for word in words: 
            if len(word) > len(longest_words[0]):
                longest_words = [word] 
            elif len(word) == len(longest_words[0]):
                longest_words.append(word) 
    return longest_words



def longest_palindrome(read_file):
    longest_palindromes = ['']
    for line in my_file:
        words = line.split()
        for word in words:
            if len(word) > len(longest_palindromes[0]) and word == word[::-1]:
                longest_palindromes = [word] 
            elif len(word) == len(longest_palindromes[0]) and word == word[::-1]:
                longest_palindromes.append(word) 
    return longest_palindromes



def all_vowels_counter(read_file):
    num_words_all_vowels = 0 
    for line in my_file:
        words = line.split()
        for word in words:
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
                num_words_all_vowels += 1
    return num_words_all_vowels



def count_long_lines(read_file, min_length):
    num_long_lines = 0
    for line in my_file:
        if len(line) > min_length:
            num_long_lines += 1
    return num_long_lines



def random_word(read_file):
    all_words = []
    for line in my_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    return random.choice(all_words)

'''
# Returns a list of num_words random words from the file read_file
def random_words(read_file, num_words):
    all_words = []
    for line in read_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    return random.sample(all_words, num_words)
'''



def specific_word_count(read_file, word):
    word_count = 0
    for line in my_file:
        words = line.split()
        for current_word in words:
            if current_word == word:
                word_count += 1
    return word_count

file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    average_word_length = average_length(my_file)
    print('The average word length is ' + str(average_word_length) + '. ')

with open(file_name, 'r') as my_file:
    longest_words = longest_word(my_file)
    print('The longest words are ' + str(longest_words))

with open(file_name, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)
    print('The longest palindromes are ' + str(longest_palindromes))

with open(file_name, 'r') as my_file:
    num_words_all_vowels = all_vowels_counter(my_file)
    print('There are ' + str(num_words_all_vowels) + ' words that contain all of the vowels. ')

with open(file_name, 'r') as my_file:
    min_length = 15 
    num_long_lines = count_long_lines(my_file, min_length)
    print('There are ' + str(num_long_lines) + ' number of lines that contain over 15 characters.')

with open(file_name, 'r') as my_file:
    random_word = random_word(my_file)
    print('The random word is ' + random_word + '.')

'''
with open(file_name, 'r') as my_file:
    num_words = 5
    random_words = random_words(my_file, num_words)
    print('The random words are ' + random.sample(words, num_words) + '.')
'''

with open(file_name, 'r') as my_file:
    specific_word = 'and' 
    word_count = specific_word_count(my_file, specific_word)
    print('The number of times the word "' + specific_word + '" showed up is ' + str(word_count) + '.')
    


