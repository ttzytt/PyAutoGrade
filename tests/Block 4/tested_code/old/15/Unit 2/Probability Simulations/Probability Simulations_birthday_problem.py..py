


import random

def tries_until_duplicate_birthday():
    birth = []
    while (True):
        month = random.randint(1,12)
        if(month == 2):
            day = random.randint(1,28)
        elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            day = random.randint(1,31)
        else:
            day = random.randint(1,30)
        
        MD = month*100+day
        if MD in birth :
            
            break
        else:
            birth.append(MD)
            
    
    return len(birth)+1
            
    
    

def average_until_deplicate_birthday(num_trials):
    Sum = 0
    for i in range(0, num_trials):
        Sum += tries_until_duplicate_birthday()
    
    return Sum/num_trials

x = int(input("How many times?"))




