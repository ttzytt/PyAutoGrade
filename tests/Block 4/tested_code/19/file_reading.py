


import random


def average_length(read_file):

    num_words = 0
    word_count = 0

    for line in file:

        
        word_list = line.split()
        
        for word in word_list:
            word_count += len(word)
            num_words += 1

    return word_count/num_words




def find_longest_word(read_file):

    longest_word = [file.readline().split()[1]]

    for line in file:
        
        word_list = line.split()
        for i in range(len(word_list)):
            
            if len(word_list[i]) > len(longest_word[0]):
                longest_word = [word_list[i]]
            elif len(word_list[i]) == len(longest_word[0]):
                longest_word.append(word_list[i])

    return longest_word




def find_longest_palindrome(file):

    
    longest_palindrome = [file.readline().split()[1]]

    for line in file:
        
        word_list = line.split()
        for i in range(len(word_list)):
            

            if word_list[i][::-1] == word_list[i]:
                if len(word_list[i]) > len(longest_palindrome[0]):
                    longest_palindrome = [word_list[i]]
                elif len(word_list[i]) == len(longest_palindrome[0]):
                    longest_palindrome.append(word_list[i])

    if longest_palindrome[::-1] == longest_palindrome:
        return longest_palindrome
    
    else:
        return None





def all_vowels_counter(file):
    counter = 0

    for line  in file:
        line = line.lower()
        word_list = line.split()
        for word in word_list:

            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
                counter += 1
                
    return counter

 



def count_long_lines(file, min_length):
    counter = 0

    for line in file:
        if len(line) > min_length:
            counter += 1

    return counter




def random_word(file):
    
    line_list = file.readlines()
    
    line = line_list[random.randint(0, (len(line_list) - 1))]
    
    return line.split()[random.randint(0, (len(line.split()) - 1))]



def random_words(file, num_words):
    
    
    word_list = []

    line_list = file.readlines()

    for i in range(num_words):
        
        
        
        
        
        line = line_list[random.randint(0, (len(line_list) - 1))]
        
        word_list.append(line.split()[random.randint(0, (len(line.split()) - 1))])

    return word_list



def specific_word_count(file, specific_word):

    specific_word_count = 0
    
    specific_word.lower()

    
    for line in file:
        
        line = line.lower()
        word_list = line.split()

        
        for word in word_list:
            
            if word == specific_word:
                specific_word_count += 1

    return specific_word_count



def starts_with_counter(file, start_of_word):

    starts_with_count = 0

    start_of_word.lower()

    for line in file:
        line = line.lower()
        
        word_list = line.split()

        for word in word_list:
            if word[:len(start_of_word)] == start_of_word:
                starts_with_count += 1

    return starts_with_count


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as file:
    longest_word = find_longest_word(file)

print('The longest word in ' + file_name + ' is(are) ' + str(longest_word))
print()

file_name = 'Text files/average_len.txt'
with open(file_name, 'r') as file:
    average_length = average_length(file)

print('The average word lenght in ' + file_name + ' is ' + str(average_length))
print()

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as file:
    all_vowels_counter = all_vowels_counter(file)

print('The number of words with all vowels in ' + file_name + ' is ' + str(all_vowels_counter))
print()

min_length = 24
file_name = 'Text files/long_lines.txt'
with open(file_name, 'r') as file:
    num_long_lines = count_long_lines(file, min_length)

print('There are ' + str(num_long_lines) + ' long lines in ' + file_name)
print()

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as file:
    the_random_word = random_word(file)

print(the_random_word + ' exists in ' + file_name)
print()


file_name = 'Text files/greeneggs.txt'
num_words = 5
with open(file_name, 'r') as file:
    random_words = random_words(file, num_words)

print('These words: ' + str(random_words) + ' all exist in ' + file_name)
print()

file_name = 'Text files/specific_word.txt'
specific_word = 'david'
with open(file_name, 'r') as file:
    num_specific_words = specific_word_count(file, specific_word)

print('The number of ocurrences of ' + str(specific_word) + ' in ' + file_name + ' is ' + str(num_specific_words))
print()

file_name = 'Text files/word_start.txt'
start_of_word = 'start'
with open(file_name, 'r') as file:
    num_start_words = starts_with_counter(file, start_of_word)

print('The number of ocurrences of ' + start_of_word + ' at the start of a word in ' + file_name + ' is ' + str(num_start_words))
print()
