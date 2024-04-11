


import random
random.seed


def relative_prime(number_1,number_2):
    
    calculate =[number_1,number_2]
    
    while calculate[0] * calculate[1] != 0 and min(calculate[0],calculate[1]) != 1:
        if calculate[0] > calculate[1]:
            calculate[0] = calculate[0] % calculate[1]
        else:
            calculate[1] = calculate[1] % calculate[0]
    return not (calculate[0] * calculate[1] == 0)

def trials(lower_limit,upper_limit,num_trials):
    
    result = 0
    
    for i in range(num_trials):
        
        number_1 = random.randint(lower_limit,upper_limit)
        number_2 = random.randint(lower_limit,upper_limit)
        
        if relative_prime(number_1,number_2) == True:
            result += 1
    return result/num_trials


            






