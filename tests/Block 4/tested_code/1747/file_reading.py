







import random
random.seed()



'''
T2
Returns the average length of all the words in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
        
    num_words = 0 
    num_letters = 0 
    
    for line in read_file:  
        line_of_words = line.split()
        
        num_words += len(line_of_words)
        

        for j in range(len(line_of_words)):
            num_letters += len(line_of_words[j])
        
                    
    return(str(num_letters / num_words))


'''
T3
Returns the longest list of word(s) of all words in the file.
If there are ties, the list contains all the tied words.
If there are repeated words, they aren't put into the list repeatedly.

    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):

    # Create a list to store the longest word(s) and store the first word.
    long_words = ['']
    # Using a shortest word, assuming that there are words in the list
    # longer than ''.
     
    # Looping through.
    for line in read_file:  # Goes through each line in the file.
        line_of_words = line.split()
        # Creates a list of words in this line.
        
        for word in line_of_words:
            if len(word) > len(long_words[-1]):
                # Checks if there is a longer word.
                long_words = [word]
                # Take over the list, because we found a new longest.
            elif len(word) == len(long_words[-1]):
                # Checks if there is a tie.
                if word not in long_words:
                    long_words.append(word)
                    # If not repeated, add the word to the list.                   

    return(str(long_words))


'''
T4
Returns the longest list of word(s) of palindrome words in the file.
If there are ties, the list contains all the tied words.
If there are repeated words, they aren't put into the list repeatedly.

    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):

    
    long_words = ['']
    
    
    
    
    for line in read_file:  
        line_of_words = line.split()
        
        
        for word in line_of_words:

            if (len(word) % 2) == 1:
                len_odd_half_word = ((len(word) + 1) / 2)
                
                if word[0:(int(len_odd_half_word) - 1):1] == word[-1:(int(len_odd_half_word) - 1):-1]:
                
                    if len(word) > len(long_words[-1]):
                        
                        long_words = [word]
                        
                    elif len(word) == len(long_words[-1]):
                        
                        if word not in long_words:
                            long_words.append(word)
                            

            else:
                len_even_half_word = len(word) / 2
                
                if word[0:(int(len_even_half_word)):1] == word[-1:(int(len_even_half_word) - 1):-1]:
                
                    if len(word) > len(long_words[-1]):
                        
                        long_words = [word]
                        
                    elif len(word) == len(long_words[-1]):
                        
                        if word not in long_words:
                            long_words.append(word)
                            

    return(str(long_words))


'''
T5
Returns the number of words in the file that contain all five vowels,
not necessarily in that order.
If there are repeated words, they are counted repeatedly.

    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):

    num_fives = 0 
    
    for line in read_file:  
        line_of_words = line.split()
        

        for word in line_of_words: 
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
            
                num_fives += 1
                
                  
    return(str(num_fives))


'''
T6
Returns the number of lines in the file that contain at least min_length characters.
min_length is pre-determined by user input.
Spaces don't count as characters, but punctuations do.

    inputs:
        read_file    A file that is open for reading.
'''
def count_long_lines(read_file, min_length):

    num_long_lines = 0 # The count of lines that fits the minimum length criteria.

    for line in read_file:  # Goes through each line in the file.

        line_of_words = line.split()
        # Creates a list of words in this line.
        no_space_line = ''.join(line_of_words)
        # Returns this line without spaces in between.

        if len(no_space_line) >= min_length: # Checks if it fits criteria.
            num_long_lines += 1 # If it fits, add to count.

    return(str(num_long_lines))
    

'''
T7
Returns a random word in the file.
Warning: Full content of the file stored, be careful using this with a lengthy file.

    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):

    words = [] # Creates a list for all words in the file.
    
    for line in read_file:  # Goes through each line in the file.

        line_of_words = line.split()
        # Creates a list of words in this line.
        for line_of_word in line_of_words:
            words.append(line_of_word)
            # Adds this line's words to the all words list.

    random_word_choice = random.choice(words)
    

    return(str(random_word_choice))


'''
T8
Returns a list of random words in the file according to the input number of words.
Warning: Full content of the file stored, be careful using this with a lengthy file.

    inputs:
        read_file    A file that is open for reading.
'''
def random_words(read_file, num_words):

    words = [] 
    random_word_choice = [] 
    
    for line in read_file:  

        line_of_words = line.split()
        
        for line_of_word in line_of_words:
            words.append(line_of_word)
            

    for i in range(num_words):
        random_word = random.choice(words)
        
        random_word_choice.append(random_word)
        

    return(str(random_word_choice))


'''
T9
Returns the number of times the word 'word' appears in the file.

    inputs:
        read_file    A file that is open for reading.
'''
def specific_word_count(read_file, word):

    num_the_word = 0 

    for line in read_file:  

        for word_in_line in line: 
            if word_in_line == word: 
                num_the_word += 1 

    return(str(num_the_word))


'''
T10
Returns the number of words in the file that begin with the input letter.

    inputs:
        read_file    A file that is open for reading.
'''
def starts_with_counter(read_file, word_beginning):

    num_word = 0 

    for line in read_file:  

        for word in line:
            if word[0].lower() == word_beginning.lower():
            
                num_word += 1 

    return(str(num_word))




def main():

    file_name = 'Text files/greeneggs.txt'

    with open(file_name, 'r') as my_file:
        average_word_length= average_length(my_file)

    print('The file ' + file_name + ' has on average ' + average_word_length
          + ' characters in each word.')
    print()


    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        longest_word_list = longest_word(my_file)

    print('The longest word(s) in the file ' + file_name + ' are ' + longest_word_list)
    print()


    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        longest_palindrome_list = longest_palindrome(my_file)

    print('The longest palindrome(s) in the file ' + file_name + ' are')
    print(longest_palindrome_list)
    print()


    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        all_vowels_words = all_vowels_counter(my_file)

    print('The number of words that contain all five vowels in the file ' + file_name)
    print('are ' + all_vowels_words)
    print()


    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        min_length = int(input('What would you like the minimum length to be?: '))
        num_long_lines = count_long_lines(my_file, min_length)

    print('The file ' + file_name + ' has ' + (num_long_lines) + ' lines that')
    print('contain at least ' + str(min_length) + ' characters.')
    print()


    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        random_choice = random_word(my_file)

    print('A random word from the file ' + file_name + ' is ' + (random_choice))
    print()


    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        num_words = int(input('How many random words would you like?: '))
        random_choice = random_words(my_file, num_words)

    print(str(num_words) + ' random words from the file ' + file_name + ' are')
    print(random_choice)
    print()


    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word = 'word'
        num_specific_word = specific_word_count(my_file, word)

    print("The word 'word' appeared " + num_specific_word + ' times in the file')
    print(file_name)
    print()


    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word_beginning = input('Which letter would you like as the beginning?: ')
        same_beginning_words = starts_with_counter(my_file, word_beginning)

    print('There are ' + same_beginning_words + ' words from the file')
    print(file_name + " that begin with the letter '" + word_beginning + "'.")
    print()


if __name__ == "__main__":
    main()































