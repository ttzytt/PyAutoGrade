




import random



def average_length(read_file):
    total_length = 0  
    total_words = 0   
    for line in read_file:
        words = line.split()
        total_length += sum(len(word) for word in words)  
        total_words += len(words)  
    if total_words == 0:
        return 0  
    return total_length / total_words  


def longest_word(read_file):
    longest_words = []  
    max_length = 0      
    for line in read_file:
        words = line.split()
        for word in words:
            word_length = len(word)
            if word_length > max_length:
                longest_words = [word]  
                max_length = word_length  
            elif word_length == max_length:
                longest_words.append(word)  
    return longest_words


def longest_palindrome(read_file): 
    def is_palindrome(word):
        return word == word[::-1]  

    longest_palindromes = []  
    max_length = 0            
    for line in read_file:
        words = line.split()
        for word in words:
            if is_palindrome(word):
                word_length = len(word)
                if word_length > max_length:
                    longest_palindromes = [word]  
                    max_length = word_length      
                elif word_length == max_length:
                    longest_palindromes.append(word)  
    return longest_palindromes


def all_vowels_counter(read_file):
    vowels = set('aeiou')  
    count = 0              
    for line in read_file:
        words = line.split()
        for word in words:
            if vowels.issubset(set(word.lower())): 
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
        words.extend(line.split()) 
    return random.choice(words)  


def random_words(read_file, num_words):
    words = []  
    for line in read_file:
        words.extend(line.split())
        return random.sample(words, num_words)  


def specific_word_count(read_file, word):
    count = 0  
    for line in read_file:
        count += line.lower().count(word.lower())  
    return count


def starts_with_counter(read_file, word_beginning):
    count = 0  
    for line in read_file:
        words = line.split()
        for word in words:
            if word.lower().startswith(word_beginning.lower()):
                count += 1  
    return count



def main():

    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        print("Average word length:", average_length(my_file))

    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        print("Longest word(s):", longest_word(my_file))

    file_name = 'Text files/test_for_palindrome.txt'
    with open(file_name, 'r') as my_file:
        print("Longest palindrome word(s):", longest_palindrome(my_file))
    with open(file_name, 'r') as my_file:
        print("Number of words containing all vowels:", all_vowels_counter(my_file))

    with open(file_name, 'r') as my_file:
        print("Number of lines with at least 10 characters:", count_long_lines(my_file, 10))

    with open(file_name, 'r') as my_file:
        print("Random word:", random_word(my_file))

    with open(file_name, 'r') as my_file:
        print("Random words:", random_words(my_file, 5))

    with open(file_name, 'r') as my_file:
        print("Occurrences of 'the':", specific_word_count(my_file, 'the'))

    with open(file_name, 'r') as my_file:
        print("Number of words starting with 'a':", starts_with_counter(my_file, 'a'))


if __name__ == "__main__":
    main()

