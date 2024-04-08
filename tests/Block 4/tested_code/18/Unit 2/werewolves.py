



import random

def find_winner(num_werewolves, num_villagers):
    
    
    while num_werewolves > 0 and num_villagers > num_werewolves:
        
        
        
        total_players = num_werewolves + num_villagers
        
        
        killed_person = random.randint(1, total_players) 
        if killed_person <= num_werewolves: 
            num_werewolves -= 1
        else:
            num_villagers -= 1
            
        
        if num_werewolves > 0 and num_villagers > 0: 
            num_villagers -= 1

    
    if num_villagers <= num_werewolves:
        return 'werewolves'  
    else:
        return 'village'  

def odds_of_werewolves_winning(num_werewolves, num_villagers    werewolves_wins = 0
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






