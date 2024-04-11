




import random

def rolls_until_all_values():
    
    rolled_values = set()
    rolls = 0

    while len(rolled_values) < 6:
        
        roll = random.randint(1, 6)
        rolls += 1

        
        rolled_values.add(roll)

    return rolls

def average_rolls_until_all_values(num_trials):
    
    total_rolls = 0

    for _ in range(num_trials):
        total_rolls += rolls_until_all_values()

    average_rolls = total_rolls / num_trials
    return average_rolls

def run_simulation():
    
    num_trials = int(input("Enter the number of trials: "))

    
    average = average_rolls_until_all_values(num_trials)
    print(f"Average number of rolls needed to cover all six values: {average}")

run_simulation()
