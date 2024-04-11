



import random
random.seed()


def tries_until_duplicate_birthday():
    people = 0
    days = []
    while True: 
        random_days = random.randint(1,365)
        people += 1
        if random_days in days:
            break
        else:
            days.append(random_days)
    return people

        
def average_until_duplicate_birthday(num_trials):
    total_sum = 0
    for i in range(num_trials):
        total_sum += tries_until_duplicate_birthday()
    return total_sum/num_trials

num_trials = int(input('how many trials are there? '))
print('the average is ' + str(average_until_duplicate_birthday(num_trials)))


