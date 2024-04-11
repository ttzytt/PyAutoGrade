'''
Written by Alex
I did not receive help from my classmates and/or online resources
'''
import random
random.seed()




def tries_until_duplicate_birthday(include_leap_year = False):
    birthdays = []
    times_used = 0
    asked = random.randint(1,1461)
    
    
    if asked != 1461:
        asked = random.randint(1,365)
    while asked not in birthdays: 
        birthdays.append(asked)
        times_used += 1
        asked = random.randint(1,1461)
        if asked != 1461:
            asked = random.randint(1,365)
    if asked in birthdays:
        return times_used + 1

def average_until_duplicate_birthday(num_trials, include_leap_year = False):
    times_total = 0
    for run_time in range(num_trials):
        tries_until_duplicate_birthday()
        times_total += tries_until_duplicate_birthday()
    return times_total/num_trials

num_trials = int(input('For how many times do you want it to run? '))
print(average_until_duplicate_birthday(num_trials))
