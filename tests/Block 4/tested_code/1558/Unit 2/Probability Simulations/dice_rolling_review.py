




import random
"""
a simulation to see how many times you would need to roll a standard 6 sided die
until all the sides have been rolled at least once.
"""


def rolls_until_all_values():
    values_seen = []  
    rolls = 0  

    while len(values_seen) < 6:
        roll = random.randint(1, 6)  
        values_seen.append(roll)  
        rolls += 1  
        



        
    return rolls

def average_until_all_values(num_trials):
    total_rolls = 0  

    for _ in range(num_trials):
        total_rolls += rolls_until_all_values()

    return total_rolls / num_trials 

num_trials = int(input('How many trials do you want to go through? '))
print(f'Average number of rolls to get all six values in {num_trials} trials is')
print(f'{average_until_all_values(num_trials)}')
