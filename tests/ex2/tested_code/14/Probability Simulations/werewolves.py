




import random
random.seed()

def find_winner(num_werewolves, num_villager):
    while num_werewolves != 0 and num_villager > num_werewolves:
        
        a = random.randint(1, num_werewolves + num_villager)
        if a > num_villager:
            num_werewolves -= 1
        else:
            num_villager -= 1

        
        num_villager -= 1

    if num_werewolves == 0:
        return 'village'
    else:
        return 'werewolves'

def odds_of_werewolves_winning(num_werewolves, num_villager):
    werewolves_win = 0
    time = 1000
    for _ in range(1000):
        if find_winner(num_werewolves, num_villager)=='werewolves':
            werewolves_win += 1
    if werewolves_win > 0:
        return werewolves_win * 1.00 / time
    else:
        while werewolves_win == 0:
            time += 1
            if find_winner(num_werewolves, num_villager)=='werewolves':
                werewolves_win += 1
        return werewolves_win * 1.00 / time
            
