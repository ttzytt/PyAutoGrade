


import random
random.seed()


def tries_until_all_dice_values_are_achieved():
    times_rolled = 0
    dice_values = []
    
    while True:
        random_outcome = random.randint(1,6)
        times_rolled += 1
        
        if random_outcome not in dice_values:
            dice_values.append(random_outcome)
        
        if len(dice_values) is 6:   
            break
    return times_rolled


def average_rolls_until_all_values(num_trials):
    total_sum = 0
    for i in range(num_trials):
        total_sum += tries_until_all_dice_values_are_achieved()

    return total_sum/num_trials


num_trials = int(input('How many trials would you like to run?'))

print('The average amount of rolls until all dice values are achieved is '
      + str(average_rolls_until_all_values(num_trials)))
