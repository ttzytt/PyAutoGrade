





import random
random.seed()

def tries_until_different_values():
    dice = [0,0,0,0,0,0] 
    i = 0
    while True:
        a = random.randint(0, 5) 
        if dice != [1,1,1,1,1,1]: 
            dice[a] = 1
            i += 1
            
        else:
            return i 

def average_until_different_values(num_trials):
    f = 0 
    for _ in range(num_trials):
        f += tries_until_different_values()
    return f / num_trials * 1.00 

num_trial = input("How many trials do you want to have? ")


j = average_until_different_values(int(num_trial))

print("The average amount of rolling we need to have to have rolled six different values is "
        + str(j))


