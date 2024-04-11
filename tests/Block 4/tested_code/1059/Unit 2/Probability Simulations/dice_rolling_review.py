





import random
random.seed


num_trials = int(input("How many times you want to try: "))






def tries_until_duplicate_birthday():
    birthday_list = []
    new_birthday = random.randint(1, 6)
    
    
    
    while ((1 not in birthday_list) or (2 not in birthday_list) or (3 not in birthday_list) or (4 not in birthday_list) or (5 not in birthday_list) or (6 not in birthday_list)):    
        birthday_list.append(new_birthday)
        new_birthday = random.randint(1, 6)
    return len(birthday_list)

tries_until_duplicate_birthday()



def average_until_duplicate_birthday(num_trials):
    total = 0
    for _ in range(num_trials):
        total += tries_until_duplicate_birthday()
    average = (total/num_trials)
    return average
    
average_until_duplicate_birthday(num_trials)






'''R
Where is the average printed out?

'''

