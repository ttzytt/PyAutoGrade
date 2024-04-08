



import random


def average_length(read_file):
    
    total_length = 0
    words_read = 0
    
    for line in read_file:
        words = line.split()
        for word in words: 
            total_length += len(word) 
            words_read += 1
            
    return total_length/words_read 


def longest_word(read_file):
    current_longest_word = '' 
    
    for line in read_file:
        words = line.split()
        for word in words: 

            
            if len(word) > len(current_longest_word):
                current_longest_word = word
                
    return current_longest_word


def longest_palindrome(read_file):
    current_longest_palindrome = ''
    for line in read_file:
        words = line.split()
        for word in words:
            if word == word[::-1]:
                if len(word) > len(current_longest_palindrome):
                    current_longest_palindrome = word
    return current_longest_palindrome


def all_vowels_counter(read_file):
    vowel_count = 0 
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for line in read_file:
        words = line.split()
        for word in words: 
            for vowel in vowels: 
                if vowel in word:
                    vowel_count += 1
    return vowel_count  


def count_long_lines(read_file, min_length):
    long_line_count = 0 
    
    for line in read_file: 
        
        if len(line) >= min_length:
            long_line_count += 1 
                                 
    return long_line_count


def random_word(read_file):
    random_words = []
    for line in read_file:
        words = line.split()
        random_word = random.choice(words)
        random_words.append(random_word)

    final_random_word = random.choice(random_words)
    
    return final_random_word










file_name_AL = 'Text files/names.txt' 
with open(file_name_AL, 'r') as my_file:
    average_length = average_length(my_file)
    
file_name_LW = 'Text files/names.txt' 
with open(file_name_LW, 'r') as my_file:
    longest_word = longest_word(my_file)

file_name_LP = 'Text files/words.txt' 
with open(file_name_LP, 'r') as my_file:
    longest_palindrome_result = longest_palindrome(my_file)

file_name_VC = 'Text files/names.txt' 
with open(file_name_VC, 'r') as my_file:
    vowel_count = all_vowels_counter(my_file)

file_name_CLL = 'Text files/names.txt' 
with open(file_name_CLL, 'r') as my_file:
    long_line_count = count_long_lines(my_file, 10)

file_name_RW = 'Text files/names.txt' 
with open(file_name_RW, 'r') as my_file:
    random_word_result = random_word(my_file)

file_name_RWs = 'Text files/names.txt' 
with open(file_name_RWs, 'r') as my_file:
    random_words_results = random_words(my_file, 5)
    
print('The average length of a word in the file ' + file_name_AL + ' is ' +
      str(round(average_length, 5)))
print('The longest word in the file ' + file_name_LW + " is '" + str(longest_word) + "'")
print('The longest palindrome in the file ' + file_name_LP + " is '" +
      str(longest_palindrome_result))
print('The number of vowels in the file ' + file_name_VC + " is " + str(vowel_count))
print('The number of lines with more than 10 characters in the file ' + file_name_CLL +
      'is ' + str(long_line_count))
print('A random word from the file ' + file_name_RW + "is '" + random_word_result + "'")
