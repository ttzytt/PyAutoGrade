
















import random
random.seed()

werewolf_wins = 0
villager_wins = 0


def find_winner(num_werewolves, num_villagers):
    winner = False

    
    
    while winner != True:
        
        
        
        villager_or_werewolf = random.randint(1,num_werewolves + num_villagers)

        if villager_or_werewolf <= num_werewolves:
            num_werewolves -= 1
        else:
            num_villagers -= 1
        
        if num_villagers > num_werewolves and num_werewolves != 0:
            num_villagers -= 1

        
        if num_werewolves == num_villagers:
            winner = True
            return 'werewolves'
        
        elif num_werewolves <= 0:
            winner = True
            return 'villagers'






def odds_of_werewolves_winning(num_werewolves, num_villagers):
    werewolf_wins = 0
    villager_wins = 0
    
    for i in range(num_trials):
        if find_winner(num_werewolves, num_villagers) == 'werewolves':
            werewolf_wins += 1

    print(str(werewolf_wins) + ':' + str(num_trials))
    return werewolf_wins / num_trials

num_trials = int(input('How many times would you like it to run?'))
num_werewolves = int(input('How many werewolves?'))
num_villagers = int(input('How many villagers?'))
print('The ratio of werewolves winning is: ')
print('As a decimal it is: ' + str(odds_of_werewolves_winning(num_werewolves, num_villagers)))


