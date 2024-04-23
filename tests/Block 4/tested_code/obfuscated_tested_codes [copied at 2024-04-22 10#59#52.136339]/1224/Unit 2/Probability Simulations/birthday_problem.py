


import random
random.seed()


def tries_until_duplicate_birthday():
    birthdays = []
    
    random_birthday = random.randint(1, 365)
    
    while random_birthday not in birthdays:
        birthdays.append(random_birthday)
        random_birthday = random.randint(1, 365)
    
    return len(birthdays)



def average_until_duplicate_birthday(num_trials):
    birthday_average = 0
    for i in range(num_trials):
        tries_until_duplicate_birthday()
        birthday_average = birthday_average + tries_until_duplicate_birthday()
    numerator = birthday_average
    average = numerator / num_trials
    print(average)

num_trials = int(input('How many trials do you want to run?'))
average_until_duplicate_birthday(num_trials)

