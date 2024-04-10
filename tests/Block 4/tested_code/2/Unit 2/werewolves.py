


import random
random.seed()


def find_current_winner(num_werewolves, num_villager):
    if num_werewolves == num_villager:
        return 'werewolves'
    elif num_werewolves == 0:
        return 'villager'
    else:
        return 'no one'


def find_winner(num_werewolves, num_villager):
    day_night = 1
    while True:
        if find_current_winner(num_werewolves, num_villager) != 'no one':
           return find_current_winner(num_werewolves, num_villager)
        
        if day_night % 2 != 0:
            total_people = num_werewolves + num_villager
            person_killed = random.randint(1, total_people)
            
            if person_killed <= num_werewolves:
                return find_winner(num_werewolves - 1, num_villager)
            else:
                return find_winner(num_werewolves, num_villager - 1)
        else:
            return find_winner(num_werewolves, num_villager - 1)
        day_night += 1




def odds_of_werewolves_winning(num_werewolves, num_villager):
    num_trials = 10000
    werewolf_wins = 0
    for i in range(num_trials):
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolf_wins += 1
    return werewolf_wins/num_trials
    
print('hi :)')
num_werewolves = int(input('number of werewolves: '))
num_villager = int(input('number of villager: '))
print(str(odds_of_werewolves_winning(num_werewolves, num_villager)))




