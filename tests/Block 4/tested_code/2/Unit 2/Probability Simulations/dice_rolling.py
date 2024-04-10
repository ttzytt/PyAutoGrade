


import random
random.seed()

def all_dice_achived():
    rolled = 0
    values = []
    while True:
        outcome = random.randint(1,6)
        rolled += 1
        if outcome not in values:
            values.append(outcome)
        if len(values) is 6:
            break
    return rolled

def average_of_all_of_trials(trials):
    total_sum = 0
    for i in range(trials):
        total_sum += all_dice_achived()

    return total_sum/trials

trials = int(input('how many trials are there? '))
print('the average is ' + str(average_of_all_of_trials(trials)))
