import random
random.seed()



def find_winner(num_wolves,num_villager):
    
    
    
    
    
    status = []
    for i in range(num_villager):
        status.append(1)
    for i in range(num_wolves):
        status.append(-1)
    
    
    for i in range(num_villager):
        
        status[random.randint(0,num_wolves+num_villager-1)] = 0
        
        
        if sum(status) == num_wolves + num_villager - 2*i - 1:
            return 'villager'
        if sum(status) == 0:
            return 'werewolves'
        
        status[i] = 0
        
        if sum(status) == 0:
            return 'werewolves'

def odds_of_werewolves_winning(num_werewolves, num_villager,nums = 100000):
    records = []
    for i in range(nums):
        if find_winner(num_werewolves,num_villager) == 'werewolves':
            records.append(1)
    return sum(records)/nums

wolves = int(input("wolves_number: "))
villager = int(input("villager_number: "))
print('The odds of werewolves wining is ' + str(odds_of_werewolves_winning(wolves, villager)))









