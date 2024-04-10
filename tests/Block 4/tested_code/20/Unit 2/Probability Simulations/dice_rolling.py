


import random
random.seed()



def tries_until_duplicate_dices():

    

    dices = []

    
    
    dice = random.randint(1,6) 
            
    while dice not in dices:
        dices.append(dice)
        dice = random.randint(1,6)    
    return len(dices) + 1



def avg_tries_until_duplicate_dices(num_trial):

    
    
    dices = []

    
    for i in range(num_trial):
        dices.append(tries_until_duplicate_dices())
    sum_dices = sum(dices)
    avg_dices = round(sum_dices/len(dices),2)
    return avg_dices



num_trial = int(input("How many trials do you want to do?"))
print(avg_tries_until_duplicate_dices(num_trial))





