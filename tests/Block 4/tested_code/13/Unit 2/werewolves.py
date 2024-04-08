


import random


def find_winner(num_werewolves, num_villagers):
    while num_werewolves > 0 and num_villagers > num_werewolves:
        
        if random.random() < num_villagers/(num_villagers+num_werewolves):
            num_villagers -= 1         
        else:
            num_werewolves -= 1
        num_villagers -= 1    

     return 'werewolves' if num_werewolves > 0 else 'village'



def odds_of_werewolves_winning(num_werewolves, num_villagers, num_simulations=1000000):
    werewolves_won = 0
    for i in range(num_simulations):
        winner = find_winner(num_werewolves, num_villagers)
        if winner == 'werewolves':
            werewolves_won += 1
    return werewolves_won / num_simulations


def odds_of_werewolves_winning(num_werewolves, num_villagers):
    num_simulations = 1000000
    werewolves_won = 0
    for i in range(num_simulations):
        winner = find_winner(num_werewolves, num_villagers)
        if winner == 'werewolves':
            werewolves_won += 1
    return werewolves_won / num_simulations





num_werewolves = int(input("Enter the number of werewolves: "))
num_villagers = int(input("Enter the number of villagers: "))

result = find_winner(num_werewolves, num_villagers)
print("The winner is:"+ result)

odds = odds_of_werewolves_winning(num_werewolves, num_villagers)
print("Odds of werewolves winning: " + str(round(odds, 2)))

























