





'''
Returns the average length of the words in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    count_word = 0
    count_character = 0
    
    for line in read_file: 
        words = line.split()
        count_word += len(words)

        for word in words:
            count_character += len(word)

    return count_character / count_word
        




'''
Returns the list of the longest words of the file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    length = 0
    longest_word = []
    
    for line in read_file:
        words = line.lower().split()
        
        for word in words:
            if len(word) == length:
                longest_word.append(word)
            elif len(word) > length:
                longest_word = [word]
                length = len(word)

    return longest_word





'''
Returns a list of the longest word that is a palindrome in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    length = 0
    longest_palindrome = []

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if word == word[::-1]:
                if len(word) == length:
                    longest_palindrome.append(word)
                elif len(word) > length:
                    longest_palindrome = [word]
                    length = len(word)

    return longest_palindrome





'''
Returns the number of words in the file that contain all five vowels A, E, I, O, U.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    vowels_counter = []

    for line in read_file:
        words = line.lower().split()

        for word in words:
            
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                vowels_counter.append(word)

    return vowels_counter





'''
Returns the number of lines in the file that contains at least a particular number of characters.
    inputs:
        read_file    A file that is open for reading.
        min_length   The given number of characters that the lines need to at least contain
'''
def count_long_lines(read_file, min_length):
    count = 0

    for line in read_file:
        if len(line) >= min_length:
            count += 1

    return count




'''
WARNING: This function reads the whole file at first, so beware of super long files!!!
Return a random word from the file. 
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    import random
    file = read_file.read().split()
    word = random.choice(file)
    return word




'''
WARNING: This function reads the whole file at first, so beware of super long files!!!
Return a list of a given number of random words from the file. 
    inputs:
        read_file    A file that is open for reading.
        num_words    The number of random words chosen.
'''
def random_words(read_file, num_words):
    import random
    words = []
    file = read_file.read().split()
    
    for _ in range(num_words):
        random.shuffle(file)
        words.append(file[0])
        file = file[1:]

    return words



'''
Returns the number of times the word 'word' appears in the file
    inputs:
        read_file    A file that is open for reading.
        word         The word that we are searching for.
'''
def specific_word_count(read_file, word):
    count = 0
    
    for line in read_file:
        words = line.lower().split()
        for wordd in words:
            if wordd == word.lower():
                count += 1

    return count



'''
Returns the number of words in a file that begin with a specific word.
    inputs:
        read_file        A file that is open for reading.
        word_beginning   We're searching for words that start with it.
'''
def starts_with_counter(read_file, word_beginning):
    count = 0

    for line in read_file:
        words = line.lower().split()
        for word in words:
            if word[:len(word_beginning)] == word_beginning.lower():
                count += 1

    return count



# Main Function
def main():

    # T2
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        average_characters = average_length(my_file)
    print('The file ' + file_name + ' has an average of ' + str(average_characters)
          + ' characters per word.')
    print()

    # T3
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        longest_words = longest_word(my_file)


    print('The list of the longest words of the file ' + file_name + ' is\n' + str(longest_words))
    print()

    # T4
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        longest_palindromes = longest_palindrome(my_file)


    print('The list of the longest palindromes of the file ' + file_name + ' is\n' + str(longest_palindromes))
    print()

    # T5
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        vowels_counter = all_vowels_counter(my_file)

    print('The list of the vowels of ' + file_name + 'that contains all vowels is\n' + str(vowels_counter))
    print()

    # T6
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        # Cannot be count_long_lines = count_long_lines()
        count = count_long_lines(my_file, 16)

    print('There are ' + str(count) + ' words in ' + file_name + ' that contains at least 10 characters')
    print()

    # T7
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word = random_word(my_file)

    print('The random word chosen in ' + file_name + ' is ' + str(word) + '.')
    print()

    # T8
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        words = random_words(my_file, 3)

    print('The 3 random words chosen in ' + file_name + ' are ' + str(words) + '.')
    print()

    # T9
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        number = specific_word_count(my_file, "them")

    print("The number of times the word 'them' appears is " + str(number) + " times.")
    print()

    # T10
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        number = starts_with_counter(my_file, "a")

    print("The number of words that starts with a 'a' is " + str(number) + '.')
    
    
if __name__ == "__main__":
    main()

    
