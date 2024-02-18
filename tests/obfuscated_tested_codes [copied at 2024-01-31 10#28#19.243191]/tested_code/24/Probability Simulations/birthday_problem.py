





import random

random.seed()


def tries_until_duplicate_birthday():
    
    birthdays = [] 
    i = 0
    birthday = random.randint(1, 365)

    while birthday not in birthdays:
        birthdays.append(birthday) 
        i += 1
        birthday = random.randint(1, 365)

    return i + 1 


def average_until_duplicate_birthday(num_trials):

    trials = [] 

    sum = 0

    for j in range(len(num_trials)): 
        sum += tries_until_duplicate_birthday()

    average = sum / len(num_trials)

    return average



num_trials = input('How many times of simulation would you like to do? ')

average_until_duplicate_birthday(num_trials)

print('You did ' + str(num_trials) + ' times of simulation.')
print('The trials asked on average ' + str(average_until_duplicate_birthday(num_trials)) + ' people.')
