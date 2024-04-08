




import random
random.seed()

def tries_until_duplicate_roll():
    values = []
    rolls = 0
   

    
    while len(values) < 6:
        roll = random.randint(1,6)
        if roll not in values:
            values.append(roll)
        rolls += 1
    return rolls

    

def average_until_duplicate_roll(num_trials):
    total_rolls = 0
    for i in range(1, num_trials):
        total_rolls += tries_until_duplicate_roll()
    return total_rolls/num_trials


num_trials = int(input('Enter how many trials you want to go through: '))
average_result = average_until_duplicate_roll(num_trials)


print(f'The average amount of trials until you get all values of a 6 sided dice is {average_result}')
