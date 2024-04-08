



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
            print(words)
            if ('a' in words): 
                num_words_all_vowels += 1
    return num_words_all_vowels          

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
    
