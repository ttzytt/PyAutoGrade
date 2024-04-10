





def average_length(read_file):
    number_of_words = 0   
    length = 0
    for line in read_file:  
        words = line.split()
        for word in words:
            number_of_words += 1
            length += len(word)
        
    return (length/number_of_words)




def longest_word(read_file):
    longest_words = ['']
    for line in read_file: 
        words = line.split()
        for word in words:
            if len(word) > len(longest_words[0]): 
                longest_words = [word]
            elif len(word) == len(longest_words[0]): 
                if word not in longest_words:
                    longest_words.append(word)
    return longest_words




def longest_palindrome(read_file):
    longest_palindrome = ['']
    for line in read_file: 
        words = line.split()
        for word in words:
            if word == word[::-1]: 
                if len(word) > len(longest_palindrome[0]): 
                    longest_palindrome = [word]
                elif len(word) == len(longest_palindrome[0]): 
                    if word not in longest_palindrome:
                        longest_palindrome.append(word)

    return longest_palindrome




def all_vowels_counter(read_file):
    all_vowels_counter = 0
    for line in read_file: 
        words = line.split() 
        for word in words:
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word): 
                all_vowels_counter += 1 
    return all_vowels_counter




def count_long_lines(read_file, min_length):
    num_long_line = 0
    for line in read_file:
        if line[-1] == '\n': 
            line = line[:-1]
        if len(line) > min_length: 
            num_long_line += 1
    return num_long_line




def random_word(read_file):
    bag_of_words = []
    import random
    for line in read_file:
        words = line.split()
        for word in words:
            bag_of_words.append(word) 
    random_word = random.choice(bag_of_words) 
    return random_word




def random_words(read_file, num_words):
    bag_of_words = []
    random_word = []
    import random
    for line in read_file:
        words = line.split()
        for word in words:
            bag_of_words.append(word) 
    for _ in range(num_words):
        random_word.append(random.choice(bag_of_words)) 
    return random_word




def specific_word_count(read_file, word):
    word_count = 0
    for line in read_file:
        words = line.split()
        for thing in words:
            if thing == word:
                word_count += 1
    return word_count




def starts_with_counter(read_file, word_beginning):
    word_counter = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if line[0] == word_beginning:
                word_counter += 1
    return word_counter




def main():

    file_name = 'Text files/greeneggs.txt'
    min


    with open(file_name, 'r') as my_file:
        num_characters = average_length(my_file)

    print('The average of ' + file_name + ' is ' + str(num_characters)
          + ' words.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = longest_word(my_file)

    print('The longest words of ' + file_name + ' are ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = longest_palindrome(my_file)

    print('The longest palindromes of ' + file_name + ' are ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = all_vowels_counter(my_file)

    print('The words that contain all the vowels of ' + file_name + ' are ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = count_long_lines(my_file, 5)

    print('The number of long lines of ' + file_name + ' is ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = random_word(my_file)

    print('The random word of ' + file_name + ' is ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = random_words(my_file, 7)

    print('The list of random words of ' + file_name + ' is ' + str(num_characters)
          + '.')
    print()



    with open(file_name, 'r') as my_file:
        num_characters = specific_word_count(my_file, 'eggs')

    print('The the number of words eggs in ' + file_name + ' is ' + str(num_characters)
          + '.')
    print()



    
    with open(file_name, 'r') as my_file:
        num_characters = starts_with_counter(my_file, 'I')

    print('The the number of lines starting with I in ' + file_name + ' is ' + str(num_characters)
          + '.')
    print()


    
if __name__ == "__main__":
    main()
