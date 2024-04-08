







import random
random.seed()



def tries_until_all_six():
    
    tries_value = []
    value = random.randint(1,6)
    count = 0

    
    while len(tries_value) != 6:
        if value not in tries_value:
            tries_value.append(value)
        value = random.randint(1,6)

        
        
        
        count = count + 1

    return count




def average_until_all_six(num_trails):
    sum_tries = 0

    for _ in range(num_trials):
        sum_tries = sum_tries + tries_until_all_six()

    return (sum_tries / num_trails)


num_trials = int(input('How many trails do you want to have? '))
print(average_until_all_six(num_trials))


    
        
