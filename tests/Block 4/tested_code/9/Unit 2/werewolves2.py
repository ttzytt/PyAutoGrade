


import random
random.seed()



def game_ended(num_werewolves, num_villager):
    
    if num_werewolves == 0:
        return 'village'
    
    elif num_werewolves == num_villager:
        return 'werewolves'
    
    return False



def find_winner(num_werewolves,num_villager):
    
    
    daycount = 1
    
    while game_ended(num_werewolves, num_villager) == False: 
        
        if daycount % 2 == 1: 
            
            total = num_werewolves + num_villager
            killed = random.randint(1,total)
            
            if killed <= num_werewolves:
                num_werewolves -= 1
                
            else:
                num_villager -= 1
                
        else: 
            num_villager -= 1
            
        daycount += 1
        
    if game_ended(num_werewolves, num_villager) != False:
        
        return game_ended(num_werewolves, num_villager)
        
def odds_of_werewolves_winning(num_werewolves,num_villager):
    
    village = 0
    werewolves = 0
    
    for count in range(2000):
        
        result = find_winner(num_werewolves,num_villager)
        
        if result == 'werewolves':
            werewolves += 1
        elif result == 'village':
            village += 1
            
    return werewolves/2000



num_werewolves = int(input('Werewolves: '))
num_villager = int(input('Villager: '))
print(odds_of_werewolves_winning(num_werewolves,num_villager))



