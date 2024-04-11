











print('T2 begins: ')
def average_word_length(read_file):
    with open(read_file, 'r') as my_file:
        words = my_file.read().split() 
        word_lengths = [len(word) for word in words] 
        if len(word_lengths) > 0:
            return sum(word_lengths) / len(word_lengths) 
        else:
            return 0  

read_file = "Text files/names.txt" 
average_length = average_word_length(read_file) 
if average_length is not None: 
    print("Average word length:" + str(round(average_length*100)/100) + ' in ' + read_file)
print()




print('T3 begins: ')
def longest_word(read_file):
    highest_length = 0 
    with open(read_file, 'r') as my_file:
        words = my_file.read().split() 
        for word in words:
            if len(word) > highest_length: 
                highest_length = len(word) 
                words_list.clear() 
                words_list.append(word) 
            elif len(word) == highest_length: 
                if word not in words_list:
                    words_list.append(word) 
        return words_list           

words_list = []
read_file = "Text files/greeneggs.txt" 
longest = longest_word(read_file)
print('The longest words are: ' + str(longest))
print()




print('T4 begins: ')
def longest_palindrome(read_file):
    highest_length = 0 
    with open(read_file, 'r') as my_file:
        words = my_file.read().split() 
        for word in words:
            if word[::-1] == word[::]:
                if len(word) > highest_length: 
                    highest_length = len(word) 
                    words_list.clear() 
                    words_list.append(word) 
                elif len(word) == highest_length: 
                    if word not in words_list: 
                        words_list.append(word) 
        return words_list           

words_list = []
read_file = "Text files/greeneggs.txt" 
palindrome = longest_palindrome(read_file)
print('The longest palindrome are: ' + str(palindrome))
print()




print('T5 begins: ')
def all_vowels_counter(read_file):
    vowels_in_word = []
    with open(read_file, 'r') as my_file:
        words = my_file.read().split() 
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
        return words_list
       

words_list = []
read_file = "Text files/words.txt" 
all_vowels = all_vowels_counter(read_file)
print('The words contain all five vowels are: ' + str(all_vowels))
print()




def count_long_lines(read_file, min_length):
    length = 0
    with open(read_file, 'r') as my_file:
        words = my_file.read().split() 
        if len(words) >= min_length:
            length += 1
            print(words)
    return length

min_length = 5
read_file = "Text files/names.txt" 
number_of_lines = count_long_lines(read_file, min_length)
print('The number of lines longer than min_length is: ' + str(number_of_lines))
print()

































