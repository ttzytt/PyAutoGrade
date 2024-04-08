



import random

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






