


import random

random.seed()



def tries_until_duplicate_birthday():

    birthdays = []
    new_birthday = 1 
    
    while new_birthday not in birthdays:
        birthdays.append(new_birthday)
        new_birthday = random.randint(1, 365)


    return len(birthdays)



def average_until_duplicate_birthday(num_trials):
    total_trials = []
    
    for _ in range(num_trials):
        total_trials.append(tries_until_duplicate_birthday())
        

    return sum(total_trials)/num_trials




tries = int(input('How many trials do you want to run?'))

print('The average number of people is ' + str(average_until_duplicate_birthday(tries)) + '.')

