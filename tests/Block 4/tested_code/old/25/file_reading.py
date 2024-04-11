





def average_length(read_file):
    word_count = 0
    character_count = 0
    for line in read_file:
        words = line.split()
        word_count = word_count + len(words)
        for word in words:
            character_count = character_count + len(word)
    return (character_count/word_count)



def longest_word(read_file):
    longest_words = ['']
    
    for line in read_file:
        words = line.split()
           
        for i in range(len(words)):
            if len(words[i]) > len(longest_words[0]):
                longest_words = []
                if words[i].lower() not in longest_words:
                    longest_words.append(words[i].lower())
                
            elif len(words[i]) == len(longest_words[0]):
                if words[i].lower() not in longest_words:
                    longest_words.append(words[i].lower())
                
    return longest_words



def longest_palindrome(read_file):
    






file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    average_word_len = average_length(my_file)

with open(file_name, 'r') as my_file:
    longest_word_list = longest_word(my_file)

with open(file_name, 'r') as my_file:
    longest_palindrome_list = longest_palindrome(my_file)

print('The average length of each word is ' + str(average_word_len))
print('The longest word(s) is/are ' + str(longest_word_list))
print('The longest palindrome(s) is/are ' + str(longest_palindrome_list))
