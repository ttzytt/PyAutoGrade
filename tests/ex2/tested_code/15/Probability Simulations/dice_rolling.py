




import random





def dice_rolls_until_6():

    counter = 0
    rolls = []
    roll = random.randint(1,6)

    while len(rolls) != 6:

        roll = random.randint(1,6)

        if roll not in rolls:
            rolls.append(roll)

        counter += 1

    return counter



def average_dice_rolls_until_6(num_trials):
    sum = 0
    for i in range(num_trial):
        sum += dice_rolls_until_6()

    return sum/num_trial

while True:
    
    num_trial = int(input('How many trials do you want to run: '))

    print(average_dice_rolls_until_6(int(num_trial)))



