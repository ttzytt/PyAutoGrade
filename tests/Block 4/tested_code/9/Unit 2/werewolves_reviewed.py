


import random
random.seed()
num_werewolves = 4
num_villager = 100



def find_winner(num_werewolves, num_villager):

    
    
    while num_werewolves > 0 and num_villager > num_werewolves:
        
        killed = random.randint(1, num_villager + num_werewolves)
        
        
        if killed <= num_werewolves: 
            num_werewolves -= 1
        elif killed > num_werewolves: 
            num_villager -= 1
            
        num_villager -= 1 

    if num_werewolves == 0: 
        return 'villagers'
    
    elif num_villager == num_werewolves: 
        return 'werewolves'


def odds_of_werewolves_winning(num_werewolves, num_villager):
    
    werewolves = 0
    villagers = 0
    
    for count in range(2000): 
        
        result = find_winner(num_werewolves,num_villager) 
        
        
        if result == 'villagers':
            villagers += 1
            
        elif result == 'werewolves':
            werewolves += 1
        
    return (werewolves/2000)
    # It returns the chance of werewolves winning out of 2000 times
    # The actual results show that the chance of werewolves winning is a little bit higher than 50%
 

print(odds_of_werewolves_winning(num_werewolves,num_villager))




