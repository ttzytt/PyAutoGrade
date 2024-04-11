


import random
"""
The tests were within the range of about, and did not get closer to the actual answer
with a larger number of tests
"""
random.seed()
"""
a simulation to see how many people we would need to ask,
on average, before we find two with the same birthday.
We will assume each birthday is equally likely, and
ignore leap years (so, 365 days in a year). 
"""

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

