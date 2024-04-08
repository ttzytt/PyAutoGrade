




def length(read_file):
    count = 0  
    number_of_words = 0
    for line in read_file:  
        words = line.split()
        for word in words:
            count += len(word)
            number_of_words += 1
    average_length = count / number_of_words        
    return average_length


file_name = 'Text files/commonwords.txt'
with open(file_name, 'r') as my_file:
    average_length = length(my_file)

print('The file ' + file_name + ' contains ' + str(average_length)
      + ' characters.')
print()



def longest_word(read_file):
    longest_words = [] 
    length_of_word = 0
    for line in read_file:
        words = line.split()
        for word in words: 
            if len(word) > length_of_word:
                length_of_word = len(word)
                longest_words = [word]
            elif len(word) == length_of_word:
                longest_words.append(word)
            
                
    return longest_words


file_name = 'Text files/longest_word_test.txt'
with open(file_name, 'r') as my_file:
    longest_words = longest_word(my_file)

print('The file ' + file_name + " 's " + 'longest word(s) is(are) ' + str(longest_words))
print() 

