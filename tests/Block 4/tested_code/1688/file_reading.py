





'''
Return the average length of all the words.

    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):

    total_word_length = 0
    word_count = 0

    for line in read_file:
        
        words = line.split()
        word_count += len(line.split())
        
        for word in words:
            total_word_length += len(word)

    return total_word_length / word_count



'''
Return the longest word / words in the file.
(Include punctuations)

    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):

    words = []
    longest_words = []

    for line in read_file:
        words += line.lower().split()

    max_length = len(words[0])

    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

            
    
    for word in words:

        if len(word) == max_length and word not in longest_words:
            longest_words.append(word)

    return longest_words



'''
Return the longest palindormes in the file.
* Palindorme is a word that has same spelling forward and backward

    inputs:
        read_file   A file that is open for reading
'''
def longest_palindrome(read_file):
    
    longest_palindromes = []
    max_length = 0

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if word == word[ : :-1]:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_palindromes = [word]
                elif len(word) == max_length and \
                     word not in longest_palindromes:
                    longest_palindromes.append(word)

    return longest_palindromes



'''
Return the # of words that contain all five vowels (A, E, I, O, U).
(No repitition)

    inputs:
        read_file   A file that is open for reading
'''
def all_vowels_counter(read_file):

    count = 0
    all_vowels_words = []

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if 'a' and 'e' and 'i' and 'o' and 'u' in word and word not in all_vowels_words:
                count += 1
                
    return count



'''
Return the # of lines that is longer (in characters) than the minimum length.

    inputs:
        read_file   A file that is open for reading
        min_length   A value 
'''
def count_long_lines(read_file, min_length):

    count = 0

    for line in read_file:
        if len(line) >= min_length:
            count += 1

    return count



'''
Return the a random word.

    inputs:
        read_file   A file that is open for reading
'''
def random_word(read_file):

    import random

    words = []

    for line in read_file:
        words += line.split()

    return random.choice(words)



'''
Return a list of random words.

    inputs:
        read_file   A file that is open for reading
        num_words   # of random words returned
'''
def random_words(read_file, num_words):
    
    import random

    words = []
    list_of_random_words = []

    for line in read_file:
        words += line.split()

    for _ in range(num_words):
        list_of_random_words.append(random.choice(words))

    return list_of_random_words



'''
Return the # of times a word appears.

    inputs:
        read_file   A file that is open for reading
        word   The target word to check # of appearance
'''
def specific_word_count(read_file, target_word):
    
    count = 0

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if word == target_word.lower():
                count += 1

    return count



'''
Return the # of words that begins with target string.

    inputs:
        read_file   A file that is open for reading
        word_beginning   A preset string to search for words that begins with this
'''
def starts_with_counter(read_file, word_beginning):

    count = 0
    
    for line in read_file:
        words = line.lower().split()
        
        for word in words:
            if len(word) >= len(word_beginning) and \
               word.lower()[ :len(word_beginning)] == word_beginning.lower():
                count += 1
    
    return count





def main():

    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        average_length_of_words = average_length(read_file)

    print('The Average length of the words in the file: ')
    print(average_length_of_words)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        longest_words = longest_word(read_file)

    print('The longest words in the file: ')
    print(longest_words)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        longest_palindromes = longest_palindrome(read_file)

    print('The longest palindrome in the file: ')
    print(longest_palindromes)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        all_vowels_words_count = all_vowels_counter(read_file)

    print('The number of words that contains all vowels in the file: ')
    print(all_vowels_words_count)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        min_length = int(input('Set Minimum Length? '))
        long_lines_count = count_long_lines(read_file, min_length)

    print('The number of lines that is longer than ' + str(min_length) + ' characters in the file: ')
    print(long_lines_count)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        word = random_word(read_file)

    print('A random word in the file: ')
    print(word)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        num_words = int(input('How many random words do you want to generate? '))
        words = random_words(read_file, num_words)

    print(str(num_words) + ' random words in the file: ')
    print(words)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        target_word = str(input('What word do you want to find? '))
        specific_word_appear_times = specific_word_count(read_file, target_word)

    print("The number of times '" + str(target_word) + "' appeared in the file: ")
    print(specific_word_appear_times)
    print()



    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as read_file:
        word_beginning = str(input('What do you want to start with? '))
        specific_beginning_word_count = starts_with_counter(read_file, word_beginning)

    print("The number of words that start with '" + str(word_beginning) + "' in the file: ")
    print(specific_beginning_word_count)
    print()



if __name__ == "__main__":
    main()
