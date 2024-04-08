



import random
random.seed()





def find_winner(num_werewolves, num_villagers):
    day_or_night = 'day'

    
    
    while num_werewolves != 0 and num_villagers != num_werewolves:
        total_players = num_villagers + num_werewolves

        
        
        if day_or_night == 'day':
            person_killed = random.randint(1, total_players)
            if person_killed <= num_werewolves:
                num_werewolves -= 1
            else:
                num_villagers -= 1
            day_or_night = 'night'

        elif day_or_night == 'night':
            num_villagers -= 1
            day_or_night = 'day'

    
    if num_werewolves == 0:
        return 'villagers'
    else:
        return 'werewolves'



def odds_of_werewolves_winning(num_werewolves, num_villagers):
    werewolf_wins = 0
    villager_wins = 0 
    for _ in range(10000):
        current_simulation = find_winner(num_werewolves, num_villagers)
        if current_simulation == 'werewolves':
            werewolf_wins += 1

        elif current_simulation == 'villagers': 
            villager_wins += 1

    return werewolf_wins/10000




num_werewolves = int(input('How many werewolves would you like? '))
print()
num_villagers = int(input('How many villagers would you like? '))
print()
odds_werewolf = odds_of_werewolves_winning(num_werewolves, num_villagers)
print(odds_werewolf)









