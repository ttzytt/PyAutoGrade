



import random

random.seed()


def tries_until_six_different_values():
    roll = random.randint(1, 6)
    rolls = []
    roll_count = 0
    rolls.append(roll)
    while len(rolls) < 6:
        roll = random.randint(1, 6)
        if roll not in rolls:
            rolls.append(roll)
            
        roll_count = roll_count + 1
        
    return roll_count



def average_until_six_different_values(num_trials):
    sum_results = 0
    for i in range(num_trials):
        result = tries_until_six_different_values()
        sum_results = sum_results + result
        
    return sum_results / num_trials

user_input = int(input('How many times would you like to run this function?: '))
print()    

print(tries_until_six_different_values())
print()

print(average_until_six_different_values(user_input))
print()
