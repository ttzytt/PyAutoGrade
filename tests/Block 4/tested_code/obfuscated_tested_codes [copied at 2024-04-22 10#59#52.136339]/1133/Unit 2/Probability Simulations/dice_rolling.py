



import random
def rolls_until_all_values():
    """
    Simulates the number of rolls needed until all six different values are rolled on a standard six-sided die.
    Returns:
    - int: Number of rolls needed to get all six different values.
    """
    
    rolled_values = []
    
    rolls_count = 0
    while len(rolled_values) < 6:
        
        roll = random.randint(1, 6)
        
        if roll not in rolled_values:
            rolled_values.append(roll)
        
        rolls_count += 1
    return rolls_count

def average_rolls_until_all_values(num_trials):
    """
    Calls rolls_until_all_values() multiple times and returns the average.
    Parameters:
    - num_trials (int): Number of trials to perform.
    Returns:
    - float: Average number of rolls needed to get all six different values across trials.
    """
    total_rolls = 0
    for _ in range(num_trials):
        total_rolls += rolls_until_all_values()
    return total_rolls / num_trials

if __name__ == "__main__":
    num_trials = int(input("Enter the number of trials: "))
    result = average_rolls_until_all_values(num_trials)
    print("Average number of rolls needed to get all six different values:", result)
