

import random
random.seed()



'''
Returns the average number of characters in each word in the file. Punctuation is counted as a
character in a word, but spaces are not.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    
    
    
    sum_final = 0
    num_line = 0
    
    for line in read_file:
        
        words = line.split()
        sum_of_lengths = 0
        
        for word in words:
            sum_of_lengths += len(word)
        sum_final += (sum_of_lengths/len(words))
        num_line += 1

    return sum_final/num_final
    
    


            
'''
Returns the longest word in the file. If there are multiple words with equal length, it
returns all of them.
    inputs:
        read_file    A file that is open for reading.
'''
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

    return longest_words
    

'''
Returns the longest palindrome word(same forward and backward) in the file. If there are
multiple palindromes of the same length, it returns all of them. Capital letters do not matter,
but punctuation does.
    inputs:
        read_file    A file that is open for reading.
'''
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

'''
Returns a list of words containting all 5 vowels in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    
    words_with_all_vowels = []
    for line in read_file:
                            

        words = line.split()
        for word in words:
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                words_with_all_vowels.append(word)
    
    print('The word with all five vowels in the file' + str(read_file) + ' are ' + str(words_with_all_vowels))
    print()

'''
Returns the number of line which have at  least min_length characters. All characters count
aside from new line characters(including punctuation and spaces).
    inputs:
        read_file    A file that is open for reading.
        min_length    Minimum number of characters for each line
'''
def count_long_lines(read_file, min_length):

    counter = 0
    
    for line in read_file:
        if len(line) >= min_length:
            counter += 1

    
    print('There are ' + str(counter) + ' lines with more than ' + str(min_length) + ' characters in the file '\
          + str(read_file))
    print()

'''
Returns a random word from the file. Do not run it on long files
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):

    
    list_of_words = []
    
    for line in read_file:
        words = line.split()

        
        for word in words:
            list_of_words.append(word)

    
    chosen_word = random.choice(list_of_words)
    print(str(chosen_word) + ' is a random word from the file ' + str(read_file)) 
 
'''
Returns num_words number of random words from the file. Do not run it on long files
    inputs:
        read_file    A file that is open for reading.
        num_words    The number of random words to be returned.
'''
def random_words(read_file, num_words):
    list_of_words = []
    
    for line in read_file:
        words = line.split()

        
        for word in words:
            list_of_words.append(word)

    
    chosen_words = []
    
    for i in range(num_words):
        chosen_words.append(random.choice(list_of_words))
    print(chosen_words + "are" + num_words + "random words from the file" + read_file)
    
'''
Counts the number of times a word appears in a file. Everything is assumed to be lowercase
    inputs:
        read_file    A file that is open for reading.
        word         The word that the function is looking for.
'''
def specific_word_count(read_file, word):
    counter = 0
    word.lower()
    
    
    for line in read_file:
        words = line.split()

        
        for word_in_file in words:
            word_in_file.lower()
            if word_in_file == word:
                counter += 1
    print("The word " + word + " appears " + counter + " times in the file " + read_file)

'''
Counts the number of times a word starts with specified characters.Everything is assumed to be
lowercase.
    inputs:
        read_file    A file that is open for reading.
        word         The word that the function is looking for.
'''
def starts_with_counter(read_file, word_beginning):
    
    word_beginning.lower()
    counter = 0
    list_of_words = []

    
    for line in read_file:

        words = line.split()
        for word in words:
            
            word.lower()
            
            if word_beginning == word[:len(word_beginning)]:
                counter += 1
    print(str(counter) + " words start with " + word_beginning + " in the file " + read_file)


def main():
    with open('Text files/commonwords.txt', 'r') as my_file:
        min_num_char = input("What would you like your minimum number of characters to be? ")
        number_words = input("How many random words would you like? ")
        input_word = input("What word would you like to search for? ")
        input_start = input("What word beginning would you like to search for? ")

        print('The words in the file ' + average_length(my_file) + ' has an average of ' + str(sum_final/num_line)
      + ' characters.')
        print()

        print('The longest words in the file ' + str(my_file) + ' are ' + str(longest_word(my_file)))
        print()
        longest_word(my_file)
        longest_palindrome(my_file)
        all_vowels_counter(my_file)
        count_long_lines(my_file, min_num_char)
        random_word(my_file)
        random_words(my_file, number_words)
        specific_word_count(my_file, input_word)
        starts_with_counter(my_file, input_start)

if __name__ == "__main__":
    main()
