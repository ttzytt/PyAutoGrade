









import random
random.seed()


def tries_until_duplicate_birthday():
    random_date = random.randint(1, 365)
    dates = []

    while random_date not in dates:
        dates.append(random_date)
        random_date = random.randint(1, 365)
    return len(dates) + 1 

def average_until_duplicate_birthday(num_trials):
    total = 0
    for _ in range(1, num_trials):
        total += tries_until_duplicate_birthday()
    return total/num_trials
    
num_trials = int(input('Enter how many trials you want to go through: '))
average_result = average_until_duplicate_birthday(num_trials)
print('The average amount of tries is ' + str(average_result))
