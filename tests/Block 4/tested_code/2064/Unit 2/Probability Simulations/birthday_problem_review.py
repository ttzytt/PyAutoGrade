 



import random

random.seed()













def tries_until_duplicate_birthday():
    birthdays = [random.randint(1, 365)]
    new_bday = random.randint(1, 365)
    while new_bday not in birthdays:
        birthdays.append(new_bday)
        new_bday = random.randint(1, 365)

    return len(birthdays) + 1
        




def average_until_duplicate_birthday(num_trials):
    sum = 0
    for _ in range(num_trials):
        sum += tries_until_duplicate_birthday()

    average = sum / num_trials

    return average

num_trials = int(input('How many trials would you like to do? '))
print('Your average is: ' + str(average_until_duplicate_birthday(num_trials)))
