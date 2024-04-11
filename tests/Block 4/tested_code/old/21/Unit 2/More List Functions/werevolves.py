
import random
random.seed()

import random



def find_winner(num_werewolves, num_villagers):
    werewolves = [num_werewolves]
    villagers = [num_villagers]
    choice = ['villagers', 'werewolves']
    
    
    while villagers[0] > 0 and werewolves[0] > 0:
        random.shuffle(choice)
        if choice[0] == 'villagers':
            werewolves[0] -= 1
        else:
            villagers[0] -= 1
    
        villagers[0] -= 1
    if villagers[0] == 0:
        return 'Villagers win'
    if werewolves[0] == 0:
        return 'Werewolves win'

def odds_of_werewolves_winning(num_werewolves, num_villagers):
    werewolf_win = 0
    villager_win = 0
    
    for _ in range(10000):
        win = find_winner(num_werewolves, num_villagers)
        if win == 'Villagers win':
            villager_win += 1
        elif win == 'Werewolves win':
            werewolf_win += 1
    
    return werewolf_win / 10000 


num_villager = int(input('How many villagers would you like? '))
num_werewolves = int(input('How many werewolves would you like? '))
print(odds_of_werewolves_winning(num_werewolves, num_villager))



