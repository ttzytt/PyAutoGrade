



def average_length(read_file):
    number_of_words = 0   
    length = 0
    for line in my_file:  
        words = line.split()
        for word in words:
            number_of_words += 1
            length += len(word)
        
    return (length/number_of_words)




def longest_word(read_file):
    longest_words = ['']
    for line in my_file: 
        words = line.split()
        for word in words:
            if len(word) > len(longest_words[0]): 
                longest_words = [word]
            elif len(word) == len(longest_words[0]): 
                longest_words.append(word)

    return longest_words




def longest_palindrome(read_file):
    longest_palindrome = ['']
    for line in my_file: 
        words = line.split()
        for word in words:
            if word == word[::-1]: 
                if len(word) > len(longest_palindrome[0]): 
                    longest_palindrome = [word]
                elif len(word) == len(longest_palindrome[0]): 
                    longest_palindrome.append(word)

    return longest_palindrome




def all_vowels_counter(read_file):
    all_vowels_counter = 0
    for line in my_file: 
        words = line.split() 
        for word in words:
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word: 
                all_vowels_counter += 1 
    return all_vowels_counter




def count_long_lines(read_file, min_length):
    


file_name = 'Text files/greeneggs.txt'



with open(file_name, 'r') as my_file:
    num_characters = average_length(my_file)

print('The average of ' + file_name + ' is ' + str(num_characters)
      + ' words.')
print()



with open(file_name, 'r') as my_file:
    num_characters = longest_word(my_file)

print('The longest word of ' + file_name + ' are ' + str(num_characters)
      + '.')
print()



with open(file_name, 'r') as my_file:
    num_characters = longest_palindrome(my_file)

print('The longest palindrome of ' + file_name + ' are ' + str(num_characters)
      + '.')
print()



with open(file_name, 'r') as my_file:
    num_characters = all_vowels_counter(my_file)

print('The words that contain all the vowels of ' + file_name + ' are ' + str(num_characters)
      + '.')
print()



