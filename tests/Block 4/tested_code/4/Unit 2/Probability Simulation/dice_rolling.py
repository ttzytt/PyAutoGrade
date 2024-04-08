



import random
random.seed()

def roll_dice_until_six_different_values():
    die = random.randint(1,6) 
    dice = []
    count = 0 
    dice.append(die)
    while len(dice) < 6:
        die = random.randint(1,6)
        
        if die not in dice:
            
            dice.append(die)
        count = count + 1 
    return count


def average_until_duplicate_dice(num_trials):
    list_ = []
    for times in range(num_trials):
        
        list_.append(roll_dice_until_six_different_values())
    sum_ = 0
    for index in range(len(list_)):
        sum_ += list_[index]
    
    return sum_/num_trials

user_input = int(input('print how many times you want to roll the dice: '))


print(roll_dice_until_six_different_values())
print(average_until_duplicate_dice(user_input))
