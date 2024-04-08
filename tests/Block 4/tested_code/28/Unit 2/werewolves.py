





import random











def find_winner(num_werewolves, num_villager):
    phase_count = 0 
    while 0 < num_werewolves < num_villager:
        if phase_count % 2 == 0: 
            
            random_kill = random.randint(1, num_werewolves + num_villager)

            
            
            
            if random_kill <= num_werewolves: 
                                              
                num_werewolves -= 1
            else:
                num_villager -= 1

        else: 
            num_villager -= 1
        phase_count += 1

    if num_werewolves >= num_villager:
        return 'werewolves'
    return 'village'
    


def find_winner_2(num_werewolves, num_villager):
    phase_count = 0 
    while 0 < num_werewolves < num_villager:
        if phase_count % 2 == 0: 
            num_villager -= 1

        else: 
            
            random_kill = random.randint(1, num_werewolves + num_villager)

            
            
            
            if random_kill <= num_werewolves: 
                                              
                num_werewolves -= 1
            else:
                num_villager -= 1

        phase_count += 1

    if num_werewolves >= num_villager:
        return 'werewolves'
    return 'village'










def odds_of_werewolves_winning(num_werewolves, num_villager, tries = 100):
    games_won_by_werewolves = 0
    for i in range(tries):
        
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            games_won_by_werewolves += 1

    return games_won_by_werewolves / tries








get_tries = input("How many tries? Type 'q' to quit. ")

while get_tries != 'q':
    get_werewolves = input('How many werewolves? ')
    get_villagers = input('How many villagers? ')
    print()
    print('The odds of werewolves winning is '
          + str(odds_of_werewolves_winning(int(get_werewolves),
                                           int(get_villagers),
                                           int(get_tries)))
          + '.')
    print()
    get_tries = input("How many tries? Type 'q' to quit. ")

print()
print('Come again soon!')
