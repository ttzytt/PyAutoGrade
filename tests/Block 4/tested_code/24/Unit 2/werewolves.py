




import random
random.seed()


def find_winner():
    num_werewolves = 4
    num_villager = 100
    winner = False
    day_count = 0

    
    while winner == False:
        if num_werewolves == num_villager:
            winner = True
            return "werewolves"
        elif num_werewolves == 0:
            winner = True
            return "village"
        else:
            winner = False
            
        
        if day_count % 2 == 0:
            villager_or_werewolves = random.randint(1, num_werewolves + num_villager)
            if villager_or_werewolves > num_werewolves:
                num_villager -= 1
            else:
                num_werewolves -= 1
        
        elif day_count % 2 != 0:
            num_villager -= 1
        day_count += 1


def odds_of_werewolves_winning(num_trials):
    werewolves = 0
    village = 0
    
    for _ in range(num_trials):
        result = find_winner()
        if result == 'werewolves':
            werewolves += 1
        elif result == 'village':
            village += 1

    
    werewolves_odds = werewolves/num_trials
    village_odds = village/num_trials
    
    return ('Werewolves odds: ' + str(werewolves_odds), 'Village odds: ' + str(village_odds))

num_trials = int(input('Input how many times the function run: '))
print(odds_of_werewolves_winning(num_trials))




