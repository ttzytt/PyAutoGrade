



import random
random.seed()


def six_different_values(dices):
    if (1 in dices and 2 in dices and 3 in dices
        and 4 in dices and 5 in dices and 6 in dices):
        return True
    return False

def tries_until_all_six():
    dices = []
    dice = random.randint(1,6)
    while six_different_values(dices) is False:
        dices.append(dice)
        dice = random.randint(1,6)
    
    return len(dices)

def average_times_used(num_trials):
    times_total = 0
    for run_time in range(num_trials):
        tries_until_all_six()
        times_total += tries_until_all_six()
    return times_total/num_trials

num_trials = int(input('For how many times do you want it to run? '))
print(average_times_used(num_trials))

