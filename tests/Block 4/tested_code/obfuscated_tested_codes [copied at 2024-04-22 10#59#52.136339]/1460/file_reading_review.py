


import random

names = 'Text files/names.txt'
green_eggs = 'Text files/greeneggs.txt'
words = 'Text files/words.txt'









def average_length(read_file):

    
    
    
    with open(read_file, 'r') as my_file: 
        my_file_content = my_file.read()
        
    words = my_file_content.split() 
    sum_so_far = 0
    
    for word in words: 
        sum_so_far += len(word)
        
    return sum_so_far/len(words) 






def longest_word(read_file):
    
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
        
    words = my_file_content.split()
    longest_words = []
    max_so_far = 0
    
    for word in words:
        
        if len(word) > max_so_far:
            max_so_far = len(word)
            longest_words = []
        if len(word) == max_so_far and word not in longest_words:
            longest_words.append(word)
            
    return longest_words







def longest_palindrome(read_file, case_sensitive = False):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    longest_words = []
    max_so_far = 0
    for word in words:
        
        if word == word[::-1] or (not case_sensitive and word.lower() == word[::-1].lower()):
            if len(word) > max_so_far: 
                max_so_far = len(word) 
                longest_words = []
            if len(word) == max_so_far and word not in longest_words:
                longest_words.append(word)
    return longest_words







def all_vowels_counter(read_file):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    count = 0
    for word in words:
        
        
        
        if (('e' in word or 'E' in word) and 
            ('a' in word or 'A' in word) and 
            ('i' in word or 'I' in word) and 
            ('o' in word or 'O' in word) and 
            ('u' in word or 'U' in word)):
            count += 1
    return count









def count_long_lines(read_file, min_length):
    with open(read_file, 'r') as my_file:
       my_file_content = my_file.read()
    lines = my_file_content.splitlines()
    count = 0
    for line in lines:
        if len(line) >= min_length:
            count += 1
    return count








def random_word(read_file):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    return words[random.randint(0,len(words)-1)]














def random_words(read_file, num_words):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    
    if num_words > len(set(words)):
        raise(ValueError,
              'num_words should not be greater than the number of distinct words in a given file.')
    chosen_indexes = []
    chosen_words = []
    for _ in range(num_words):
        
        index = random.randint(0,len(words)-1) 
        word = words[index]
        while word.lower() in chosen_words:
            index = random.randint(0,len(words)-1)
            word = words[index]
        chosen_words.append(words[index].lower())
    return chosen_words









def specific_word_count(read_file, word):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    file_words = my_file_content.split()
    count = 0
    for file_word in file_words:
        if word.lower() == file_word.lower():
            count += 1
    return count









def starts_with_counter(read_file, word_beginning):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    file_words = my_file_content.split()
    prefix_length = len(word_beginning)
    count = 0
    for file_word in file_words:
        if word_beginning.lower() == file_word[:prefix_length].lower():
            count += 1
    return count




def main():
    files = ['Text files/addition.txt',
             'Text files/commonwords.txt',
             'Text files/greeneggs.txt',
             'Text files/names.txt',
             'Text files/words.txt']

    
    for i in range(5):
        print("Average Length of", files[i], "is",
              average_length(files[i]))

    
    for i in range(5):
        print("Longest Word of", files[i], "is",
              longest_word(files[i]))

    
    for i in range(5):
        print("Longest Palindrome of", files[i], "is",
              longest_palindrome(files[i]))

    
    for i in range(5):
        print("# of words with aeiou in", files[i], "is",
              all_vowels_counter(files[i]))

    
    for i in range(5):
        print("Lines w/ length > 10 of", files[i], "is",
              count_long_lines(files[i], 10))

    
    for i in range(5):
        print("A random word of", files[i], "is",
              random_word(files[i]))

    
    for i in range(5):
        print("Some random words of", files[i], "is",
              random_words(files[i], 5))

    
    for i in range(5):
        print("Specific word count of 'I' in", files[i], "is",
              specific_word_count(files[i], 'I'))

    
    for i in range(5):
        print("# of words that start with 'a' in", files[i], "is",
              starts_with_counter(files[i], 'a'))

if __name__ == '__main__':
    main()
