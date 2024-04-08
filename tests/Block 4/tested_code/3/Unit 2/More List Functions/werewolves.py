




from werewolves_functions import * 



def find_winner(num_werewolves, num_villager):
    while num_werewolves != 0 and num_werewolves != num_villager:
        
        if num_villager == 0:
            return 'wolves'
        if kill_day(num_werewolves, num_villager) == 'wolves':
            num_werewolves -= 1
        else:
            num_villager -= 1

        if num_villager == 0:
            return 'wolves'
        
        num_villager -= 1 
        
    if num_werewolves == 0: 
        
        return 'villager'
    elif num_werewolves == num_villager: 
        
        return 'wolves'


def odds_of_werewolves_winning(num_werewolves, num_villager):
    wolves = 0
    villager = 0
    for i in range(1000):
        result = find_winner(num_werewolves, num_villager)
        if result == 'wolves':
            wolves += 1
        elif result == 'villager':
            villager += 1
    return wolves/1000


def player_is_the_god():
    num_werewolves = int(input('How many wolves do you want to have: '))
    num_villager = int(input('How many villagers do you want to have: '))
    result = find_winner(num_werewolves, num_villager)
    print(result + ' win. ')
    odds = odds_of_werewolves_winning(num_werewolves, num_villager)
    print('the probability for werewolves to win is ' + str(odds)) 









