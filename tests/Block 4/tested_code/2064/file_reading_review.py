














'''
Returns the average length of the words in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    count = 0
    line_number = 0
    for line in read_file:
        count += len(line)
        line_number += 1

    return count / line_number


'''
Returns a list of longest word or words in the file. Ignores capitalization, but
counts punctuation as part of the word. Ignores duplicates
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    max_words = [''] 
    for line in read_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if (word not in max_words):
                if (len(word) > len(max_words[0])):
                    max_words = [word]
                elif (len(word) == len(max_words[0])):
                    max_words.append(word)

    return max_words


'''
Returns a list of the longest word or words in file that is a 
palindrome (the same forward and backward). Only prints one copy of each,
counts puncation as part of the word, ignores capitalization.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    max_palindrome = ['']
    for line in read_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if (word == word[::-1]):
                if (word not in max_palindrome):
                    if (len(word) > len(max_palindrome[0])):
                        max_palindrome = [word]
                    elif (len(word) == len(max_palindrome[0])):
                        max_palindrome.append(word)
                    
    return max_palindrome


'''
Returns the number of words in the file that contain all five vowels
A, E, I, O, and U, not necessarily in that order.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_of_words_with_all_vowels = 0
    for line in read_file:
        words = line.split()
        for word in words:
            word = word.lower()
            contains_all_vowels = 1
            for vowel in vowels:
                if (vowel not in word):
                    contains_all_vowels = 0
            number_of_words_with_all_vowels += contains_all_vowels

    return number_of_words_with_all_vowels


'''
Returns the number of lines in the file that contain at least
min_length characters.
    inputs:
        read_file    A file that is open for reading.
        min_length    An integer for the minumum length of the line
'''
def count_long_lines(read_file, min_length):
    greater_lines = 0
    for line in read_file:
        if (len(line) >= min_length):
            greater_lines += 1
            print(line)
    return greater_lines


'''
Returns a random word from the file. Beware of using this with a
very long file.
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(my_file):
    all_words = []
    for line in my_file:
        words = line.split()
        for word in words:
            all_words.append(word)

    return all_words[random.randint(0, len(all_words) - 1)]


'''
Returns a list of num_words random words from the file. Input is
opened file
    inputs:
        read_file    A file that is open for reading.
        num_words    An integer for the number of random wors generated.
'''
def random_words(my_file, num_words):
    
    all_words = []
    for line in my_file:
        words = line.split()
        for word in words:
            all_words.append(word)


    
    list_indexes = []
    for i in range(num_words):
        list_indexes.append(random.randint(1, len(all_words) - 1))

    
    list_of_items = []
    for number in list_indexes:
        list_of_items.append(all_words[number])

    return list_of_items


'''
Returns the number of times the word word appears in the file.
    inputs:
        read_file    A file that is open for reading.
        word    A string
'''
def specific_word_count(read_file, word):
    count = 0
    for line in read_file: 
        words = line.split()
        for sentence_word in words:
            if (sentence_word.lower() == word.lower()):
                count += 1

    return count


'''
Returns the number of words in read_file that begin with the string
word_beginning. Ignores capitalization.
    inputs:
        read_file    A file that is open for reading.
        word_beginning    A string 
'''
def starts_with_counter(read_file, word_beginning):
    word_beginning = word_beginning.lower()
    count = 0
    for line in read_file: 
        words = line.split()
        for word in words:
            word = word.lower()
            if (len(word) >= len(word_beginning)):
                if (word[:len(word_beginning)] == word_beginning):
                    count += 1

    return count
            
    
                
            





def main():
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        print(specific_word_count(my_file, 'I'))


if __name__ == "__main__":
    main()

