



import random
random.seed()





def average_length(read_file):
    
    number_terms = 0
    total_length = 0
    
    for line in read_file:
        
        total_length += len(line)
        number_terms += 1
    
    return total_length/number_terms







def longest_word(read_file):
    
    list_longest_words = []
    len_longest_word = 0
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            
            if len(word) > len_longest_word:
                list_longest_words = [word]
                len_longest_word = len(word)
            
            elif len(word) == len_longest_word:
                list_longest_words.append(word)
    return list_longest_words






def longest_palindrome(read_file):
    
    list_longest_palindromes = []
    len_longest_palindromes = 0
    
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            if word == word[::-1]:
                
                
                if len(word) > len_longest_palindromes:
                    list_longest_palindromes = [word]
                    len_longest_palindromes = len(word)
                
                elif len(word) == len_longest_palindromes:
                    list_longest_palindromes.append(word)
    return list_longest_palindromes






def all_vowels_counter(read_file):
    
    num_all_vowels = 0
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            word.lower()
            
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
                num_all_vowels += 1
    return num_all_vowels






def count_long_lines(read_file, min_length):
    
    num_long_lines = 0
    
    for line in read_file:
        
        
        if len(line) - 1 >= min_length:
            num_long_lines += 1
    return num_long_lines







def random_word(read_file):
    
    all_words = []
    
    for line in read_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    
    return  random.choice(all_words)








def random_words(read_file, num_words):
    
    all_words = []
    
    random_words = []
    
    for line in read_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    
    for _ in range(num_words):
        current_random = random.choice(all_words)
        random_words.append(current_random)
    return random_words    







def specific_word_count(read_file, word):
    
    num_times = 0
    
    for line in read_file:
        words = line.split()
        for current_word in words:
            
            lowered_word = current_word.lower()
            if lowered_word == word:
                num_times += 1
                
    return num_times







def starts_with_counter(read_file, word_beginning):
    
    num_words = 0
    
    for line in read_file:
        words = line.split()
        for word in words:
            
            lowered_word = word.lower()
            
            if lowered_word[:len(word_beginning)] == word_beginning:
                num_words += 1
    return num_words




file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    average_length_words = average_length(my_file)

file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    longest_words = longest_word(my_file)

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)

file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    num_all_vowels = all_vowels_counter(my_file)

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    num_long_lines = count_long_lines(my_file, 10)

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    one_random_word = random_word(my_file)

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    list_random_words = random_words(my_file, 5)

file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    num_words = specific_word_count(my_file, 'eggs')

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    num_words_beginning = starts_with_counter(my_file, 'ap')



print(average_length_words)
print()
print(longest_words)
print()
print(longest_palindromes)
print()
print(num_all_vowels)
print()
print(num_long_lines)
print()
print(one_random_word)
print()
print(list_random_words)
print()
print(num_words)
print()
print(num_words_beginning)
