

def count_characters(read_file):
    count = 0  
    for line in read_file:  
        count += len(line)
    return count

def main():
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        num_characters = count_characters(my_file)

    print('Green Eggs and Ham by Dr. Seuss ' + 'contains ' + str(num_characters)
          + ' characters.')

    print()





            


def average_length(read_file):
    word_count = 0  
    each_word_count = []  
    for line in read_file:
        words = line.split() 
        for word in words: 
            word_count = len(word) 
            each_word_count.append(word_count) 
    constant = 0
    for i in range(len(each_word_count)):
        constant = constant + each_word_count[i] 
    sum_of_all_the_lengths = constant    
    number_of_words = len(each_word_count)
    return sum_of_all_the_lengths / number_of_words


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    word_average = average_length(my_file)

print('The average length of each word in ' + file_name + ' is ' + str(round(word_average * 100)/100))






def longest_word(read_file):
    longest_word = '' 
    for line in read_file:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
                word_list.clear() 
                if word not in word_list:
                    word_list.append(longest_word)
            elif len(word) == len(longest_word):
                if word not in word_list:
                    word_list.append(word) 
    return word_list

word_list = []
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    long_word = longest_word(my_file)
print()
print('The longest word in ' + file_name + ' is ' + str(long_word))



def longest_palindrome(read_file):
    longest_word = ''
    for line in read_file:
        words = line.split()
        for word in words:
            if word[::] == word[::-1]: 
                if len(word) > len(longest_word): 
                    longest_word = word 
                    word_list.clear()
                    word_list.append(longest_word)
                elif len(word) == len(longest_word):
                    if word not in word_list:
                        word_list.append(word)

    return word_list
      
word_list = []
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    long_pal = longest_palindrome(my_file)
print()
print('The longest palindrome in ' + file_name + ' is ' + str(long_pal))
print()




def all_vowels_counter(read_file):
    for line in read_file:
        words = line.split()
        for word in words:
            if letter in word:
                vowel_word_list.append(word)
    return vowel_word_list       
                
                    
letter = ('a', 'e', 'i', 'o', 'u')
vowel_word_list = []
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    all_vowels = all_vowels_counter(my_file)
print()
print('Words with every vowel in ' + file_name + ' is ' + str(all_vowels))
print()


               
                          



