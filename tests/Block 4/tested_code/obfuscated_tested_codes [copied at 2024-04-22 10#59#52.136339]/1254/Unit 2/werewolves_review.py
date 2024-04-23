




import random
random.seed()



def find_winner(num_werewolves, num_villager):
    time = 'day' 
    while num_werewolves != 0 and num_werewolves < num_villager: 
         
        total_num = num_werewolves + num_villager
        if time == 'night': 
            num_villager -= 1
            time = 'day'
        else:
            chosen_kill = random.randint(1, total_num) 
            if chosen_kill <= num_werewolves: 
                num_werewolves -= 1
            else: 
                num_villager -= 1
            time = 'night'
    if num_werewolves == 0: 
        return 'villagers'
    elif num_werewolves >= num_villager: 
        return 'werewolves'


def odds_of_werewolves_winning(num_werewolves, num_villager):
    werewolf_win = 0
    for _ in range (10000): 
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolf_win += 1
    return (werewolf_win / 10000)


num_villager = int(input('How many villagers would you like? '))
num_werewolves = int(input('How many werewolves would you like? '))
print(odds_of_werewolves_winning(num_werewolves, num_villager))





'''
D: The probability of werewolves winning for both 101 and 99 villagers with the 4 wolves
were both lower than the probability with 100 villagers, this is because the total with 100 villager would be
an even number, causing the game have equal amounts of night and day giving the werewolves more definite
villager kills. Which in turn, increases the werewolves probability of winning.

E:
1. If there are 2 werewolves you would balance it by placing 17 or 19 villagers if the number of villagers are
odd or 28 to 30 villagers if the number of villagers are even. 
'''
