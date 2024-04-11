


import random
random.seed()



def tries_until_duplicate_birthday():
    birthday = random.randint(1, 365)
    birthdays = []
    while birthday not in birthdays:
        birthdays.append(birthday)
        birthday = random.randint(1, 365)
    return len(birthdays) + 1 
                              
                              
            



def average_until_duplicate_birthday(num_trials):
    times = 0
    average = 0
    while (times <= num_trials):
        birthday = random.randint(1, 365)
        birthdays = []
        while birthday not in birthdays:
            birthdays.append(birthday)
            birthday = random.randint(1, 365)
        average += len(birthdays) + 1 
        times += 1
    average /= times
    return average



def run_B():
    num_trials = int(input('For how many times do you want it to run? '))
    print(average_until_duplicate_birthday(num_trials))










def tries_until_duplicate_birthday(include_leap_year = False):
    leap = random.randint(1, 4)
    if leap == 4:
        days = 366
        print('it is a leap year')
    else:
        days = 365
    birthday = random.randint(1, days)
    birthdays = []
    while birthday not in birthdays:
        birthdays.append(birthday)
        birthday = random.randint(1, days)
    return len(birthdays) + 1 

def average_until_duplicate_birthday(num_trials, include_leap_year = False):
    leap = random.randint(1, 4)
    if leap == 4:
        days = 366
        print('it is a leap year')
    else:
        days = 365
    times = 0
    average = 0
    while (times <= num_trials):
        birthday = random.randint(1, 365)
        birthdays = []
        while birthday not in birthdays:
            birthdays.append(birthday)
            birthday = random.randint(1, 365)
        average += len(birthdays) + 1 
        times += 1
    average /= times
    return average


