


import random

names = 'Text files/names.txt'
green_eggs = 'Text files/greeneggs.txt'
words = 'Text files/words.txt'










def average_length(read_file):

    num_words = 0
    sum_so_far = 0
    for line in read_file:
        words = line.split()
        num_words += len(words)
        for word in words: 
            sum_so_far += len(word)

    if num_words == 0:
        return None
    
    return sum_so_far/num_words








def longest_word(read_file):
        
    longest_words = []
    max_so_far = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if len(word) > max_so_far:
                max_so_far = len(word)
                longest_words = []
            word = word.lower()
            if len(word) == max_so_far and word not in longest_words:
                longest_words.append(word)
                print(word)
            
    return longest_words








def longest_palindrome(read_file, case_sensitive = False):
    longest_words = []
    max_so_far = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            if word == word[::-1] or (not case_sensitive and word.lower() == word[::-1].lower()):
                if len(word) > max_so_far: 
                    max_so_far = len(word) 
                    longest_words = []
                word = word.lower()
                if len(word) == max_so_far and word not in longest_words:
                    longest_words.append(word)
    return longest_words







def all_vowels_counter(read_file):
    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            
            
            if (('e' in word or 'E' in word) and 
                ('a' in word or 'A' in word) and 
                ('i' in word or 'I' in word) and 
                ('o' in word or 'O' in word) and 
                ('u' in word or 'U' in word)):
                count += 1
    return count









def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file:
        if len(line) >= min_length:
            count += 1
    return count








def random_word(read_file):
    words = []
    for line in read_file:
        line_words = line.split()
        words += line_words
    return random.choice(words)
















def random_words(read_file, num_words):
    words = []
    for line in read_file:
        line_words = line.split()
        words += line_words
    
    if num_words >= len(set(words)):
        return None
    chosen_words = []
    for _ in range(num_words):
        
        index = random.randint(0,len(words)-1) 
        word = words[index]
        while word.lower() in chosen_words:
            index = random.randint(0,len(words)-1)
            word = words[index]
        chosen_words.append(word.lower())
    return chosen_words









def specific_word_count(read_file, word):
    count = 0
    for line in read_file:
        line_words = line.split() 
        for line_word in line_words:
            if word.lower() == line_word.lower():
                count += 1
    return count










def starts_with_counter(read_file, word_beginning):
    prefix_length = len(word_beginning)
    count = 0
    for line in read_file:
        line_words = line.split()
        for line_word in line_words:
            if word_beginning.lower() == line_word[:prefix_length].lower():
                count += 1
    return count




def main():

    file_names = ['Text files/addition.txt',
             'Text files/commonwords.txt',
             'Text files/greeneggs.txt',
             'Text files/names.txt',
             'Text files/words.txt']
    
    num_files = len(file_names)

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Average Length of", file_names[i], "is",
                average_length(file))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Longest Word of", file_names[i], "is",
                longest_word(file))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Longest Palindrome of", file_names[i], "is",
                longest_palindrome(file))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("# of words with aeiou in", file_names[i], "is",
                all_vowels_counter(file))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Lines w/ length > 10 of", file_names[i], "is",
                count_long_lines(file, 10))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("A random word of", file_names[i], "is",
                random_word(file))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Some random words of", file_names[i], "is",
                random_words(file, 5))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("Specific word count of 'I' in", file_names[i], "is",
                specific_word_count(file, 'I'))

    
    for i in range(num_files):
        with open(file_names[i], 'r') as file:
            print("# of words that start with 'a' in", file_names[i], "is",
                starts_with_counter(file, 'a'))

if __name__ == '__main__':
    main()
