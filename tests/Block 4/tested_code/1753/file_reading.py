




import random

random.seed()




'''
Returns the average word length of the file being read
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    word_count = 0
    character_count = 0
    for line in read_file:
        words = line.split()
        word_count = word_count + len(words)
        for word in words:
            character_count = character_count + len(word)
    return (character_count/word_count)


'''
Returns a list of the longest word(s)
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    longest_words = ['']
    
    for line in read_file:
        words = line.split()
           
        for i in range(len(words)):
            if len(words[i]) > len(longest_words[0]):
                longest_words = []
                if words[i].lower() not in longest_words:
                    longest_words.append(words[i].lower())
                
            elif len(words[i]) == len(longest_words[0]):
                if words[i].lower() not in longest_words:
                    longest_words.append(words[i].lower())
                
    return longest_words


'''
Returns a list of the longest palindrome(s)
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    longest_palindromes = ['']
    
    for line in read_file:
        words = line.split()
       
        for i in range(len(words)):
            if words[i].lower() == words[i][::-1].lower():
                if len(words[i]) > len(longest_palindromes[0]):
                    longest_palindromes = []
                    if words[i].lower() not in longest_palindromes:
                        longest_palindromes.append(words[i].lower())
                    
                elif len(words[i]) == len(longest_palindromes[0]):
                    if words[i].lower() not in longest_palindromes:
                        longest_palindromes.append(words[i].lower())
                    
    return longest_palindromes
    

'''
Returns the number of words that contain all 5 vowels: A, E, I, O, U
    inputs:
        read_file    A file that is open for reading.
'''

def all_vowels_counter(read_file):
    counter = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word :
                counter += 1

    return counter

'''
Returns the number of lines that contain at least min_length characters
    inputs:
        read_file    A file that is open for reading.
        min_length   A number of characters
'''
def count_long_lines(read_file, min_length):
    counter = 0
    for line in read_file:
        if len(line) >= min_length:
            counter += 1
    return counter


'''
Reads the WHOLE file and returns a random word from that file
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    words = read_file.read()
    word_list = words.split()
    random_word = random.randint(0, len(word_list))
    return word_list[random_word]
    
'''
Reads the WHOLE file and returns a random word from that file
    inputs:
        read_file    A file that is open for reading.
        num_words
'''
def random_words(read_file, num_words):
    words = read_file.read()
    word_list = words.split()
    random_words_list = []
    for i in range(num_words):
        random_words_list.append(word_list[random.randint(0, len(word_list))])
    return random_words_list

'''
Returns the number of times a specific word appears
    inputs:
        read_file    A file that is open for reading.
        word         A specific word that is being searched for
'''
def specific_word_count(read_file, word):
    counter = 0
    for line in read_file:
        words = line.split()
        for i in range(len(words)):
            if words[i] == word:
                counter += 1
    return counter

'''
Returns the number of words that begin with a specific beginning
    inputs:
        read_file    A file that is open for reading.
        word_beginning  A specific beginning that is being searched for
'''
def starts_with_counter(read_file, word_beginning):
    counter = 0
    for line in read_file:
        words = line.split()
        for i in range(len(words)):
            if words[i][0:len(word_beginning)] == word_beginning:
                counter += 1
    return counter




def main():
    
    


    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        average_word_len = average_length(my_file)

    with open(file_name, 'r') as my_file:
        longest_word_list = longest_word(my_file)

    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        longest_palindrome_list = longest_palindrome(my_file)

    with open(file_name, 'r') as my_file:
        words_with_vowels = all_vowels_counter(my_file)

    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        long_lines = count_long_lines(my_file, 10)
        
    with open(file_name, 'r') as my_file:
        rand_word = random_word(my_file)

    with open(file_name, 'r') as my_file:
        rand_words = random_words(my_file, 5)

    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        word_count = specific_word_count(my_file, 'I')
        
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        starter = starts_with_counter(my_file, 'ando')


        
    print('The average length of each word is ' + str(average_word_len))
    print('The longest word(s) is/are ' + str(longest_word_list))
    print('The longest palindrome(s) is/are ' + str(longest_palindrome_list))
    print('The number of words that contain all 5 vowels is ' + str(words_with_vowels))
    print('The number of lines that contain at least min_length characters is ' + str(long_lines))
    print('A random word from the file is ' + str(rand_word))
    print('Some random words from the file are ' + str(rand_words))
    print('The amount of times \"I\" appears in the file is ' + str(word_count))
    print('The number of words that begin with \"ando\" is ' + str(starter))

if __name__ == "__main__":
    main()





