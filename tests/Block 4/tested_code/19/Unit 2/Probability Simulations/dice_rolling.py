




import random
random.seed





def tries_until_all_dice_in_list():
    dice_list = []
    new_dice = 0
    count = 0
    while ((len(dice_list))< 6):
        new_dice = random.randint(1, 6) 
        if (new_dice not in dice_list):
            dice_list.append(new_dice)
        count += 1
    return count

 

def average_until_all_dice_in_list(num_trials):
    total = 0
    for _ in range(num_trials):
        total += tries_until_all_dice_in_list()
    average = (total/num_trials)
    print(average)
    return average
    
num_trials = int(input("How many times you want to try: "))
average_until_all_dice_in_list(num_trials)



