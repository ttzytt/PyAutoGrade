




import random


'''
T2
Returns the averge length of all strings in the file
    inputs:
        read_file  A file that is open for reading
'''
def average_length(read_file):
    total_length = 0
    total_words = 0
    for line in read_file:
        words = line.split()
        
        for word in words:
            total_length += len(word)
            total_words += 1
    
    if total_words == 0:
        return None

    return total_length / total_words



'''
T3
Returns the longest word in the file and when there are repeats, it only prints it once
    inputs:
        read_file  A file that is open for reading
'''
def longest_word(read_file):
    long_words = []
    current_length = 0
    
    for line in read_file:
        
        words = line.split()
        for word in words:
            word_length = len(word)
            
            if word_length > current_length:
                long_words = [word]
                current_length = word_length
                
            elif word_length == current_length:
                long_words.append(word)

    return long_words


'''
T4
Returns the longest word that can be read as a palindrome.
    inputs:
        read_file  A file that is open for reading
'''

def longest_palindrome(read_file):
    longest_palindrome = []
    current_length = 0
    
    for line in read_file:
        words = line.split()
        for word in words:
            
            if word == word[::-1]:
                word_length = len(word)
                if word not in longest_palindrome:
                    
                    if word_length > current_length:  
                        longest_palindrome =[word]
                        current_length = word_length
                            
                    elif word_length == current_length:
                        longest_palindrome.append(word)
                        
    return longest_palindrome
                
    
'''
T5
Returns the number of words that contain all vowels.
    inputs:
        read_file  A file that is open for reading
'''
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

'''
T6
Returns the strings that are longer than a certain length set by min_length
Keep in mind you will have to manually set the min_length
    inputs:
        read_file  A file that is open for reading
'''
def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file:
        if len(line) >= min_length:
            count += 1
    return count

'''
T7
Returns a random item or word in the form a list from the file with 2 same strings to have 
    inputs:
        read_file  A file that is open for reading
'''
def random_word(read_file):
    words_list = []
    for line in read_file:
        words = line.split()
        words_list += words
    
    return random.choice(words_list)


'''
T8
Returns a list of random words accordingly to how many words (set by num_words)
you want to print out
Keep in mind you will have to manually set the num_words
    inputs:
        read_file  A file that is open for reading
'''

def random_words(read_file, num_words):
    words_list = []
    random_list = []
    count = 0
    
    for line in read_file:
        words = line.split()
        words_list = words_list + words

    while num_words > count:
        random_list.append(random.choice(words_list))
        count += 1
    
    return random_list


'''
T9
Returns the number of words that match the given string (set by word)
Keep in mind you will have to manually set the word
    inputs:
        read_file  A file that is open for reading
'''
def specific_word_count(read_file, word):
    word_list = []
    count = 0
    for line in read_file:
        words = line.split()
        for specific_word in words:
            if specific_word == word:
                count += 1
    return count

'''
T10
Retuns the number of words that begin with a certain string (set by word_beginning)
Keep in mind you will have to manually set the word_beginning
    inputs:
        read_file  A file that is open for reading
'''
def starts_with_counter(read_file, word_beginning):
    word_list = []
    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            if word[0] == word_beginning:
                count += 1
    return count


def main():
    '''
    Gives T10, T9, T8 and T6 an input
    '''
    word_beginning = 'A'
    word = 'a'
    min_length = 5
    num_words = 3

        
    file_name = 'Text files/test file.txt'
    with open(file_name, 'r') as my_file:
        length_average = average_length(my_file)
        
        
    file_name = 'Text files/test file.txt'
    with open(file_name, 'r') as my_file:

        word_longest = longest_word(my_file)
        
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        min_count = count_long_lines(list_of_lines, min_length)
        
    file_name = 'Text files/test file.txt'
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        random_word_print = random_word(list_of_lines)
        
    file_name = 'Text files/test file.txt'
    with open(file_name, 'r') as my_file:
        vowels = all_vowels_counter(my_file)

    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        random_words_print = random_words(list_of_lines, num_words)
        
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        specific_word = specific_word_count(my_file, word)
        
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        list_of_lines = my_file.readlines()
        specific_start = starts_with_counter(list_of_lines, word_beginning)
        
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        specific_start = starts_with_counter(list_of_lines, word_beginning)
        
    file_name = 'Text files/test file.txt'
    with open(file_name, 'r') as my_file:
       
        palindrome_longest = longest_palindrome(my_file)

    print('Average length: ' + str(length_average))
    print('The words that contain all vowels is: ' +str(vowels))
    print('The longest string is: ' + str(word_longest))
    print('Words with a minimum count of ' + str(min_length) + ' characters is ' + str(min_count))
    print('The random word is ' + str(random_word_print))
    print('The number of times ' + str(word) + ' appear is: ' + str(specific_word))
    print('The number of words that start with a ' + str(word_beginning) + ' is ' + str(specific_start))
    print('Then random list of words is: ' + str(random_words_print))
    print('The longest palindrome is: ' + str(palindrome_longest))

if __name__ == "__main__":
    main()
