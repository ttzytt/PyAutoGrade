


import random
random.seed()


def tries_until_duplicate_birthday():
    people_asked = 0
    days_checked = []
    
    while True:
        random_day = random.randint(1,365) 
        people_asked += 1 
        if random_day in days_checked:
            break 
        else:
            days_checked.append(random_day)
    return people_asked


def average_until_duplicate_birthday(num_trials):
    total_sum = 0
    for i in range(num_trials):
        total_sum += tries_until_duplicate_birthday()

    return total_sum/num_trials 

num_trials = int(input('How many trials would you like to run: ')) 
print('The average until duplicate birthday is ' + str(average_until_duplicate_birthday(num_trials)))





