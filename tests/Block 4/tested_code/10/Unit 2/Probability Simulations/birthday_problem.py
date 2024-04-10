


import random

random.seed()


def tries_until_duplicate_birthday():
    birthdays_looked_at = []
    birthday = random.randint(1, 365) 
    
    while birthday not in birthdays_looked_at:
        birthdays_looked_at.append(birthday) 
        birthday = random.randint(1, 365) 
        

    return len(birthdays_looked_at) 



def average_until_duplicate_birthday(num_trials):

    total_repeat = 0 
    for _ in range(num_trials):
        total_repeat += tries_until_duplicate_birthday()
  
    return total_repeat/ num_trials


num_trials = int(input('How many trials do you want to go through? '))
print(f'average number of repeated birthdays in {num_trials} trials is')
print(f'{average_until_duplicate_birthday(num_trials)}')

