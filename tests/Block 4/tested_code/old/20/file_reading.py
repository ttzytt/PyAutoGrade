



def average_length(read_file):
    total_length = 0 
    total_words = 0 
    
    
    for line in read_file:
        words = line.split() 
        total_words += len(words) 

    
        for word in words:
            total_length += len(word)

    average = total_length / total_words
    return average
       
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    average = average_length(my_file)

print('The file ' + file_name + ' has an average length of ' + str(average)
      + '.')
print()


def longest_word(read_file):
    longest_length = 0
    longest_word = []

    for line in read_file:
        words = line.split()

        for word in words:
            word_length = len(word)
            
            if word_length > longest_length:
                longest_length = word_length
                longest_word = [word]
            
            elif word_length == longest_length:
                longest_word.append(word)

    return longest_word

file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    longest = longest_word(my_file)

print('The longest word(s) in the file ' + file_name + ' is/are:')
for word in longest:
    print(word)

def longest_palindrome(read_file):
