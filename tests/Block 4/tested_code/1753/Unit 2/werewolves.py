






import random

random.seed()


def find_winner(num_werewolves, num_villager):
    while num_werewolves != 0:
        
        
        dead = random.randint(1, num_werewolves + num_villager)
        if dead <= num_werewolves:
            num_werewolves = num_werewolves - 1
        else:
            num_villager = num_villager - 1
            
        
        if num_werewolves >= num_villager:
            return 'werewolves'

        
        num_villager = num_villager - 1

        
        if num_werewolves >= num_villager:
            return 'werewolves'
        
    return 'village'

def odds_of_werewolves_winning(trials, num_werewolves, num_villager):
    werewolves = 0
    
    for trial in range(trials):
        find_winner(num_werewolves, num_villager)
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolves = werewolves + 1
            
    print(werewolves / trials)
    return werewolves / trials


user_repeat = 'yes'

while user_repeat == 'Yes' or user_repeat == 'yes' :
    user_trial_input = input('How many trials do you want to do? ')
    user_werewolves_input = input('How many werewolves do you want to have? ')
    user_villager_input = input('How many villagers do you want to have? ')
    
    odds_of_werewolves_winning(int(user_trial_input), int(user_werewolves_input), int(user_villager_input))

    print()

    
    user_repeat = input('Do you want to run this program again? ')



"""
------------------------------------- Answers to Question --------------------------------------

1: If the numnber of villagers is odd, to balance a game with 2 werewolves, 21 villagers are
   needed.If the numnber of villagers is even, to balance a game with 2 werewolves, 30 villagers are
   needed.
   
"""


