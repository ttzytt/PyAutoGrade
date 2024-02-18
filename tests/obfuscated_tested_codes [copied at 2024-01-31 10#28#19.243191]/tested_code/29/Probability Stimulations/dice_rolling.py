


import random


def trials_until_all_values_rolled():

    
    
    dice_roll = random.randint(1, 6)
    list_of_rolls = []
    trials_done = 0

    
    
    while len(list_of_rolls) < 6:

        
        if dice_roll not in list_of_rolls:
            list_of_rolls.append(dice_roll)

        
        trials_done += 1
        
        dice_roll = random.randint(1, 6)


    return trials_done



def average_number_of_trials(num_trials):
    sum_of_trials = 0
    
    for _ in range(num_trials):
        sum_of_trials += trials_until_all_values_rolled()

    
    return sum_of_trials/num_trials


num_trials_input = int(input("How many times do you want to run: "))
print(average_number_of_trials(num_trials_input))
    

        
