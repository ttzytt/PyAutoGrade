 



import random


def average_length(read_file):
    
    total_length = 0
    words_read = 0
    
    for line in read_file:
        words = line.split()
        for word in words: 
            total_length += len(word) 
            words_read += 1
            
    return total_length/words_read 


def longest_word(read_file):
    current_longest_word = '' 
    
    for line in read_file:
        words = line.split()
        for word in words: 

            
            if len(word) > len(current_longest_word):
                current_longest_word = word
                
    return current_longest_word




def longest_palindrome(read_file):
    current_longest_palindrome = ''
    for line in read_file:
        words = line.split()
        for word in words:
            if word.lower() == word[::-1].lower(): 
                if len(word) > len(current_longest_palindrome):
                    current_longest_palindrome = word
    return current_longest_palindrome


def all_vowels_counter(read_file):
    
    vowels_count = 0 
    
    
    for line in read_file:
        words = line.split()
        for word in words: 
            word = word.lower()
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
                vowels_count += 1
    return vowels_count  


def count_long_lines(read_file, min_length):
    long_line_count = 0 
    
    for line in read_file: 
        
        if len(line) >= min_length:
            long_line_count += 1 
                                 
    return long_line_count


def random_word(read_file):
    random_words = [] 
    for line in read_file:
        words = line.split() 
        random_word = random.choice(words)
        random_words.append(random_word) 

    final_random_word = random.choice(random_words) 
    
    return final_random_word
 


def random_words(read_file, num_words):
    random_words = [] 
    final_random_words = [] 
    for line in read_file:
        words = line.split() 
        random_word = random.choice(words)
        random_words.append(random_word) 
        
    i = 0
    while i < num_words: 
                         
        final_random_word = random.choice(random_words)
        final_random_words.append(final_random_word) 
        i += 1 

    return final_random_words 


def specific_word_count(read_file, word):
    
    specific_word = word 
    
    specific_word_count = 0 
    
    for line in read_file:
        words = line.split()
        
        for word in words: 
            
            
            if word == specific_word:
                specific_word_count += 1 
            
    return specific_word_count 


def starts_with_counter(read_file, word_beginning):
    starts_with_counter = 0 
    word_beginning = word_beginning.lower() 
    for line in read_file:
        words = line.split()
        
        for word in words:
            word = word.lower() 

            
            if word[:len(word_beginning)] == word_beginning:
                starts_with_counter += 1
    return starts_with_counter


def main():


    file_name_AL = 'Text files/names.txt' 
    with open(file_name_AL, 'r') as my_file:
        average_length_result = average_length(my_file)
        
    file_name_LW = 'Text files/names.txt' 
    with open(file_name_LW, 'r') as my_file:
        longest_word_result = longest_word(my_file)

    file_name_LP = 'Text files/words.txt' 
    with open(file_name_LP, 'r') as my_file:
        longest_palindrome_result = longest_palindrome(my_file)

    file_name_VC = 'Text files/words.txt' 
    with open(file_name_VC, 'r') as my_file:
        vowel_count_result = all_vowels_counter(my_file)

    file_name_CLL = 'Text files/names.txt' 
    with open(file_name_CLL, 'r') as my_file:
        long_line_count_result = count_long_lines(my_file, 10)

    file_name_RW = 'Text files/names.txt' 
    with open(file_name_RW, 'r') as my_file:
        random_word_result = random_word(my_file)

    file_name_RWs = 'Text files/names.txt' 
    with open(file_name_RWs, 'r') as my_file:
        random_word_results = random_words(my_file, 5)

    file_name_SWC = 'Text files/words.txt' 
    with open(file_name_SWC, 'r') as my_file:
        specific_word_results = specific_word_count(my_file, 'word')

    file_name_SW = 'Text files/names.txt' 
    with open(file_name_SW, 'r') as my_file:
        starts_with_results = starts_with_counter(my_file, 'a')



    
    print('The average length of a word in the file ' + file_name_AL + ' is ' +
          str(round(average_length_result)))

    print('The longest word in the file ' + file_name_LW + " is '" + str(longest_word_result) + "'")

    print('The longest palindrome in the file ' + file_name_LP + " is '" +
          str(longest_palindrome_result))

    print('The number of words with all 5 vowels in the file ' + file_name_VC + " is "
          + str(vowel_count_result))

    print('The number of lines with more than 10 characters in the file ' + file_name_CLL +
          'is ' + str(long_line_count_result))

    print('A random word from the file ' + file_name_RW + "is '" + random_word_result + "'")

    print('5 random words from the file ' + file_name_RWs + " are '" +
          "', '".join(random_word_results) + "'")

    print("The amount of times the word 'word' showed up in the file  " + file_name_SWC +
          " is " + str(specific_word_results))

    print("The number of words starting with 'a' in the file " + file_name_SW + 
          " is " + str(starts_with_results))

if __name__ == "__main__":
    main()

