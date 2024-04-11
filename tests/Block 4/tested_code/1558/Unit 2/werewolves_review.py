


"""
A game a werewolves, wherethere is a number of villagers and werewolves. The game alternates
between day and night, starting at day. Each day, a random person is killed, they can be either
a werewolf or villager. During the night, one villager is killed. The game keeps going until
either all of the werewolves have been killed, which means the villagers win, or the number
of werewolves is the same as the number of villagers, which means the werewolves win. Comment
about the code at the bottom of the file
"""
import random
"""
function that simulates a game of werewolves depending on the starting conditions (number of
villagers and werewolves) and returns wither werewolves or village depending who won
"""
def find_winner(num_werewolves, num_villagers):
    werewolves_count = num_werewolves 
    villagers_count = num_villagers
    
    
    while werewolves_count > 0 and villagers_count >= werewolves_count:
        
        
        
        total_players = werewolves_count + villagers_count
        
        
        killed_person = random.randint(1, total_players) 
        if killed_person <= werewolves_count: 
            
            
            
            werewolves_count -= 1
        else:
            villagers_count -= 1
            
        
        if werewolves_count > 0 and villagers_count > 0: 
            villagers_count -= 1

    
    if villagers_count <= werewolves_count:
        return 'werewolves'  
    else:
        return 'village'  
"""
function that calls the previous function many times and returns the ratio of games that
the werewolves won as a decimal. Doesn't ask for a number of trials, but goes until the
werewolves have won 5 times and then divides that by the number of times it ran the game
"""
def odds_of_werewolves_winning(num_werewolves, num_villagers):
    werewolves_wins = 0
    num_trials = 0
    
    while werewolves_wins < 20: 
        winner = find_winner(num_werewolves, num_villagers)
    
        if winner == 'werewolves': 
            werewolves_wins += 1 
        num_trials += 1 

    return (werewolves_wins / num_trials) * 100 



num_werewolves = int(input("Enter the number of werewolves you would like: "))
num_villagers = int(input("Enter the number of villagers you would like: "))


werewolf_win = odds_of_werewolves_winning(num_werewolves, num_villagers)
print(f"The chance of the werewolves winning is approximately {werewolf_win:.4f}% ")


"""
When you run the program with 4 werewolves and 100 villagers the chance of the werewolves
winning is around 20-30%. When the program is run with 4 werewolves and 99 or 101 villagers
the chance of the werewolves winning is around 45-50% for both of them. This is interesting
because even when there are more werewolves than before (101) it results in a larger chance
the werewolves win. 
"""

"""
Villagers would prefer to have the total number of players odd because it is much harder for
the werewolves to win because only 2 people are eliminated each day so the werewolves would
another full day and night cycle to kill off a last villager, where in a game with an even
number of players the werewolves could kill off all the remanining villagers in one cycle.
"""

