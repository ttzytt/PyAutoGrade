



import random

random.seed()






def find_winner(num_werewolves, num_villager):

    
    

    while num_werewolves > 0 and num_villager != num_werewolves and num_villager > 0:
        
        
        

        num_total = num_werewolves + num_villager

        
        if random.randint(0, num_total) < num_werewolves:
            num_werewolves -= 1
            
            
            
            if num_werewolves == num_villagers:
                return 'werewolves'
            elif num_werewolves == 0:
                return 'village'
        else:
            num_villager -= 1
            if num_werewolves == num_villagers:
                return 'werewolves'
            elif num_werewolves == 0:
                return 'village'
    
        num_villager -= 1

        if num_werewolves == num_villagers:
            return 'werewolves'
        elif num_werewolves == 0:
                return 'village'
        
        
    
    if num_werewolves > 0:
        return 'werewolves'
    else:
        return 'village'
        

def one_in_werewolves_winning(num_werewolves, num_villager):

    werewolve_wins = 0

    while find_winner(num_werewolves, num_villager) != 'village':
        werewolve_wins += 1
        
        
    return ('the odds of village winning in one in ' + str(werewolve_wins))




def odds_of_werewolves_winning(num_werewolves, num_villager, num_trial):

    werewolve_wins = 0

    for i in range(num_trial):
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolve_wins += 1

    return('The werewolves won ' + str(werewolve_wins/num_trial * 100) + '% of the games')
        



while True:

    num_trial = int(input('how many times u wanna run: '))

    num_werewolves = int(input('num werewoles: '))
    num_villagers = int(input('num villagers: '))

    print(odds_of_werewolves_winning(num_werewolves, num_villagers, num_trial))


