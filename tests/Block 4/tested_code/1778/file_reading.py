

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
        if len(words) > 0:
            sum_final += (sum_of_lengths/len(words))
        num_line += 1

    if num_line > 0:
        return sum_final/num_line
    
    


            
'''
Returns the longest word in the file. If there are multiple words with equal length, it
returns all of them. No word will appear twice. Output will not have any uppercase letters
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
                                                   
                if word not in longest_words:
                    longest_words.append(word)
                
            elif len(word) > length_of_longest_word:
                                                    

                length_of_longest_word = len(word)
                                                  
                longest_words = [word] 

    return longest_words
    

'''
Returns the longest palindrome word(same forward and backward) in the file. If there are
multiple palindromes of the same length, it returns all of them. Capital letters do not matter,
but punctuation does. No word will appear twice. Output will not have any uppercase values
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    
    longest_palindrome = []
    length_of_longest_palindrome = 0
                                    

    for line in read_file:
                            

        words = line.split()
        for word in words:
            word = word.lower()
            if word == word[::-1]:
                
                if len(word) == length_of_longest_palindrome:
                                                             
                    if word not in longest_palindrome:
                        longest_palindrome.append(word)
                    
                elif len(word) > length_of_longest_palindrome:
                                                        
                                                        
                    
                    length_of_longest_palindrome = len(word)
                    longest_palindrome = [word]

    return longest_palindrome

    
    

'''
Returns a list of words containting all 5 vowels in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    
    counter = 0
    for line in read_file:
                            

        words = line.split()
        for word in words:
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                counter += 1 
    
    return counter


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

        
        num_new_line_char = 0
        for char in line:
            if char == '\'':
                num_new_line_char += 1

        # Subtracts the newline characters
        len_final = len(line) - num_new_line_char
            
        if len_final > min_length:
            counter += 1

    # Prints result
    return counter

'''
Returns a random word from the file. Do not run it on long files
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):

    
    list_of_words = []
    # Goes line by line and creates a list of all words
    for line in read_file:
        words = line.split()

        # Goes through every word in the line and adds it to the list of all words
        for word in words:
            list_of_words.append(word)

    # Randomly chooses a word and returns
    chosen_word = random.choice(list_of_words)
    return(chosen_word)
 
'''
Returns num_words number of random words from the file. Do not run it on long files
    inputs:
        read_file    A file that is open for reading.
        num_words    The number of random words to be returned.
'''
def random_words(read_file, num_words):
    list_of_words = []
    # Goes line by line and creates a list of all words
    for line in read_file:
        words = line.split()

        # Goes through every word in the line and adds it to the list of all words
        for word in words:
            list_of_words.append(word)

    
    chosen_words = []
    # Chooses a random word num_word number of times and appends it to a list
    for i in range(num_words):
        chosen_words.append(random.choice(list_of_words))
    return chosen_words
    
'''
Counts the number of times a word appears in a file. Everything is assumed to be lowercase
    inputs:
        read_file    A file that is open for reading.
        word         The word that the function is looking for.
'''
def specific_word_count(read_file, word):
    counter = 0
    
    # Goes line by line and checks if each word is the same as the specified word
    for line in read_file:
        words = line.split()

        # Checks if each word in the line is the same as wpecified word
        for word_in_file in words:
            if word_in_file.lower() == word.lower():
                counter += 1# Counts how many times the word appears
    return counter

'''
Counts the number of times a word starts with specified characters.Everything is assumed to be
lowercase.
    inputs:
        read_file    A file that is open for reading.
        word         The word that the function is looking for.
'''
def starts_with_counter(read_file, word_beginning):
    
    counter = 0
    list_of_words = []

    # These loops go word by word
    for line in read_file:

        words = line.split()
        for word in words:
            
            # Checks to see if the first characters are equal to word_beginning
            if word_beginning.lower() == word[:len(word_beginning)].lower():
                counter += 1

    return counter

#-----------------------------------Main---------------------------------------
def main():
    

    min_num_char = int(input("What would you like your minimum number of characters to be? "))
    number_words = int(input("How many random words would you like? "))
    input_word =input("What word would you like to search for? ")
    input_start = input("What word beginning would you like to search for? ")
        
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        print('The words in the file ' + file_name + ' has an average of ' + str(average_length(my_file))
      + ' characters.')
        print()
        
    with open(file_name, 'r') as my_file:

        print('The longest words in the file ' + file_name + ' are ' + str(longest_word(my_file)))
        print()

    with open(file_name, 'r') as my_file:
    
        print('The longest palindromes in the file ' + file_name + ' are ' + str(longest_palindrome(my_file)))
        print()

    with open(file_name, 'r') as my_file:
  
        print('There are '+ str(all_vowels_counter(my_file)) + ' words with all the vowels in the file ' + file_name)
        print()

    with open(file_name, 'r') as my_file:
      
        print('There are ' + str(count_long_lines(my_file, min_num_char)) + ' lines with more than ' + str(min_num_char) + ' characters in the file '\
          + file_name)
        print()
        
    with open(file_name, 'r') as my_file:

        print(str(random_word(my_file)) + ' is a random word from the file ' + file_name)
        print()
       
    with open(file_name, 'r') as my_file:

        print(str(random_words(my_file, number_words)) + " are " + str(number_words) + " random words from the file" + file_name)
        print()

    with open(file_name, 'r') as my_file:

        print("The word " + str(input_word) + " appears " + str(specific_word_count(my_file, input_word)) + " times in the file " + file_name)
        print()

    with open(file_name, 'r') as my_file:

        print(str(starts_with_counter(my_file, input_start)) + " words start with " + str(input_start) + " in the file " + file_name)
        print()

        
    

if __name__ == "__main__":
    main()
