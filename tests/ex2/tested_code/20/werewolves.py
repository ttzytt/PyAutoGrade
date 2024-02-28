


import random


def find_winner(num_werewolves, num_villagers):

    if num_werewolves == num_villagers:
        return ('werewolves')
    elif num_werewolves == 0:
        return ('villagers')
    else:
        return None


def odds_of_werewolves_winning(num_werewolves, num_villagers):
    day_count = 0
    night = False
    while find_winner(num_werewolves, num_villagers) != 'werewolves':
        if not night:
            selection = random.randint(1,2)
            if selection ==  1:
                day_count += 0.5
            night = True
        elif night:
            num_villagers -= 1
            day_count += 0.5
            night = False

    return day_count






num_villagers = int(input('How many villagers do you want: '))
num_werewolves = int(input('How many werewolves do you want: '))
    
        
odds = odds_of_werewolves_winning(num_werewolves, num_villagers)  
print(f'{odds}')
