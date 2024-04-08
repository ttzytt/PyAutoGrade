
import random
random.seed()


def average_length(read_file):
    file_data = []
    sum_ = 0 
    total_words = 0
    total_sum = 0 
    lines = read_file.splitlines() 
    
    for i in range(len(lines)):
        words = lines[i].split() 
        for i in range(len(words)):
            sum_ += len(words[i]) 
        total_words += len(words) 
        total_sum += sum_ 
        sum_ = 0 
        
    return total_sum * 1.00 / total_words

def longest_word(read_file):
    return_list = []
    highest_value = 0 
    lines = read_file.splitlines()
    
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if len(words[j]) > highest_value:
                highest_value = len(words[j]) 
                
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if len(words[j]) == highest_value:
                return_list.append(words[j]) 
                
    return return_list

def longest_palindrome(read_file):
    return_list = []
    highest_value = 0 
    lines = read_file.splitlines()
    
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if len(words[j]) > highest_value and words[j] == words[j][::-1]:
                highest_value = len(words[j]) 
                
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if len(words[j]) == highest_value and words[j] == words[j][::-1]:
                return_list.append(words[j]) 

    return return_list

def whether_word_contain_vowel(word):
    check = 0
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        return 1
    
    return 0

def all_vowels_counter(read_file):
    output = 0
    
    lines = read_file.splitlines()
    
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            words[j] = words[j].lower()
            output += whether_word_contain_vowel(words[j])
            if whether_word_contain_vowel(words[j])==1:
                print(words[j])
    return output

def count_long_lines(read_file, min_length):
    output = 0
    lines = read_file.splitlines()
    
    for i in range(len(lines)):
        if len(lines[i]) >= min_length:
            output += 1
    return output

def random_word(read_file):
    words = read_file.split()
    a = random.randint(0, len(words) -1)
    return words[a]

file_name = 'Text files/greeneggs.txt'
my_file = open(file_name, 'r')

full_content = my_file.read()
print(random_word(full_content))

my_file.close()

