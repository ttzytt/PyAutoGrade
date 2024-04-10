


import random
random.seed



def tries_until_six_different_dice():
    dice = random.randint(1, 6) 
    values = [] 
    times = 0 
    while len(values) < 6: 
        
        times += 1
        if dice not in values: 
            values.append(dice)
        dice = random.randint(1, 6)
        
    print (times)
            


def average_until_six_different_dice(num_trails):
    time = 0 
    average = 0
    while (time < num_trails):
        dice = random.randint(1, 6) 
        values = [] 
        times = 0 
        while len(values) < 6: 
            
            times += 1
            if dice not in values: 
                values.append(dice)
            dice = random.randint(1, 6)
        average += times + 1 
        time += 1
        
    average /= time
    return average

