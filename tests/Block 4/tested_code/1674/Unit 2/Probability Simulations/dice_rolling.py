




import random

def rolls_until_all_values():
    
    rolled_values = []
    rolls = 0

    while len(rolled_values)<6:
        roll = random.randint(1, 6)
        if roll not in rolled_values:
            rolled_values.append(roll)
        rolls +=1

    return rolls

def average_rolls_until_all_values(num_trials):
    total_rolls = 0
    for _ in range(num_trials):
        total_rolls += rolls_until_all_values()

    average_rolls = total_rolls / num_trials + 1
    return average_rolls

def run_simulation():
    
    num_trials = int(input("Enter the number of trials: "))

    
    average = average_rolls_until_all_values(num_trials)
    print(f"Average number of rolls needed to cover all six values: {average}")

