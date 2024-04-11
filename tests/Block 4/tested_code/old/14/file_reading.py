


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
    print(lines)
    count = 0
    for line in lines:
        if len(line) >= min_length:
            count += 1
            print(line)
    return count


def random_word(read_file):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    return words[random.randint(0,len(words)-1)]


exec("def random_word_ONE_LINER(عصير):\n جمالي = {}\n with open(عصير, 'r') as my_file:\n \t if True:\n \t \t جمالي['سخافة'] = my_file.read()\n جمالي['يتبرّز'] = جمالي['سخافة'].split()\n عصير = 'اللہ کے نام کے ساتھ جو بے انتہا رحم کرنے والا، بِن مانگے دینے والا (اور) بار بار رحم کرنے والا ہے۔'\n عصير_الموز = جمالي['يتبرّز'][random.randint(0,len(جمالي['يتبرّز'])-1)]\n return عصير_الموز")
print(random_word_ONE_LINER(green_eggs))

def random_words(read_file, num_words):
    with open(read_file, 'r') as my_file:
        my_file_content = my_file.read()
    words = my_file_content.split()
    
    if num_words > len(words):
        raise(ValueError, "num_words should not be greater than the number of words in a given file.")
    chosen_indexes = []
    chosen_words = []
    for _ in range(num_words):
        index = random.randint(0,len(words)-1)
        while index in chosen_indexes:
            index = random.randint(0,len(words)-1)
        chosen_words.append(words[index])
    return chosen_words

print(random_words(green_eggs,10))



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

        
print("bzzzzzz ", average_length(green_eggs))
print(longest_word(green_eggs))
print(longest_word(words))
print("basashoad", longest_palindrome(words), False)
print(all_vowels_counter(words))
print(count_long_lines(green_eggs, 10))
print(specific_word_count(green_eggs, 'sam-i-am'))
assert False



def TEST(expected_result, actual_result):
    return expected_result == actual_result

test_triplets
for test_triplet in test_triplets:
    pass
print("same length words: ", TEST())
print("punctuation: ", TEST())


