



def average_length(read_file):
        letter_count = 0 
        word_count = 0 
        for lines in read_file: 
            text = lines.split()
            word_count += len(text)	
            for words in text: 
                letter_count += len(words)
        return(letter_count/word_count)



def longest_word(read_file):
	length = 0
	place = 0
	long_word = []
	words = ''
	for lines in read_file: 
		words = ''
		words = str(lines) 
		text = words.split() 
		for __ in range(len(text)):
			
			if (length < len(text[__]) and text[__] not in long_word):
				length = len(text[__])
				long_word = []
				long_word.append(text[__])
			elif (length == len(text[__]) and text[__] not in long_word):
				long_word.append(text[__])

	return(long_word)



def longest_palindrome(read_file):
	length = 0
	long_word = []
	my_string = ''
	words = ''
	
	for lines in read_file:
		words = ''
		words = str(lines)
		text = words.split()
		for __ in range(len(text)):
			my_string = text[__]
			if (length < len(text[__]) and text[__] == my_string[::-1] and text[__] not in long_word):
				length = len(text[__])
				long_word = []
				long_word.append(text[__])
			elif (length == len(text[__]) and text[__] == my_string[::-1] and text[__] not in long_word):
				long_word.append(text[__])
				
	return(long_word)


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    average_length = average_length(my_file)

print('The average length of the file ' + file_name + ' is ' + str(average_length)
      + ' characters.')
print()


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    longest_word = longest_word(my_file)

print('The longest word in the file ' + file_name + ' is ' + str(longest_word)
      + ' .')
print()


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    longest_palindrome = longest_palindrome(my_file)

print('The longest_palindrome in the file ' + file_name + ' is ' + str(longest_palindrome)
      + ' .')
print()
