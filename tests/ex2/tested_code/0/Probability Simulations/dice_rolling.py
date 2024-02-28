


import random
random.seed()

def dice_rolling():
    rolls = []
    times_ran = 0
    roll_model = [1,2,3,4,5,6]
    
    
    while rolls != roll_model:
        random_dice_roll = random.randint(1,6)
        if random_dice_roll not in rolls:
            rolls.append(random_dice_roll)
            rolls.sort()
        times_ran += 1
    return times_ran - 1


def dice_rolling_average():
    number = 0
    
    for i in range(num_trials):
        number += dice_rolling()
    number = number / num_trials
    print('The average is ' + str(number))

    
    
num_trials = int(input('How many times would you like to find the average?'))
dice_rolling_average()
