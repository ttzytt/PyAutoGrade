


import random
random.seed()


'''
Returns the average length of each word in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
    sum_ = 0 
    total_words = 0
    total_sum = 0 
    
    for line in read_file:
        words = line.split() 
        for i in range(len(words)):
            sum_ += len(words[i]) 
        total_words += len(words) 
        total_sum += sum_ 
        sum_ = 0 
        
    return total_sum * 1.00 / total_words 



'''
Returns a list of longest words in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
    lines = read_file.readlines()
    return_list = []
    highest_value = 0 
    
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

'''
Returns a list of the longest palindrome words in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
    return_list = []
    highest_value = 0 
    
    
    
    lines = read_file.readlines() 
    
    
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

'''
Returns 1 or 0.
    inputs:
        word    A string
'''
def whether_word_contain_vowel(word):
    check = 0
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        return 1
    
    return 0


'''
Returns the number of words that contain all five vowels.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
    output = 0
    
    for line in read_file:
        words = line.split()
        for j in range(len(words)):
            
            
            words[j] = words[j].lower()
            output += whether_word_contain_vowel(words[j])
            
            
            
    return output

'''
Returns the number of lines that have a given minimum length.
    inputs:
        read_file    A file that is open for reading.
        min_length   An integer
'''
def count_long_lines(read_file, min_length):
    output = 0
    
    for line in read_file:
        if len(line) >= min_length:
            output += 1
    return output

'''
Returns a random word in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
    full_content = read_file.read() 
    words = full_content.split()
    a = random.randint(0, len(words) -1)
    return words[a]

'''
Returns a list of specific number of random words in the file.
    inputs:
        read_file    A file that is open for reading.
        num_words    An integer
'''
def random_words(read_file, num_words):
    full_content = read_file.read()
    words = full_content.split()
    random.shuffle(words)
    return words[:num_words]

'''
Returns the number of times that a specific word appears in the file.
    inputs:
        read_file    A file that is open for reading.
        word         A string
'''
def specific_word_count(read_file, word):
    output = 0
    for line in read_file:
        words = line.split()
        for i in range(len(words)):
            if words[i] == word:
                output += 1
    return output

'''
Returns the number of times that a specific word appears in the file.
    inputs:
        read_file    A file that is open for reading.
        word_beginning     A string.
'''
def starts_with_counter(read_file, word_beginning):
    output = 0
    for line in read_file:
        words = line.split()
        for i in range(len(words)):
            
            if words[i][:len(word_beginning)] == word_beginning:
                output += 1
    return output


def main():
    
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        output = specific_word_count(my_file, "I")

    print(output)

if __name__ == "__main__":
    main()


