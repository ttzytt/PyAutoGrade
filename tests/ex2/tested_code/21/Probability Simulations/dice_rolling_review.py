


import random

random.seed()



def tries_until_six_different_values():
    values_rolled = []
    different_values_rolled = 0
    while different_values_rolled < 6:
        roll = random.randint(1, 6)
        if roll not in values_rolled:
            different_values_rolled += 1
        values_rolled.append(roll)

    return len(values_rolled)



    


def average_until_six_different_values(num_trials):
    sum_of_trials = 0
    for _ in range(num_trials):
        sum_of_trials += tries_until_six_different_values()

    return(sum_of_trials/num_trials)

    
num_trials = int(input('How many trials do you want? '))
print(average_until_six_different_values(num_trials))



