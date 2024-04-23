



import random








'''
Returns the average length of all the words in a given file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    word_len_sum = 0
    num_words = 0
    for line in read_file:
        words = line.split()
        for word in words:
            word_len_sum = word_len_sum + len(word)
            num_words += 1
    return word_len_sum / num_words



'''
Returns the longest word in a given file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    long_word = ' '
    current_word = ' '
    old_word = ' '
    longest_word_len = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if len(word) > longest_word_len:
                longest_word_len = len(word)
                long_word = word
    return long_word


'''
Returns the longest palindrome in a given file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    longest_palindrome_len = 0
    long_palindrome_list = []
    longest_palindrome_list = []
    for line in read_file:
        words = line.split()
        line.lower()
        for word in words:
            
            if word == word[::-1]:
                if len(word) >= longest_palindrome_len:
                    long_palindrome_list.append(word)
                    longest_palindrome_len = len(word)

    for i in range(len(long_palindrome_list)):
        if len(long_palindrome_list[i]) == longest_palindrome_len:
            longest_palindrome_list.append(long_palindrome_list[i])
    return longest_palindrome_list




'''
Returns the amount of words with every vowel
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    all_vowels = 0
    for line in read_file:

        words = line.split()

        for word in words:
            if('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                all_vowels += 1
                
    return all_vowels



'''
Returns the amount of lines longer than a given length in a specified file.
    inputs:
        read_file    A file that is open for reading.
        min_length   The minimum line length. Provided by the user
'''
def count_long_lines(read_file, min_length):
    amount_greater = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            character = 0
            for letter in word:
                character += 1
            if character >= min_length:
                amount_greater += 1
    return amount_greater


'''
Returns a random word in a given file.
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    word_list = []
    for line in read_file:
        line.split()
        word_list.append(line)
    
    random_num = random.randint(0, len(word_list))
    return word_list[random_num]


'''
Returns a specified of random words in a given file.
    inputs:
        read_file    A file that is open for reading.
        num_words    The amount of random words
'''
def random_words(read_file, num_words):
    word_list = []
    return_list = []
    for line in read_file:
        line.split()
        word_list.append(line)
    for i in range(num_words):
        random_num = random.randint(0, len(word_list))
        return_list.append(word_list[random_num])
    return return_list


'''
Returns the amount of a specified word in a given file.
    inputs:
        read_file    A file that is open for reading.
        specific_word    The specified word
'''
def specific_word_count(read_file, word):
    amount_of_same_words = 0
    for line in read_file:
        words = line.split()
        for term in words:
            if term == word:
                amount_of_same_words += 1
    return amount_of_same_words


'''
Returns the amount of words that start with a specific character.
    inputs:
        read_file    A file that is open for reading.
        word_beginning    A specified character
'''
def starts_with_counter(read_file, word_beginning):
    num_beginning = 0

    for line in read_file:
        words = line.split()
        for word in words:

            if word_beginning.lower() == word[:len(word_beginning)].lower():
                num_beginning += 1
    return num_beginning







'''
Runs all of the functions.
Opens and closes the file each time it runs.
'''
def main():
    file_name = 'Text files/commonwords.txt'
    
    with open(file_name, 'r') as my_file:
        average_len = average_length(my_file)
        

    print('The average word length in ' + file_name + ' is ' + str(average_len)
          + ' characters.')
    print()



    with open(file_name, 'r') as my_file:
        longest = longest_word(my_file)
        
    print('The longest word in ' + file_name + ' is ' + str(longest)
          + '.')
    print()


    with open(file_name, 'r') as my_file:

        palindrome = longest_palindrome(my_file)

    print('The longest palindrome in ' + file_name + ' is ' + str(palindrome)
          + '.')
    print()


    with open(file_name, 'r') as my_file:

        vowels_counter = all_vowels_counter(my_file)

    print('The amount of words with all the vowels in ' + file_name + ' is ' + str(vowels_counter)
          + '.')
    print()


    min_length = int(input("Minimum length: "))
    with open(file_name, 'r') as my_file:
        long_lines = count_long_lines(my_file, min_length)
    print('The amount of lines with length > ' + str(min_length) + ' In the file ' + file_name + ' is ' + str(long_lines)
          + '.')
    print()


    with open(file_name, 'r') as my_file:

        word = random_word(my_file)

    print('A random word in ' + file_name + ' is ' + str(word) + '.')
    print()


    num_words = int(input('How many words?'))
    with open(file_name, 'r') as my_file:

        words = random_words(my_file,num_words)

    print(str(num_words) + ' random words in ' + file_name + ' are ' + str(words) + '.')
    print()


    word = str(input('What word?'))
    with open(file_name, 'r') as my_file:

        word_count = specific_word_count(my_file,word)

    print('The amount of the word ' + str(word) + ' in ' + file_name + ' is ' + str(word_count) + '.')
    print()


    word_beginning = str(input('Starting character(s): '))
    with open(file_name, 'r') as my_file:

        starts_with = starts_with_counter(my_file,word_beginning)

    print('The amount of words that start with ' + str(word_beginning) + ' in ' + file_name + ' is ' + str(starts_with) + '.')
    print()

if __name__ == "__main__":
    main()
