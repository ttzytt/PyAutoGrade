






def average_length(read_file):
    word_len_sum = 0
    num_words = 0
    for line in my_file:
        words = line.split()
        for word in words:
            word_len_sum = word_len_sum + len(word)
            num_words += 1
    return word_len_sum / num_words





def longest_word(read_file):
    long_word = ' '
    current_word = ' '
    old_word = ' '
    for line in my_file:
        words = line.split()
        for word in words:
            current_word = word
            if len(current_word) > len(old_word):
                long_word = current_word
            old_word = current_word
            
    return long_word




def longest_palindrome(read_file):
    long_palindrome = ''
    old_palindrome = ''
    for line in my_file:
        words = line.split()
        line.lower()
        for word in words:
            if word == word[::-1]:
                long_palindrome = word
                
            if len(old_palindrome) > len(long_palindrome):
                long_palindrome = old_palindrome
            

            
                
    return long_palindrome



file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    average_len = average_length(my_file)

print('The average word length in ' + file_name + ' is ' + str(average_len)
      + ' characters.')
print()

my_file.close()



with open(file_name, 'r') as my_file:
    longest = longest_word(my_file)
    
print('The longest word in ' + file_name + ' is ' + str(longest)
      + '.')
print()
my_file.close()

with open(file_name, 'r') as my_file:

    palindrome = longest_palindrome(my_file)

print('The longest palindrome in ' + file_name + ' is ' + str(palindrome)
      + '.')
print()
