





import random

random.seed()





'''
Returns the the average length of all the words in the file.
    inputs:
        read_file    A file that is open for reading.
'''


def average_length(read_file):
    words = read_file.read().split() 
    word_lengths = [len(word) for word in words] 
    if len(word_lengths) > 0:
        return sum(word_lengths) / len(word_lengths) 
    else:
        return 0  

'''
Returns the list of words in the file and keep every words if there is a tie.
    inputs:
        read_file    A file that is open for reading.
'''

def longest_word(read_file):
    words_list = []
    highest_length = 0 
    words = read_file.read().split() 
    for word in words:
        word = word.lower() 
        if len(word) > highest_length: 
            highest_length = len(word) 
            words_list.clear() 
            words_list.append(word) 
        elif len(word) == highest_length: 
            if word not in words_list:
                words_list.append(word) 
    return words_list           

'''
Returns the longest word in the file that is palindrom.
    inputs:
        read_file    A file that is open for reading.
'''


def longest_palindrome(read_file):
    words_list = []
    highest_length = 0 
    words = read_file.read().split() 
    for word in words:
        word = word.lower() 
        
        if word[::-1] == word[::]:
            if len(word) > highest_length: 
                highest_length = len(word) 
                words_list.clear() 
                words_list.append(word) 
            elif len(word) == highest_length: 
                if word not in words_list: 
                    words_list.append(word) 
    return words_list           


'''
Return all the number of words contain all five vowels A,E,I,O,U.
    inputs:
        read_file    A file that is open for reading.
'''


def all_vowels_counter(read_file):
    words_list = []
    vowels_in_word = []
    words = read_file.read().split() 
    for word in words:
        for i in range(len(word)):
            if word[i].lower() == 'a' and 'a' not in vowels_in_word:
                vowels_in_word.append(word[i].lower())
            elif word[i].lower() == 'e' and 'e' not in vowels_in_word:
                vowels_in_word.append(word[i].lower())
            elif word[i].lower() == 'i' and 'i' not in vowels_in_word:
                vowels_in_word.append(word[i].lower())
            elif word[i].lower() == 'o' and 'o' not in vowels_in_word:
                vowels_in_word.append(word[i].lower())
            elif word[i].lower() == 'u' and 'u' not in vowels_in_word:
                vowels_in_word.append(word[i].lower())
        vowels_in_word.sort()
        

        if vowels_in_word == ['a','e','i','o','u']:
            words_list.append(word)
            
        vowels_in_word.clear()
    return len(words_list)
       
'''
Returns the number of lines that contain at least min_length characters.
    inputs:
        read_file    A file that is open for reading.
'''

def count_long_lines(read_file, min_length):
    length = 0
    lines = read_file.readlines()
    
    for line in lines:
        if len(line) >= min_length:
            length += 1
            
    return length


'''
Returns a random word from the file. 
    inputs:
        read_file    A file that is open for reading.
'''

def random_word(read_file):
    with open(read_file, 'r') as my_file:
        words = my_file.read().split()
        
        word = random.choice(words)
    return word

'''
Returns a random word from the file and store them into a list. 
    inputs:
        read_file    A file that is open for reading.
'''

def random_words(read_file, num_words):
    words = read_file.read()
    word = words.split()
    num_words = min(num_words, len(word))
    
    random_selection = random.sample(word, num_words)
    return random_selection



'''
Returns the number of times a word appears in the filer. 
    inputs:
        read_file    A file that is open for reading.
'''

def specific_word_count(read_file, word):
    lines = read_file.read()
    words = lines.split()
    
    word_count = words.count(word)
    return word_count


'''
Returns the number of words in read_file that begin with the string
word_beginning. 
    inputs:
        read_file    A file that is open for reading.
'''

def starts_with_counter(read_file, word_beginning):
    times = 0
    lines = read_file.read()
    words = lines.split()
    for word in words: 
        if word[:len(word_beginning)].lower() == word_beginning.lower():
            times += 1
    
    return times



def main():
    
    

    
    print('T2 begins: ')

    read_file = "Text files/names.txt" 
    with open(read_file, 'r') as my_file:
        average_words_length = average_length(my_file) 
    if average_words_length is not None: 
        print("Average word length:" + str(round(average_words_length*100)/100) + ' in ' + read_file)        
    print()

    
    print('T3 begins: ')
    read_file = "Text files/greeneggs.txt" 
    with open(read_file, 'r') as my_file:
        longest = longest_word(my_file)
    print('The longest words are: ' + str(longest))
    print()

    
    print('T4 begins: ')

    read_file = "Text files/greeneggs.txt" 
    with open(read_file, 'r') as my_file:
        palindrome = longest_palindrome(my_file)
    print('The longest palindrome are: ' + str(palindrome))
    print()

    
    print('T5 begins: ')

    read_file = "Text files/words.txt" 
    with open(read_file, 'r') as my_file:
        all_vowels = all_vowels_counter(read_file)
    print('The words contain all five vowels are: ' + str(all_vowels))
    print()

    
    print('T6 begins: ')

    min_length = 1
    read_file = "Text files/names.txt" 
    with open(read_file, 'r') as my_file:
        number_of_lines = count_long_lines(read_file, min_length)
    print('The number of lines longer than min_length is: ' + str(number_of_lines))
    print()

    
    print('T7 begins: ')

    read_file = "Text files/vowels.txt" 
    random_words_for_t7 = random_word(read_file)
    print('The word randomly chose in ' + read_file +' is: ' + random_words_for_t7)
    print()

    
    print('T8 begins: ')

    file_name = 'Text files/words.txt'  
    num_words = 18  
    with open(file_name, 'r') as my_file:
        random_word_list = random_words(my_file, num_words)
    print(str(random_word_list))
    print()

    
    print('T9 begins: ')

    file_name = 'Text files/names.txt'  
    search_word = 'Maggie'
    with open(file_name, 'r') as my_file:
        times = specific_word_count(my_file, search_word)
    print("The specific word appears " + str(times) + " times in the file.")
    print()

    
    print('T10 begins: ')

    file_name = 'Text files/greeneggs.txt'  
    word_beginning = 'r'  

    with open(file_name, 'r') as my_file:
        count = starts_with_counter(my_file, word_beginning)
    print("The number of words in the file that begin with "
           + word_beginning + " is: " + str(count))
    print()

if __name__ == "__main__":
    main()












