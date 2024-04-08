import random
random.seed()






def average_length(read_file):
	length = 0
	length_word = 0
	words = ''
	
	for lines in read_file:
		text = lines.split()
		length_word += len(text)
		
		for words in text: 
			length += len(words)
	return(length/length_word)






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



def all_vowels_counter(read_file):
	length = 0
	long_word = []
	my_string = ''
	words = ''
	word = ''
	for lines in read_file:
		words = (lines)
		text = words.split()
		for word in text:
			word = word.lower() 
			if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
				length += 1
					
	return(length)

def count_long_lines(read_file, min_length):
	length = 0
	long_word = []
	my_string = ''
	words = ''
	word = ''
	min_length += 1
	for lines in read_file:
		if len(lines) >= min_length:
			length += 1
			
	return(length)



def random_word(read_file):
	length = 0
	txt_word = []
	my_string = ''

	word = ''
	list_1 = []
	
	lines = read_file.read()
	words = lines.split()
	random_place = random.randint(0,len(words))
	return(words[random_place])

def random_words(read_file, num_words):
	length = 0
	txt_word = []
	my_string = ''

	word = ''
	list_1 = []
	
	lines = read_file.read()
	words = lines.split()
	random_place = random.randint(0,len(words))
	for i in range (num_words):
		random_place = random.randint(0,len(words))
		txt_word.append(words[random_place])
	return(txt_word)

def random_words(read_file, num_words):
	length = 0
	txt_word = []
	my_string = ''

	word = ''
	list_1 = []
	
	lines = read_file.read()
	words = lines.split()
	random_place = random.randint(0,len(words))
	for i in range (num_words):
		random_place = random.randint(0,len(words))
		txt_word.append(words[random_place])
	return(txt_word)
	
	
min_length = 35
num_words = 5
file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as read_file:
    task = random_words(read_file, num_words)
print(task)
