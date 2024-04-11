


import random

random.seed()



def tries_until_all_six_values():
    values_rolled = []
        
    number_of_rolls = 0
    
    while len(values_rolled) != 6: 
    
        current_roll = random.randint(1, 6)

        if current_roll not in values_rolled:
                                            
            values_rolled.append(current_roll)

        number_of_rolls += 1
    return number_of_rolls





def average_until_all_six_values(num_trials):
    total_trials = []
    
    for _ in range(num_trials):
        total_trials.append(tries_until_all_six_values())

    return sum(total_trials)/num_trials


num_trials = int(input('How many trials do you want to run?'))

print('The average number of tries was ' + str(average_until_all_six_values(num_trials)) + '.')
