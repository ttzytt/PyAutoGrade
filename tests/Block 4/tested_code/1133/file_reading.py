




import random


'''
T2
Returns the average length of all the words in the file by dividing total length by total words.
read_file    A file that is open for reading.
'''
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


'''
T3
Returns the list of longest word(s) in the file.
    inputs
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    longest_words = []  
    max_length = 0      
    for line in read_file:
        words = line.split()
        for word in words:
            word_length = len(word)
            if word_length > max_length:
                longest_words = [word.lower()]  
                max_length = word_length  
            elif word_length == max_length:
                longest_words.append(word.lower())  
    return longest_words



'''
T4
Returns the list of longest palindrome word(s) in the file.
    inputs
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    def is_palindrome(word):
        return word == word[::-1]  

    longest_palindromes = []  
    max_length = 0            
    for line in read_file:
        words = line.split()
        for word in words:
            word_lower = word.lower()  
            if is_palindrome(word_lower):
                word_length = len(word)
                if word_length > max_length:
                    longest_palindromes = [word_lower]  
                    max_length = word_length  
                elif word_length == max_length:
                    if word_lower not in longest_palindromes:
                        longest_palindromes.append(word_lower)  
    return longest_palindromes

'''
T5
Returns the number of words in the file that contain all five vowels.
    inputs
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    vowels = set('aeiou')  
    count = 0              
    for line in read_file:
        words = line.split()
        for word in words:
            if vowels.issubset(set(word.lower())): 
                count += 1  
    return count

'''
T6 
Returns the number of lines in the file that contain at least min_length characters.
    inputs
        read_file    A file that is open for reading.
'''
def count_long_lines(read_file, min_length):
    count = 0  
    for line in read_file:
        if len(line) >= min_length:
            count += 1  
    return count

'''
T7
Returns a random word from the file.
    inputs
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    words = []  
    for line in read_file:
        words.extend(line.split()) 
    return random.choice(words)  

'''
T8
Returns a list of num_words random words from the file.
    inputs
        read_file    A file that is open for reading.
        num_words    
'''
def random_words(read_file, num_words):
    words = []  
    for line in read_file:
        words.extend(line.split())
    return random.sample(words, num_words)  
'''
T9
Returns the number of times the specified word appears in the file.
    inputs
    
'''
def specific_word_count(read_file, word):
    count = 0  
    for line in read_file:
        count += line.lower().count(word.lower())  
    return count

'''
Returns the number of words in the file that begin with the specified string.
    inputs:
        read_file        
        word_beginning    The string that words should start with.
'''
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
        my_file.seek(0)  
        print("Longest word(s):", longest_word(my_file))

    
    file_name = 'Text files/test_for_palindrome.txt'
    with open(file_name, 'r') as my_file:
        print("Longest palindrome word(s):", longest_palindrome(my_file))
        my_file.seek(0)  
        print("Number of words containing all vowels:", all_vowels_counter(my_file))
        my_file.seek(0)  
        print("Number of lines with at least 10 characters:", count_long_lines(my_file, 10))
        my_file.seek(0)  
        print("Random word:", random_word(my_file))
        my_file.seek(0)  
        print("Random words:", random_words(my_file, 5))
        my_file.seek(0)  
        print("Occurrences of 'the':", specific_word_count(my_file, 'the'))
        my_file.seek(0)  
        print("Number of words starting with 'a':", starts_with_counter(my_file, 'a'))

if __name__ == "__main__":
    main()
