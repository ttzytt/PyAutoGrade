'''
TASK 11
Written by Alex Zhu
Reviewed by Ethan Che
I did not receive help from my classmates
'''

'''Set Up'''
import random
random.seed()
num_werewolves = 4
num_villager = 100

'''Functions'''

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
        '''A common mistake is made when the result isn't previously defined'''
        
        if result == 'villagers':
            villagers += 1
            
        elif result == 'werewolves':
            werewolves += 1
        
    return (werewolves/2000)
    # It returns the chance of werewolves winning out of 2000 times
    # The actual results show that the chance of werewolves winning is a little bit higher than 50%
 
'''Main Part'''
print(odds_of_werewolves_winning(num_werewolves,num_villager))


'''Questions'''
'''
1. It takes about 28 or 30 villagers to balance the game with 2 werewolves.
(29 villagers doesn't work because it's an odd number)
2. When there is only one wolf left, 3 players are more likely to win
than 2 players
3. 1 wolf = 9 villagers; 2 wolves = 19 villagers; 3 wolves = 59 villagers
'''
