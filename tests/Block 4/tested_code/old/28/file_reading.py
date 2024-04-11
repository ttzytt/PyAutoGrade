



import random


delimiters = [' ']





def average_length(read_file):
    sum_so_far = 0
    words_so_far = 0

    
    for line in read_file:
        
        for delimiter in delimiters:
            
            
            line = " ".join(line.split(delimiter))
            
        words = line.split()

        
        for word in words:
            sum_so_far += len(word)
            words_so_far += 1

    return sum_so_far / words_so_far









def longest_word(read_file):
    longest_words = ['']

    
    for line in read_file:
        
        for delimiter in delimiters:
            
            
            line = " ".join(line.split(delimiter))
            
        words = line.split()

        if len(words) > 0:

            for word in words:
                if len(word) > len(longest_words[0]): 
                    
                    longest_words = [word]
                if ((len(word) == len(longest_words[0]))
                     and (word not in longest_words)): 
                    longest_words.append(word)

    if longest_word != ['']: 
        return longest_words










def longest_palindrome(read_file):
    
    
    
    longest_palindromes = ['']

    
    for line in read_file:
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
            
        words = line.split()

        if len(words) > 0:

            for word in words:
                word = word.lower()
                if word == word[::-1]: 
                    if len(word) > len(longest_palindromes[0]): 
                        longest_palindromes = [word]
                    if ((len(word) == len(longest_palindromes[0]))
                         and (word not in longest_palindromes)): 
                        longest_palindromes.append(word)

    if longest_palindromes != ['']:
        return longest_palindromes







def all_vowels_counter(read_file):
    
    
    num_all_vowels = 0

    
    for line in read_file:
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
            
        words = line.split()

        for word in words:
            word = word.lower() 
            if ('a' in word and 'e' in word and 'i' in word and 'o' in word
                and 'u' in word):
                 num_all_vowels += 1


    return num_all_vowels








def count_long_lines(read_file, min_length):
    num_long_lines = 0
    lines = [] 

    for line in read_file:
        if len(line) - 2 >= min_length: 
                                        
            num_long_lines += 1
            lines.append(line)

    return num_long_lines








def random_word(read_file):
    contents = []

    
    for line in read_file:
        
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
        line = line.split()

        
        for word in line:
            contents.append(word)

    
    random_word_index = random.randint(0, len(contents))
    return contents[random_word_index]
    








def random_words(read_file, num_words):
    
    

    random_words_list = []
    contents = []

    
    for line in read_file:
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
        line = line.split()

        for word in line:
            contents.append(word)

    
    for i in range(num_words):
        random_word_index = random.randint(0, len(contents))
        random_words_list.append(contents[random_word_index])
        
    return random_words_list








def specific_word_count(read_file, counting_word):
    word_counter = 0
    counting_word = counting_word.lower()

    
    for line in read_file:
        
        
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
        words = line.split()

        for word in words:
            word = word.lower()
            if word == counting_word:
                word_counter += 1

    return word_counter







def starts_with_counter(read_file, word_beginning):
    word_counter = 0
    word_beginning = word_beginning.lower() 

    
    for line in read_file:
        
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
        words = line.split()

        for word in words:
            word = word.lower()
            if word_beginning == word[:len(word_beginning)]: 
                                                             
                word_counter += 1

    return word_counter
    

green_eggs_file = 'Text files/greeneggs.txt'
words_file = 'Text files/words.txt'
common_words_file = 'Text files/commonwords.txt'
names_file = 'Text files/names.txt'
addition_file = 'Text files/addition.txt'




with open(green_eggs_file, 'r') as my_file:
    average_length_of_words = average_length(my_file)

print('The average length of words in greeneggs.txt is '
      + str(average_length_of_words) + '.')
print()




with open(words_file, 'r') as my_file:
    longest_words = longest_word(my_file)

print('The longest words in words.txt are '
      + ', '.join(longest_words) + '.')
print()




with open(words_file, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)

print('The longest palindromes in words.txt are '
      + ', '.join(longest_palindromes) + '.')
print()




with open(words_file, 'r') as my_file:
    num_all_vowels = all_vowels_counter(my_file)

print('The number of words with all of the vowels in words.txt is '
      + str(num_all_vowels) + '.')
print()




with open(green_eggs_file, 'r') as my_file:
    num_long_lines = count_long_lines(my_file, 6)

print('The number of lines with at least 6 characters in greeneggs.txt is '
      + str(num_long_lines) + '.')
print()




with open(words_file, 'r') as my_file:
    one_random_word = random_word(my_file)

print('A random word from words.txt is ' + one_random_word + '.')
print()




with open(green_eggs_file, 'r') as my_file:
    random_word_list = random_words(my_file, 10)

print('10 random words from greeneggs.txt are '
      + ', '.join(random_word_list) + '.')
print()
