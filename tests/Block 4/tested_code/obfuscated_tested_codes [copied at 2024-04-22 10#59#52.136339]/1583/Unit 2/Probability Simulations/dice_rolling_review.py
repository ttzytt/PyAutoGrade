




import random


random.seed()




def tries_until_all_rolls():
    num_rolls = 0
    rolled_values = []
    
    while len(rolled_values) < 6: 
        current_roll = random.randint(1, 6)
        if current_roll not in rolled_values: 
                                              
            rolled_values.append(current_roll)
        num_rolls += 1
        
    return num_rolls




def average_until_all_rolls(num_trials):
    
    
    
    
    sum_so_far = 0
    for i in range(num_trials):
        sum_so_far += tries_until_all_rolls() 
                                              
    average = sum_so_far / num_trials

    return average



while True:
    
    
    get_trials = int(
        input('How many times do you want to run the simulation? '))
    
    print('The average of the results is ' +
          str(average_until_all_rolls(get_trials)) + '.')


