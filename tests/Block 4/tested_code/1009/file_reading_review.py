



import random
'''
Returns the average length for the file, as a string.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    total_length = 0 
    total_words = 0 
    
    
    
    
    
    for line in read_file:
        words = line.split() 
        total_words += len(words) 

    
        for word in words:
            total_length += len(word)

    average = total_length / total_words
    return average
       

'''
Returns the longest word(s) in the file, as a list of strings.
    inputs:
        read_file    A file that is open for reading.
''' 
def longest_word(read_file):
    longest_length = 0
    longest_word = []

    for line in read_file:
        words = line.split()

        for word in words:
            word_length = len(word)
            
            if word_length > longest_length:
                longest_length = word_length
                longest_word = [word]
            
            elif word_length == longest_length:
                longest_word.append(word)

    return longest_word

'''
Returns the longest palindrome word(s), as a list of strings.
    inputs:
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
            if is_palindrome(word):  
                word_length = len(word)
                
                if word_length > max_length:
                    max_length = word_length
                    longest_palindromes = [word]
                elif word_length == max_length:
                    longest_palindromes.append(word)
    
    return longest_palindromes

'''
Returns the number of words that contains all five vowels, as a string.
    inputs:
        read_file    A file that is open for reading.
''' 
def all_vowels_counter(read_file):
    vowels = 'aeiou'  
    count = 0  
    
    
    for line in read_file:
        words = line.split()
        
        for word in words:
            has_all_vowels = True
            
            for vowel in vowels:
                if vowel not in word:
                    
                    has_all_vowels = False
                    break
            if has_all_vowels:
                
                count += 1
    return count

'''
Returns the number of lines that contain at least min_length of character
(only include alphabet letter), as a string.
    inputs:
        read_file    A file that is open for reading.
''' 
def count_long_lines(read_file, min_length):
    count = 0
    
    
    for line in read_file:
        length = len(line)  

        for char in line:
            if char.isalpha():  
                
                length += 1
                
        
        if length >= min_length: 
            count += 1
    
    return count

'''
Returns a random word in the file, as a list of strings.
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    
    words = read_file.read().split()
   
    
    return random.choice(words)

'''
Returns a list of num_words random words in the file, as a list of strings.
    inputs:
        read_file    A file that is open for reading.
'''
def random_words(read_file, num_words):
    
    words = read_file.read().split()
    num_words = int(input("How many words do you want: "))
    
    
    
    return random.sample(words, num_words)


'''
Returns the number of times a word appears in the file, as a strings.
    inputs:
        read_file    A file that is open for reading.
'''
def specific_word_count(read_file, word):
    count = 0
    
   
    for line in read_file:
        
        words = line.split()

        for w in words:
            
            if w == word:
                
                count += 1
    
    return count

'''
Returns the number of word that started with word_begining, as a string.
    inputs:
        read_file    A file that is open for reading.
'''
def starts_with_counter(read_file, word_beginning):
    count = 0
    
    for line in read_file:
        words = line.split()
        
        for w in words:
            
            if w.startswith(word_beginning):
                count += 1
    
    return count

def main():
    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        average = average_length(my_file)

    print('The file ' + file_name + ' has an average length of ' + str(average)
          + '.')
    print()

    
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        longest = longest_word(my_file)

    print('The longest word(s) in the file ' + file_name + ' is/are:')
    for word in longest:
        print(word)
    print()

    
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        palindromes = longest_palindrome(my_file)

    print("Longest palindrome word(s) in the file"+ file_name + ' is/are:')
    for word in palindromes:
        print(word)
    print()

    
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as file:
         num_words = all_vowels_counter(file)
         print("Number of words containing all vowels:", num_words)
    print()

    
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as file:
        min_length = 10  
        num_lines = count_long_lines(file, min_length)
        print("Number of lines containing at least", min_length, "characters:", num_lines)
    print()

    
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as file:
        random_word_value = random_word(file)
        print("Random word:", random_word_value)

    
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as file:
        num_words = int(input("How many words do you want: "))
        random_word_list = random_words(file, num_words)
        print("Random words:", random_word_list)


    
    
    
    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as file:
        word_count = specific_word_count(file, word)
        print(f"The word '{word}' appears {word_count} times in the file.")
    print()

    
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as file:
        word_beginning = 'as'
        word_counting = starts_with_counter(file, word_beginning)
    print(f"There are {word_counting} words in the file begin with '{word_beginning}'.")

if __name__ == "__main__":
    main()
