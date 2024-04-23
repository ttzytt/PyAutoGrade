


import random
random.seed()




'''
Return the average length of all the words in the file read_file.
    inputs:
        read_file    A file that is open for reading.
'''
def average_length(read_file):
        letter_count = 0 
        word_count = 0 
        for lines in read_file: 
            text = lines.split()
            word_count += len(text)	
            for words in text: 
                letter_count += len(words)
        if word_count > 0:             
            return(letter_count/word_count)
        else:
            return none 
        


'''
Find the longest word or words in the file read_file.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_word(read_file):
	length = 0
	place = 0
	long_word = []
	words = ''
	for lines in read_file: 
		words = ''
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


'''
Find the longest word in the file read_file that is a palindrome.
    inputs:
        read_file    A file that is open for reading.
'''
def longest_palindrome(read_file):
	length = 0
	long_word = []
	my_string = ''
	words = ''
	
	for lines in read_file:
		words = ''
		words = str(lines)
		text = words.split()
		for i in range(len(text)):
			my_string = text[i]
			if (length < len(text[i]) and text[i] == my_string[::-1] and text[i] not in long_word):
				length = len(text[i])
				long_word = []
				long_word.append(text[i])
			elif (length == len(text[i]) and text[i] == my_string[::-1] and text[i] not in long_word):
				long_word.append(text[i])
				
	return(long_word)


'''
Return the number of words in the file read_file that contain all five vowels
A, E, I, O, and U, not necessarily in that order.
    inputs:
        read_file    A file that is open for reading.
'''
def all_vowels_counter(read_file):
	length = 0
	long_word = []
	my_string = ''
	words = ''
	word = ''
	for lines in read_file:
		words = str(lines)
		text = words.split()
		for word in text:
			if (('a' or 'A')in word) or (('e' or 'E')in word) or (('i' or 'I')in word) or (('o' or 'O')in word) or (('u' or 'U')in word):
				long_word.append(text)
					
	return(long_word)
          

'''
Return the number of lines in the file read_file that contain at least min_length characters.
    inputs:
        read_file    A file that is open for reading.
        min_length   A variable that restrict the line numbers
'''
def count_long_lines(read_file, min_length):
        long_lines = 0
        for line in read_file:
                len_line = 0
                splited_line = line.split()
                for i in range(len(splited_line)):
                        word = splited_line[i]

                        for n in range(len(word)):
                                if word[n] != (',' and '.'):
                                        len_line += 1
                if len_line >= min_length:
                        long_lines += 1

        return(long_lines)


'''
Return a random word from the file read_file
    inputs:
        read_file    A file that is open for reading.
'''
def random_word(read_file):
        all_words = []
        for line in read_file:
                splited_line = line.split()
                for n in range(len(splited_line)):
                        single_word = splited_line[n]
                        all_words.append(single_word)

        length_of_file = len(all_words)
        position = random.randint(0, length_of_file - 1)
        if all_words[position][-1] == (',' or '.'):
                all_words[position] = all_words[position][:-1]

        return(all_words[position])


'''
Return a list of num_words random words from the file read_file.
    inputs:
        read_file    A file that is open for reading.
        num_words    Amount of the random words want to take from the file
'''
def random_words(read_file,num_words):
    all_words = []
    random_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            all_words.append(single_word)
    

    while len(random_words) < num_words:
    
        length = len(all_words)-1
        position = random.randint(0,length)
        if all_words[position][-1] == ',' or all_words[position][-1] == '.':
            all_words[position] == all_words[position][:-1]
            
        if all_words[position] not in random_words:
            random_words.append(all_words[position])
            
    return random_words


'''
Return the number of times the word word appears in the file read_file.
    inputs:
        read_file    A file that is open for reading.
        word         The word want to take from the file
'''
def specific_word_count(read_file, word):
    all_words = []
    appeared_time = 0
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            if single_word[-1] == ',' or single_word[-1] == '.':
                single_word = single_word[:-1]
            all_words.append(single_word)
    

    for n in range(len(all_words)):
        if word.lower() == all_words[n].lower():
            appeared_time += 1
            

    return appeared_time


'''
Return the number of words in read_file that begin with the string word_beginning.
    inputs:
        read_file            A file that is open for reading.
        word_beginning       The word want to begin with
'''
def starts_with_counter(read_file, word_beginning):
    all_words = []
    appeared_time = 0
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            if single_word[-1] == ',' or single_word[-1] == '.':
                single_word = single_word[:-1]
            all_words.append(single_word)
    

    for n in range(len(all_words)):
        if len(all_words[n]) >= len(word_beginning):
        
        
            if all_words[n][:len(word_beginning)].lower() == word_beginning.lower():
            
                appeared_time += 1

    return appeared_time




def main():
     
        file_name = 'Text files/greeneggs.txt'
        with open(file_name, 'r') as my_file:
            average_lengths = average_length(my_file)

        print('The average length of the file ' + file_name + ' is ' + str(average_lengths)
              + ' characters.')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            longest_words = longest_word(my_file)

        print('The longest word in the file ' + file_name + ' is ' + str(longest_words)
              + ' .')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            longest_palindromes = longest_palindrome(my_file)

        print('The longest_palisndrome in the file ' + file_name + ' is ' + str(longest_palindromes)
              + ' .')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            all_vowels_counters = all_vowels_counter(my_file)

        print('There ' + file_name + ' are ' + str(all_vowels_counters)
              + ' words containing A,E,I,O and U.')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            count_long_lines_1 = count_long_lines(my_file, 3)

        print('There ' + file_name + ' are ' + str(count_long_lines_1)
              + ' long lines in the file.')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            random_word_1 = random_word(my_file)

        print('The random word ' + file_name + ' is ' + str(random_word_1)
              + ' .')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            random_words_1 = random_words(my_file, 4)

        print('The random words ' + file_name + ' are ' + str(random_words_1)
              + ' .')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            appeared_times = specific_word_count(my_file, 'Sky')

        print('The specific word count ' + file_name + ' is ' + str(appeared_times)
              + ' .')
        print()


        file_name = 'Text files/names.txt'
        with open(file_name, 'r') as my_file:
            appeared_time_1 = starts_with_counter(my_file, 'Sky')

        print('The count after the word ' + file_name + ' is ' + str(appeared_time_1)
              + ' .')
        print()

if __name__ == "__main__":
        main()
