


import random

random.seed()









def tries_until_all_six_numbers():
    dice_roll = [random.randint(1, 6)]
    num_rolled = 1
    while (len(dice_roll) < 6):
        new_dice_roll = random.randint(1, 6)
        if(new_dice_roll not in dice_roll):
            dice_roll.append(new_dice_roll)
        num_rolled += 1

    return num_rolled





def average_until_duplicate_birthday(num_trials):
    sum = 0
    for _ in range(num_trials):
        sum += tries_until_all_six_numbers()

    average = sum / num_trials

    return average


num_trials = int(input('How many trials would you like to do? '))
print('Your average is: ' + str(average_until_duplicate_birthday(num_trials)))
print(average_until_duplicate_birthday(100))
print(average_until_duplicate_birthday(1000))
print(average_until_duplicate_birthday(10000))
print(average_until_duplicate_birthday(100000))
