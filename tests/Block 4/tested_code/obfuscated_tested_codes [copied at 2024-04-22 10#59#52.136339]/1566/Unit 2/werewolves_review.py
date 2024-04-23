






'''
Simulates a werewolve game where each day, a random person is killed (it might be a werewolf or a villager).
Each night, a villager is killed. The game alternates between day and night (starting with day),
until one of the following happens:
1. The werewolves have been killed. This means that the village wins.
2. The number of werewolves equals the number of villagers. This means that the werewolves
win.
'''
import random

def find_winner(num_werewolves, num_villagers):
    if num_werewolves == 0:
        return 'villagers'
    elif num_werewolves >= num_villagers:
        return 'werewolves'
    else:
        return None


def odds_of_werewolves_winning(num_werewolves, num_villagers):
    werewolves_wins_count = 0
    loop_count = 0
    
    
    while loop_count < 10000:
        
        current_num_werewolves = num_werewolves
        current_num_villagers = num_villagers
        
        while (find_winner(current_num_werewolves,current_num_villagers) != 'werewolves'
                and current_num_werewolves > 0 and current_num_villagers > 0):
            
            current_num_villagers -= 1
            
            
            random_kill = random.randint(1, current_num_werewolves + current_num_villagers)
            
            
            if random_kill <= current_num_werewolves:
                current_num_werewolves -= 1
            else:
                current_num_villagers -= 1
                
                        
        if find_winner(current_num_werewolves, current_num_villagers) == 'werewolves':
            werewolves_wins_count += 1
            
        loop_count += 1
    return werewolves_wins_count/loop_count



num_villagers = int(input('How many villagers do you want: '))
num_werewolves = int(input('How many werewolves do you want: '))
    
        
odds_of_werewolves_winning_probability = odds_of_werewolves_winning(num_werewolves, num_villagers)  
print(f'The odds of werewolves winning {odds_of_werewolves_winning_probability}')


'''
1. To balance a game with 2 werewolve, and odd number of villagers, the villager count would
be 11 or 13. For a even number of villagers, the number would be 20, 22 or 24.

'''
