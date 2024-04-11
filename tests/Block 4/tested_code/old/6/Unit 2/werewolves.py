


import random



def find_winner(num_werewolves, num_villagers):

    while num_werewolves > 0 and num_werewolves < num_villagers:
        
        num_villagers -= 1

        if random.randint(1, num_werewolves + num_villagers) <= num_werewolves:
            
            num_werewolves -= 1
            
        else:
            
            num_villagers -= 1

    if num_werewolves >= num_villagers:

        winner = 'werewolves'

    else:
        
        winner = 'villages'

    return winner


def odds_of_werewolves_winning(num_werewolves, num_villagers, num_of_trials):

    werewolves_win = 0

    for i in range(num_of_trials):
        
        if find_winner(num_werewolves, num_villagers) == 'werewolves':
            
            werewolves_win += 1

    return werewolves_win / num_of_trials



num_werewolves = int(input('How many werewoles do you want to start with? '))
num_villagers = int(input('How many villagers do you want to start with? '))
num_of_trials = int(input('How many games do you want to simulate? '))
odds = odds_of_werewolves_winning(num_werewolves, num_villagers, num_of_trials)
print('The odds of werewolves winning is ' + str(odds) + '.')






