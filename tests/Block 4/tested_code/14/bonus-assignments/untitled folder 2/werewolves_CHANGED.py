




from random import randint
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          





def find_winner(num_werewolves, num_villager):
    is_day = True
    while num_werewolves < num_villager and num_werewolves > 0:
        if is_day: 
            if randint(1, num_werewolves + num_villager) <= num_werewolves:
                
                num_werewolves -= 1
            else:
                num_villager -= 1
        else: 
            num_villager -= 1
        is_day = not is_day 
    if num_werewolves > 0:
        return 'werewolves'
    return 'village'

def odds_of_werewolves_winning(num_werewolves, num_villager, tries = 100):
    werewolves_wins = 0
    for _ in range(tries):
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolves_wins += 1
    return werewolves_wins / tries


while True:
    werewolves = input("Number of Werewolves: ")
    if not werewolves.isnumeric(): 
        print("not a number")
        werewolves = input("Number of Werewolves: ")
    werewolves = int(werewolves)
    villagers = input("Number of Villagers: ")
    if not villagers.isnumeric():
        print("not a number")
        villagers = input("Number of Villagers: ")
    villagers = int(villagers)
    tries = input("Number of Tries: ")
    if not tries.isnumeric():
        print("not a number")
        tries = input("Number of Tries: ")
    tries = int(tries)

    odds = odds_of_werewolves_winning(werewolves, villagers, tries)
    print("Odd of werewolves winning with", werewolves,
          "werewolves and", villagers, "villagers is",
          round(odds,4), "(",round(odds*100,2) ,"% )")
















