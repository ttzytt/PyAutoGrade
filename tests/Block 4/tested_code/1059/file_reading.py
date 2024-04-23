






import random
random.seed()





def average_length(read_file):
	length = 0
	length_word = 0

	
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
		words = str(lines) 
		text = words.split() 
		for i in range(len(text)):
			
			
			if (length < len(text[i]) and text[i] not in long_word):
				length = len(text[i])
				long_word = []
				long_word.append(text[i])
			elif (length == len(text[i]) and text[i] not in long_word):
				long_word.append(text[i])

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
	number = 0
	long_word = []
	for lines in read_file: 
		text = lines.split()
		
		for word in text:
			word = word.lower() 
			if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
				number += 1
					
	return(number)






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
	lines = read_file.read()
	words = lines.split() 
	random_place = random.randint(0,len(words)) 
	
	return(words[random_place])





def random_words(read_file,num_words):
	txt_word = []
	lines = read_file.read()
	words = lines.split()
	for i in range (num_words): 
		random_place = random.randint(0,len(words)) 
		txt_word.append(words[random_place]) 
	return(txt_word)





def specific_word_count(read_file,word):
	count = 0
	lines = read_file.read()
	words = lines.split()
	for word_ in words:
		if word == word_:
			count += 1
	return(count)





def starts_with_counter(read_file,word_beginning):
	length = 0
	txt_word = []
	my_string = ''
	count = 0
	list_1 = []
	lines = read_file.read()
	words = lines.split()
	for word_ in words:
                
		if word_[0:len(word_beginning)] == word_beginning:
			count += 1
	return(count)



def main():
        min_length = 10
        num_words = 5
        word_beginning = 'eggs'
        word = 'eggs'
        file_name = 'Text files/greeneggs.txt'

        with open(file_name, 'r') as read_file:
            task_2 = average_length(read_file)
        print('The average length of the word in ', file_name, 'is',task_2)

        with open(file_name, 'r') as read_file:
            task_3 = longest_word(read_file)
        print('The longest word in ', file_name, 'is',task_3)

        with open(file_name, 'r') as read_file:
            task_4 = longest_palindrome(read_file)
        print('The longest palindrome in ', file_name, 'is',task_4)

        with open(file_name, 'r') as read_file:
            task_5 = all_vowels_counter(read_file)
        print('The words that have all vowels in ', file_name, 'is',task_5)

        with open(file_name, 'r') as read_file:
            task_6 = count_long_lines(read_file, min_length)
        print('The lines that have at least',min_length,'words in', file_name, 'is',task_6)

        with open(file_name, 'r') as read_file:
            task_7 = random_word(read_file)
        print('A random word in', file_name, 'is',task_7)

        with open(file_name, 'r') as read_file:
            task_8 = random_words(read_file, num_words)
        print('A list of',num_words,'random words', file_name, 'is',task_8)

        with open(file_name, 'r') as read_file:
            task_9 = specific_word_count(read_file, word)
        print(word,'appeared',task_9,'times in',file_name)
        
        with open(file_name, 'r') as read_file:
            task_10 = starts_with_counter(read_file, word_beginning)
        print(task_10,'words in',file_name, 'starts with', word_beginning)
if __name__ == "__main__":
        main()
