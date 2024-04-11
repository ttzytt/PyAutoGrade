



import random
random.seed


def tries_until_six_different_values():
    
    all_possibles = []
    
    
    count = 0

    
    while len(all_possibles) < 6:
        
        result = random.randint(1,6)
        
        
        if result not in all_possibles:
            all_possibles.append(result)
            
        count += 1
    return count


def average_until_six_different_values(num_trials):
    
    records = []
    
    
    for i in range(num_trials):
        records.append(tries_until_six_different_values())
        
    
    sum_ = 0
    
    for i in range(num_trials):
        sum_ += records[i]
    
    return sum_ / num_trials
    
