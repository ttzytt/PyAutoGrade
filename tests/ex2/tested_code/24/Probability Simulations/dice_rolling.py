


import random

random.seed()


def tries_until_duplicate_dice():
    
    dice_rolls = [] 
    i = 0
    dice_roll = random.randint(1, 6)
    n = 0

    while i < 6:
        if dice_roll not in dice_rolls:
            dice_rolls.append(dice_roll) 
            i += 1
        dice_roll = random.randint(1, 6)
        n += 1

    return n 


def average_until_duplicate_dice(num_trials):

    trials = [] 

    sum = 0

    for j in range(len(num_trials)): 
        sum += tries_until_duplicate_dice()

    average = sum / len(num_trials)

    return average



num_trials = input('How many times of simulation would you like to do? ')

average_until_duplicate_dice(num_trials)

print('You did ' + str(num_trials) + ' times of simulation.')
print('The trials threw on average ' + str(average_until_duplicate_dice(num_trials)) + ' times of dice.')
