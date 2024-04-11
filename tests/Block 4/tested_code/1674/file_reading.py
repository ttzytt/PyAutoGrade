




import random

random.seed()


'''
Returns the average length of each word in the file.
    inputs:
        read_file    A file that is open for reading.
'''

def average_length(read_file):
    word_count = 0  
    each_word_count = []  
    for line in read_file:
        words = line.split() 
        for word in words: 
            word_count = len(word) 
            each_word_count.append(word_count) 
    constant = 0
    for i in range(len(each_word_count)):
        constant = constant + each_word_count[i] 
    sum_of_all_the_lengths = constant    
    number_of_words = len(each_word_count)
    return sum_of_all_the_lengths / number_of_words
'''
Returns the longest word / words in the file.
    inputs:
        read_file    A file that is open for reading.
'''


def longest_word(read_file):
    word_list = []
    longest_word = '' 
    for line in read_file:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
                word_list.clear() 
                if word not in word_list:
                    word_list.append(longest_word)
            elif len(word) == len(longest_word):
                if word not in word_list:
                    word_list.append(word) 
    return word_list
'''
Returns the longest palindrome in the file.
    inputs:
        read_file    A file that is open for reading.
'''

def longest_palindrome(read_file):
    word_list = []
    longest_word = ''
    for line in read_file:
        words = line.split()
        for word in words:
            if word[::] == word[::-1]: 
                if len(word) > len(longest_word): 
                    longest_word = word 
                    word_list.clear()
                    word_list.append(longest_word)
                elif len(word) == len(longest_word):
                    if word not in word_list:
                        word_list.append(word)

    return word_list
'''
Returns the words that contain all vowels.
    inputs:
        read_file    A file that is open for reading.
'''


def all_vowels_counter(read_file):
    vowel_word_list = []
    for line in read_file:
        words = line.split()
        for word in words:
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word and 'A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word:
                vowel_word_list.append(word)
    return vowel_word_list       


'''
Returns the number of lines in the file that contains min_length of chaarcters
    inputs:
        read_file    A file that is open for reading.
'''

def count_long_lines(read_file, min_length):
    amount_of_lines = 0
    for line in read_file:
        if len(line) > min_length:
            amount_of_lines = amount_of_lines + 1
    return amount_of_lines

'''
Returns a random word in the file
    inputs:
        read_file    A file that is open for reading.
'''

def random_word(read_file):
    word_list = []
    list_of_lines = read_file.readlines()
    new_line = random.choice(list_of_lines)
    words = new_line.split()
    new_word = random.choice(words)
    word_list.append(new_word)
    return word_list


'''
Returns a list of num_words random words from read file
    inputs:
        read_file    A file that is open for reading.
'''
def random_words(read_file, num_words): 
    random_word_list = []
    words = read_file.read().split() 
    while len(random_word_list) < num_words:
        random_word = random.choice(words)
        if random_word not in random_word_list:
            random_word_list.append(random_word)
    return random_word_list


'''
Returns how many times a word appears in read_file
    inputs:
        read_file    A file that is open for reading.
'''
def specific_word_count(read_file, word):
    count = 0 
    for line in read_file:
        words = line.split()
        for word_from_file in words:
            if word_from_file == word:
                count = count + 1

    return count      



'''
Returns how many times a word begin with a certain letter
    inputs:
        read_file    A file that is open for reading.
'''
def starts_with_counter(read_file, word_beginning):

    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if word[0].lower() == word_beginning:
                count = count + 1
    return count      
                                

def main():
    
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word_average = average_length(my_file)

    print('The average length of each word in ' + file_name + ' is ' + str(round(word_average * 100)/100))

    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        long_word = longest_word(my_file)
    print()
    print('The longest word in ' + file_name + ' is ' + str(long_word))

    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        long_pal = longest_palindrome(my_file)
    print()
    print('The longest palindrome in ' + file_name + ' is ' + str(long_pal))
    print()

                        
    
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        all_vowels = all_vowels_counter(my_file)
    print('Words with every vowel in ' + file_name + ' is ' + str(all_vowels))
    print()


    
    min_length = int(input("What would you like your min_length to be? "))
    amount_of_lines = 0
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        long_lines = count_long_lines(my_file, min_length)
    print('The amount of lines longer than min_length in ' + file_name + ' is ' + str(long_lines))
    print()

    
    
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        rand_word = random_word(my_file)
    print('A random word in ' + file_name + ' is ' + str(rand_word))
    print()
    
    
    number_words = int(input("How many random words would you like? "))                    
    random_word_list = []
    file_name = 'Text files/names.txt'

    with open(file_name, 'r') as my_file:
        rand_words = random_words(my_file, number_words)
    print('Random Words In: ' + file_name + ' are ' + ', ' + (str(rand_words)))
    print()
    
    
    user_word = "rain."
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        word_count = specific_word_count(my_file, user_word)
    print(user_word + ' appears in '  + file_name, str(word_count) + ' times')
    print()

    
    word_beginning = input("What letter would you like to return how many times it begins a word in the file? ")
    file_name = 'Text files/test.txt'
    with open(file_name, 'r') as my_file:
        starts_with = starts_with_counter(my_file, word_beginning)
    print()
    print(word_beginning + ' starts ' + str(starts_with), 'words in ' + file_name )
    print()





if __name__ == "__main__":
    main()



              
