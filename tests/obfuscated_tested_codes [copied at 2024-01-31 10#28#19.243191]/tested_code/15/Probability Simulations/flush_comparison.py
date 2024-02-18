




import random

def create_dice(dice_roll):
    for i in range(5):
        dice_roll.append(random.randint(1,4))

def all_equal(equal_list):

    prev_element = equal_list[0]
    
    for i in range(1, len(equal_list)):
        if prev_element != equal_list[i]:
            return False

    return True
    
()

def dice_comparison(dice_roll):

    if all_equal(dice_roll):
        return 1

    return 0


num_trial = int(input('here: '))

total = 0


for i in range(num_trial):
    
    
    dice_roll = []
    create_dice(dice_roll)
    total += dice_comparison(dice_roll)

total += 1

print('The odds are one in ' + str(num_trial/total))
