'''
TASK 11
Written by Alex
Reviewed by Ethan
I received help from Ethan
'''

'''Set Up'''
import random
random.seed()

'''Functions'''

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

'''Main Part'''

num_werewolves = int(input('Werewolves: '))
num_villager = int(input('Villager: '))
print(odds_of_werewolves_winning(num_werewolves,num_villager))

'''Questions'''
'''
1. It takes about 28 or 30 villagers to balance the game with 2 werewolves.
(29 villagers doesn't work because it's an odd number)
2. When there is only one wolf left, 3 players are more likely to win
than 2 players
3. 1 wolf = 9 villagers; 2 wolves = 19 villagers; 3 wolves = 59 villagers
'''
