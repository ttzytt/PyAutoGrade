





import random
random.seed




def tries_until_duplicate_birthday():
	new = random.randint(1, 6)
	birthday_list = []
	while new not in birthday_list:	
		birthday_list.append(new)
		new = random.randint(1, 365)
	return (len(birthday_list) + 1)


def average_until_duplicate_birthday(num_trials):
	total = 0
	for _ in range (num_trials):
		total += tries_until_duplicate_birthday()
	print (total/num_trials)
	return (total/num_trials)

num_trials = int(input("How many times you want to try: "))	
average_until_duplicate_birthday(num_trials)








