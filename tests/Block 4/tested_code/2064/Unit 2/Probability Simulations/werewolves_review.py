



import random

random.seed()


































def find_winner(num_werewolves, num_villager):
    while (num_werewolves > 0):
        if (num_villager <= num_werewolves):
            return 'werewolves'
        num_villager -= 1 
        if (num_villager <= 0):
            return 'werewolves'
        werewolf_or_villlager = random.randint(1, num_villager + num_werewolves)
        
        if (werewolf_or_villlager > num_werewolves):
            
            num_villager -= 1 
        else:
            num_werewolves -= 1 

    return 'village'




def odds_of_werewolves_winning(num_werewolves, num_villager):
    werewolves_won = 0.0
    for i in range(100000): 
        winner = find_winner(num_werewolves, num_villager)
        if(winner == 'werewolves'):
            werewolves_won += 1.0

    return werewolves_won / 100000.00
    



num_werewolves = int(input('Enter how many werewolves you want: '))
num_villager = int(input('Enter how many villagers you want: '))
percentage = odds_of_werewolves_winning(num_werewolves, num_villager)
print('There is a ' + str(percentage * 100) + '% chance of the werewolves winning')


