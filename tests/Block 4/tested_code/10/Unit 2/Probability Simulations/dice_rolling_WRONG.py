




import random
random.seed()

def tries_until_duplicate_dice_roll():
    rolls = []
    random_dice_roll = random.randint(1, 6)
    while random_dice_roll not in rolls:
        rolls.append(random_dice_roll)
        random_dice_roll = random.randint(1, 6)
    return len(rolls)


def average_until_duplicate_dice_roll(num_trials):
    rolls = 0
    for i in range(num_trials):
        tries_until_duplicate_dice_roll()
        rolls = rolls + tries_until_duplicate_dice_roll()
    numerator = rolls
    average = numerator / num_trials
    print(average)

num_trials = int(input('How many trials do you want to run?'))
average_until_duplicate_dice_roll(num_trials)
