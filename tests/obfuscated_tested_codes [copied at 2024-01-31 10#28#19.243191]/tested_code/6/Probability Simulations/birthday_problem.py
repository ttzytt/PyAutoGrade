



import random
random.seed

def tries_until_duplicate_birthday(include_leap_year=False):
    
    records = []
    
    
    if include_leap_year == False:
        days_per_year = 365
    else:
        days_per_year = 366
    
    number= random.randint(1,days_per_year)
    
    while number not in records:
        records.append(number)
        number = random.randint(1,days_per_year)
        
        if days_per_year == 366 and number == 366:
            
            randomness = random.randint(1,4)
            
            if randomness == 1:
                number = 366
            else:
                number = random.randint(1,365)
            
    
    return len(records) + 1


def average_until_duplicate_birthday(num_trials,include_leap_year=False):
    
    values = []

    
    for i in range(num_trials):
        values.append(tries_until_duplicate_birthday(include_leap_year))
    sum_ = 0
    
    for i in range(num_trials):
        sum_ += values[i]
    
    return(sum_/num_trials)
        
    
