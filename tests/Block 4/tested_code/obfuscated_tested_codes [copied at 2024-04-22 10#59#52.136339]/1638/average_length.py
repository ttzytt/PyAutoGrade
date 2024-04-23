


import random
random.seed()

def length(read_file):
    count = 0  
    number_of_words = 0
    for line in read_file:  
        words = line.split()
        for word in words:
            count += len(word)
            number_of_words += 1
    average_length = count / number_of_words        
    return average_length



def longest_word(read_file):
    longest_words = [] 
    length_of_word = 0
    for line in read_file:
        words = line.split()
        for word in words: 
            if len(word) > length_of_word:
                length_of_word = len(word)
                longest_words = [word]
            elif len(word) == length_of_word:
                longest_words.append(word)
            
                
    return longest_words



def longest_palindrome(read_file):
    longest_palindrome = [] 
    length_of_word = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if word == word[::-1]:
                if len(word) > length_of_word:
                    length_of_word = len(word)
                    longest_palindrome = [word]
                elif len(word) == length_of_word:
                    longest_palindrome.append(word)
            
                
    return longest_palindrome



def vowels_counter(read_file):
    vowels_counter = 0 
    for line in read_file:
        words = line.split()
        for word in words:
            if 'a' in word:
                if 'e' in word:
                    if 'i' in word:
                        if 'o' in word:
                            if 'u' in word:
                                vowels_counter = vowels_counter + 1

    return vowels_counter


def count_long_lines(read_file,min_length):
    count_long_lines = 0
    for line in read_file:
        if len(line) >= min_length:
            count_long_lines = count_long_lines + 1


    return count_long_lines



def random_word(read_file):
    the_word = []
    for line in read_file:
        words = line.split()
        the_word += words
    result = random.choice(the_word)

    return result



def specific_word_count(read_file, word):
    count = 0
    for line in read_file:
        words = line.split()
        for word_ in words:
            if word_ == word:
                count += 1

    return count

    



            
        



def main():

    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        average_length = length(my_file)

    print('The file ' + file_name + ' contains ' + str(average_length)
          + ' characters.')
    print()

    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        longest_words = longest_word(my_file)

    print('The file ' + file_name + " 's " + 'longest word(s) is(are) ' + str(longest_words))
    print()


    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        palindrome = longest_palindrome(my_file)

    print('The file ' + file_name + " 's " + 'longest palindrome(s) is(are) ' + str(palindrome))
    print()


    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        vowels = vowels_counter(my_file)

    print('The file ' + file_name + ' contains ' + str(vowels) + ' words that contain all five vowels')
    print()


    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        long_lines = count_long_lines(my_file, 10)

    print('The file ' + file_name + ' contains ' + str(long_lines) + ' lines longer than 10 ')
    print()


    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        random = random_word(my_file)

    print('The word is ' + str(random))
    print()


    file_name = 'Text files/longest_word_test.txt'
    with open(file_name, 'r') as my_file:
        specific = specific_word_count(my_file, 'I')

    print('The count is ' + str(specific))
    print()

if __name__ == "__main__":
    main()


