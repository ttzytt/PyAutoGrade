


import random





def find_winner(num_werewolves, num_villagers):
    werewolves = num_werewolves
    villagers = num_villagers
    
    
    players = ['werewolf'] * num_werewolves + ['villager'] * num_villagers

    while True:
        random.shuffle(players)
        killed = random.choice(players)



    
        if killed == 'werewolf':
            werewolves -= 1
        else:
            villagers -= 1
    
    
        if villagers == 0:
            return 'werewolves'
        elif werewolves == 0:
            return 'villagers'
        elif werewolves == villagers:
            return 'werewolves'



def odds_of_werewolves_winning(num_werewolves, num_villagers):
    
    num_trials = 100 



    werewolf_winning = 0

    
    
    for _ in range(num_trials):
        winner = find_winner(num_werewolves, num_villagers)

        if winner == 'werewolves':
            werewolf_winning += 1
    return werewolf_winning / num_trials 


def when_to_start():
    num_werewolves = int(input("Enter the number of werewolves: "))
    
    num_villagers = int(input("Enter the number of villagers: "))
    


    winner = find_winner(num_werewolves, num_villagers)
    print("The winner is:", winner)

    odds = odds_of_werewolves_winning(num_werewolves, num_villagers)
    print("The odds of werewolves winning are:", round(odds, 2))
    


when_to_start() 
