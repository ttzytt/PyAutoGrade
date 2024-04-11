import random
random.seed()


def task_1():
	words = ''
	words_1 = ''
	file_name = 'Text files/greeneggs.txt'
	with open(file_name, 'r') as my_file:
		lines = my_file.readlines()
		print(lines)
		
		for _ in range (len(lines)):
			words += lines[_]
			

		for __ in range(len(words)):
			
			if (random.random()) < 0.6:
				temp = words[__].lower()
			else:
				temp = words[__].upper()
			
			words_1 += temp

	return(words_1)


task_1()
