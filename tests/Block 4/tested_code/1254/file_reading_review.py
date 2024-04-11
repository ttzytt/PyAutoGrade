



import random
random.seed()


'''
Returns the average lengths of the word in the file
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    
    character_count = 0
    
    amount_of_words = 0
    for line in read_file:
        amount_of_words += 1
        character_count += len(line)
    
    return (character_count/amount_of_words)



'''
Returns the longest word(s) in the file and will return a list so it can find multiple if there's a tie
    inputs:
        read_file    A file that is open for reading.
'''
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



'''
Returns a list of the longest word in the file that is a palindrome that means it's the same
forward and backward
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    palindromes = [] # This is a list to store all the palindromes in the file
    longest_palindromes = [] # This is a list to store the longest palindrome(s) in the file
    length_of_largest = 0 # Keeps track of the largest word length in the file
    for line in read_file: # Loops thorugh all the lines in the file
        words = line.splitlines() # Breaks each line into a list of words
        for word in words: # loops thorugh each word in the list
            if len(word) >= length_of_largest and word == word[::-1]: # Checks if the word is a palindrome
                palindromes.append(word)
                length_of_largest = len(word)
    for i in range (len(palindromes)): # Loops thorugh the palindrome list and finds the largest ones
        if len(palindromes[i]) == length_of_largest:
            longest_palindromes.append(palindromes[i])
    return longest_palindromes
#R Testing on green eggs returns spaces, spaces doesn't count

'''
Returns the number of words in the file that contain all five vowels
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    count = 0
    for line in read_file: 
        words = line.split() 
        for word in words:
            
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word: 
                count += 1
    return count

'''
Returns the number of lines in the file that have at least min_length characters
    inputs:
        read_file    A file that is open for reading.
        min_length   An integer used to track the minimum length of a word
'''
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
                
'''
Returns a random word form the file, the probablity of the getting each word is dependent on how often it shows
up in the file. Be careful using too big of a file for this function
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    full_content = [] 
    for line in read_file: 
        words = line.split() 
        for word in words: 
            full_content.append(word)
    return random.choice(full_content) 

'''
Returns the number of times the word 'word' appears in the file
    inputs:
        read_file    A file that is open for reading.
        word         A string that is a word
'''
def specific_word_count(read_file, word):
    count = 0 
    for line in read_file: 
        words = line.split() 
        for word_ in words: 
            if word_ == word:
                
                count += 1
    return count


'''
Returns the number of words in the file that start with the string word_beginning
    inputs:
        read_file    A file that is open for reading.
        word_beginning    A string that is the beginning of a word
'''
def start_with_counter(read_file, word_beginning):
    count = 0 
    for line in read_file: 
        words = line.split() 
        for word in words: 
            if word[:(len(word_beginning))] == word_beginning:
                
                count += 1
    return count
            

    



file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    average_length_of_words = average_length(my_file)
print('The file ' + file_name + ' contains ' + str(average_length_of_words) + ' characters.')
print()


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    longest_word_or_words = longest_word(my_file)
print('The longest word(s) in the file ' + file_name + ' is/are ' +  str(longest_word_or_words) + '.')
print()


file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)
print('The longest palindrome(s) in the file ' + file_name + ' is/are ' + str(longest_palindromes) + '.')
print()

file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    all_vowels_count = all_vowels_counter(my_file)
print('The number of words that contain all vowels in the file '
      + file_name + ' is/are ' + str(all_vowels_count) + '.')
print()

file_name = 'Text files/greeneggs.txt'
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

file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    word_count = specific_word_count(my_file, 'eggs')
print("The word 'eggs' appears in the file "
      + file_name +' ' + str(word_count) + ' times.')
print()

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    start_with_word_count = start_with_counter(my_file, 'A')
print('There are ' + str(start_with_word_count) + ' words in the file '
      + file_name + " that start with 'A'.")
print()


