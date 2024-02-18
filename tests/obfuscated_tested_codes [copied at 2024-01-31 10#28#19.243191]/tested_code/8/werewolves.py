



import random

random.seed()





def find_winner(num_werewolves, num_villager):
    while (num_werewolves > 0):
        if (num_villager <= 0):
            return 'werewolves'
        num_villager -= 1 
        werewolf_or_villlager = random.randint(1, num_villager + num_werewolves)
        
        if (num_werewolves <= werewolf_or_villlager):
            num_werewolves -= 1 
        else:
            num_villager -= 1 

    return 'village'




def odds_of_werewolves_winning(num_werewolves, num_villager):
    werewolves_won = 0.0
    for i in range(100000):
        winner = find_winner(num_werewolves, num_villager)
        if(winner == 'werewolves'):
            werewolves_won += 1.0

    return werewolves_won / 100000.00
    
