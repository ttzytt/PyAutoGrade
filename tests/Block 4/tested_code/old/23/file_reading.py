





def average_length(read_file):
    count_word = 0
    count_character = 0
    
    for line in read_file: 
        words = line.split()
        count_word += len(words)

        for word in words:
            count_character += len(word)

    return count_character / count_word
            

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    average_characters = average_length(my_file)

    
print('The file ' + file_name + ' has an average of ' + str(average_characters)
      + ' characters per word.')
print()






def longest_word(read_file):
    length = 0
    longest_word = []
    
    for line in read_file:
        words = line.lower().split()
        
        for word in words:
            if len(word) == length:
                longest_word.append(word)
            elif len(word) > length:
                longest_word = [word]
                length = len(word)

    return longest_word


file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    longest_words = longest_word(my_file)


print('The list of the longest words of the file ' + file_name + ' is\n' + str(longest_words))
print()





def longest_palindrome(read_file):
    length = 0
    longest_palindrome = []

    for line in read_file:
        words = line.lower().split()

        for word in words:
            if word == word[::-1]:
                if len(word) == length:
                    longest_palindrome.append(word)
                elif len(word) > length:
                    longest_palindrome = [word]
                    length = len(word)

    return longest_palindrome


file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    longest_palindromes = longest_palindrome(my_file)


print('The list of the longest palindromes of the file ' + file_name + ' is\n' + str(longest_palindromes))
print()





def all_vowels_counter(read_file):
    vowels_counter = []

    for line in read_file:
        words = line.lower().split()

        for word in words:
            
            if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
                vowels_counter.append(word)

    return vowels_counter

file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    vowels_counter = all_vowels_counter(my_file)

print('The list of the vowels of ' + file_name + 'that contains all vowels is\n' + str(vowels_counter))
print()





def count_long_lines(read_file, min_length):
    count = 0

    for line in read_file:
        if len(line) >= min_length:
            count += 1

    return count

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    
    count = count_long_lines(my_file, 16)

print('There are ' + str(count) + ' words in ' + file_name + ' that contains at least 10 characters')
print()





def random_word(read_file):
    import random
    file = read_file.read().split()
    word = random.choice(file)
    return word
    
file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    word = random_word(my_file)

print('The random word chosen in ' + file_name + ' is ' + str(word) + '.')
print()





def random_words(read_file, num_words):
    import random
    words = []
    file = read_file.read().split()
    
    for _ in range(num_words):
        random.shuffle(file)
        words.append(file[0])
        file = file[1:]

    return words

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    words = random_words(my_file, 3)

print('The 3 random words chosen in ' + file_name + ' are ' + str(words) + '.')
print()





    
