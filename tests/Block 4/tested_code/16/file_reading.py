



import random
random.seed()



def average_length(read_file):
    
    character_count = 0
    
    amount_of_words = 0
    for line in read_file:
        amount_of_words += 1
        character_count += len(line)
    
    return (character_count/amount_of_words)



def longest_word(read_file):
    length_of_largest = 0
    # This is a list of the words that have lengths larger than the last
    # the point of this list is to narrow down the longest words
    initial_longest_words = []
    # This list is to return the final words with the longest lengths
    final_longest_words = []
    for line in read_file:
        words = line.splitlines()
        for word in words:
            # Loops thorugh every line and storing the word in the list if they're longer than the last
            if len(word) >= length_of_largest:
                length_of_largest = len(word)
                initial_longest_words.append(word)
    for i in range (len(initial_longest_words)):
        
        if len(initial_longest_words[i]) == length_of_largest:
            final_longest_words.append(initial_longest_words[i])
    return final_longest_words




def longest_palindrome(read_file):
    palindromes = [] 
    longest_palindromes = [] 
    length_of_largest = 0 
    for line in read_file: 
        words = line.splitlines() 
        for word in words: 
            if len(word) >= length_of_largest and word == word[::-1]: 
                palindromes.append(word)
                length_of_largest = len(word)
    for i in range (len(palindromes)): 
        if len(palindromes[i]) == length_of_largest:
            longest_palindromes.append(palindromes[i])
    return longest_palindromes


def all_vowels_counter(read_file):
    count = 0
    for line in read_file: 
        words = line.split() 
        for word in words:
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word: 
                count += 1
    return count


def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file: 
        sum_of_characters = 0 
        words = line.split()
        for word in words: 
            sum_of_characters += len(word) 
        if sum_of_characters >= min_length: 
            count += 1
    return count
                




def random_word(read_file):
    full_content = []
    for line in read_file:
        words = line.split()
        for word in words:
            full_content.append(word)
    return random.choice(full_content)
            
      
    
    













file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    average_length_of_words = average_length(my_file)
print('The file ' + file_name + ' contains ' + str(average_length_of_words) + ' characters.')
print()


file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    longest_word_or_words = longest_word(my_file)
print('The longest word(s) in the file ' + file_name + ' is/are ' +  str(longest_word_or_words) + '.')
print()


file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)
print('The longest palindrome(s) in the file ' + file_name + ' is/are ' + str(longest_palindromes) + '.')
print()

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    all_vowels_count = all_vowels_counter(my_file)
print('The number of words that contain all vowels in the file '
      + file_name + ' is/are ' + str(all_vowels_count) + '.')
print()

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    long_lines_count = count_long_lines(my_file, 10)
print('The number of lines in the file '
      + file_name + ' that contain at least 10 characters are ' + str(long_lines_count) + '.')
print()

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    random_word = random_word(my_file)
print('A random word in the file '
      + file_name + ' is ' + str(random_word) + '.')
print()
