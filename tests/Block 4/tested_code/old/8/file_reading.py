

import random
random.seed()


def average_length(read_file):
    
    
    
    sum_final = 0
    num_line = 0
    
    for line in my_file:
        
        words = line.split()
        sum_of_lengths = 0
        
        for word in words:
            sum_of_lengths += len(word)
        sum_final += (sum_of_lengths/len(words))
        num_line += 1

    
    print('The words in the file ' + str(read_file) + ' has an average of ' + str(sum_final/num_line)
      + ' characters.')
    print()

            

def longest_word(read_file):
    
    longest_words = []
    length_of_longest_word = 0

    for line in read_file:
                            

        words = line.split()
        for word in words:

            if len(word) == length_of_longest_word:
                                                   
                longest_words.append(word)
                
            elif len(word) > length_of_longest_word:
                                                    

                length_of_longest_word = len(word)
                                                  
                longest_words = [word] 

    
    print('The longest words in the file ' + str(read_file) + ' are ' + str(longest_words))
    print()


def longest_palindrome(read_file):
    
    longest_palindrome = []
    length_of_longest_palindrome = 0
                                    

    for line in read_file:
                            

        words = line.split()
        for word in words:
            word.lower()
            if word == word[::-1]:
                
                if len(word) == length_of_longest_palindrome:
                                                        
                    longest_palindrome.append(word)
                    
                elif len(word) > length_of_longest_palindrome:
                                                        
                                                        
                    
                    length_of_longest_palindrome = len(word)
                    longest_palindrome = [word] 

    
    print('The longest palindromes in the file ' + str(read_file) + ' are ' + str(longest_palindrome))
    print()


def all_vowels_counter(read_file):
    
    words_with_all_vowels = []
    for line in read_file:
                            

        words = line.split()
        for word in words:
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                words_with_all_vowels.append(word)
    
    print('The word with all five vowels in the file' + str(read_file) + ' are ' + str(words_with_all_vowels))
    print()


def count_long_lines(read_file, min_length):

    counter = 0
    
    for line in read_file:
        if len(line) >= min_length:
            counter += 1

    
    print('There are ' + str(counter) + ' lines with more than ' + str(min_length) + ' characters in the file '\
          + str(read_file))
    print()


def random_word(read_file):

    
    list_of_words = []
    
    for line in my_file:
        words = line.split()

        
        for word in words:
            list_of_words.append(word)

    
    chosen_word = random.choice(list_of_words)
    print(str(chosen_word) + ' is a random word from the file ' + str(read_file)) 
 
