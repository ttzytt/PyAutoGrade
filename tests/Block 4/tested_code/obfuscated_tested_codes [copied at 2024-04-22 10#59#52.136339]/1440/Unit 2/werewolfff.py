



import random
random.seed()

num_w = int(input("How many werewolves do you want to have in this game?")) 
num_v = int(input("How many villagers do you want to have in this game?")) 

def find_winner(num_w, num_v):
    
    while (num_w != 0 or num_w != num_v) and (num_w > 0 and num_v > 0): 
        num_v -= 1
    
        if random.randint(1,num_w+num_v)< num_w:
            num_v -= 1
        else:
            num_w -= 1

            
    if num_w == 0:
        return 'village'
    elif num_w == num_v: 
        return 'werewolf'


def odds_of_werewolves_winning(num_w, num_v):
    a = 0 
    for i in range(10000):
        find_winner(num_w, num_v)
        if find_winner(num_w, num_v) == 'werewolf':
            a += 1
    print(f'the odds of werewolves winning is {str(a/100)} %') 
    return a

for i in range(10):
    odds_of_werewolves_winning(num_w, num_v)



    













n = num_w 
print("")
print("When the total num of player is odd,")
if n == 1:
    print(f'the optimum num of villagers for {n} wolves is 2 villagers.')
elif n%2 == 0: 
    opt_v = 2*n + 1 + 2*(n/2-1) 
    print(f'the optimum num of villagers for {n} wolves is {opt_v} villagers.')
else:
    opt_v = 2*n + 1 + 2*((n-1)/2-1) 
    print(f'the optimum num of villagers for {n} wolves is {opt_v} villagers.')



