





import random
random.seed


num_trials = int(input("How many times you want to try: "))



def tries_until_duplicate_birthday():
	new = 0
	birthday_list = [random.randint(1, 365)]
	while new not in birthday_list:	
		birthday_list.append(new)
		new = random.randint(1, 365)
	return len(birthday_list)


def average_until_duplicate_birthday(num_trials):
	total = 0
	for _ in range (num_trials):
                total += tries_until_duplicate_birthday()
	average = (total/num_trials)
	print(average)
	return average
	
average_until_duplicate_birthday(num_trials)








