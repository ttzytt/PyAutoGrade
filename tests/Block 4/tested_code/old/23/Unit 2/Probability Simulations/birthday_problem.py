







import random
random.seed()



def tries_until_duplicate_birthday(include_leap_year):
    birthdays = []
    new_birthday = random.randint(1,365)

    
    
    
    
    if include_leap_year == True:
        choose_birthday = []
        for i in range(365 * 4):
            choose_birthday.append(new_birthday)
        choose_birthday.append(366)
        new_birthday = random.choose(choose_birthday)
            
    
    
    while new_birthday not in birthdays:
        birthdays.append(new_birthday)
        new_birthday = random.randint(1,365)
    return len(birthdays)+ 1



def average_until_duplicate_birthday(num_trials, include_leap_year):
    sum_tries = 0

    for _ in range(num_trials):
        sum_tries = sum_tries + tries_until_duplicate_birthday(include_leap_year)
        
    average = sum_tries / num_trials
    return average


num_trials = int(input('Birthday problem: How many trails do you want to do? '))
include_leap_year = input('Include leap year? True/False: ')
print(average_until_duplicate_birthday(num_trials, include_leap_year))
