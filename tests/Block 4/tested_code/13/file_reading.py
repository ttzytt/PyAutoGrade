
import random
file_name = 'Text files/names.txt'


my_file = open(file_name, 'r')



full_content = my_file.read()


def average_length(read_file):
    total_length = 0
    total_words = 0
    for line in read_file:
        words = line.split()  
        total_length += sum(len(word) for word in words)  
        total_words += len(words)  
    return total_length / total_words if total_words > 0 else 0

with open(file_name, 'r') as my_file:
    average_length_output = average_length(my_file)
print(str(average_length_output))

def longest_word(read_file):
    longest_words = []
    max_length = 0
    for line in read_file:
        words = line.split()
        for word in words:
            word = word.strip(",.!?")  
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length:
                longest_words.append(word)
    return longest_words

with open(file_name, 'r') as my_file:
    longest_word_output = longest_word(my_file)
print(str(longest_word_output))



def longest_palindrome(read_file):
    def is_palindrome(word):
        return word == word[::-1]  

    longest_palindromes = []
    max_length = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if is_palindrome(word) and len(word) > max_length:
                max_length = len(word)
                longest_palindromes = [word]
            elif is_palindrome(word) and len(word) == max_length:
                longest_palindromes.append(word)
    return longest_palindromes





def all_vowels_counter(read_file):
    def has_all_vowels(word):
        vowels = set('aeiouAEIOU')
        return vowels.issubset(set(word))

    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if has_all_vowels(word):
                count += 1
    return count

with open(file_name, 'r') as my_file:
    all_vowels_counter = all_vowels_counter(my_file)
print(str(all_vowels_counter))
print()



def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file:
        if len(line) >= min_length:
            count += 1
    return count




file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    average_length_output = average_length(my_file)
print(str(average_length_output))


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    longest_word_output = longest_word(my_file)
print(str(longest_word_output))


file_name = 'Text files/test_for_palindrome.txt'
with open(file_name, 'r') as my_file:
    longest_palindrome = longest_palindrome(my_file)
print(str(longest_palindrome))
print()


with open(file_name, 'r') as my_file:
    all_vowels_counter = all_vowels_counter(my_file)
print(str(all_vowels_counter))
print()


with open(file_name, 'r') as my_file:
    count_long_lines = count_long_lines(my_file)
print(str(count_long_lines))
print()
