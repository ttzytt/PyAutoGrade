


import random
random.seed()



def tries_until_all_six_different_values():

    rolls = []
    count = 0
    
    while len(rolls) < 6:
        random_side = random.randint(1, 6)
        if random_side not in rolls:
            rolls.append(random_side)
        count += 1
            

    return count


def average_until_all_six_different_values(num_trials):

    total = 0

    for i in range(num_trials):
        total += tries_until_all_six_different_values()

    return total / num_trials




num_trials = int(input("Enter the number of trials: "))
print('On average, you need to roll a standard six-sided die ' + \
      str(int(average_until_all_six_different_values(num_trials))) + \
      ' times until you have rolled all six different values.')
      
