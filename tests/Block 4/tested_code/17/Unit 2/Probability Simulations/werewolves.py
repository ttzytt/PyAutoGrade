







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
    
    if werewolves_win == 0:
        while werewolves_win == 0:
            time += 1
            if find_winner(num_werewolves, num_villager)=='werewolves':
                werewolves_win += 1
    
    return werewolves_win * 1.00 / time


print("Do you want to find winner or find the odds of werewolves winning?"
      + "(Type in 'find winner' or 'odds of werewolves winning')")
ans = input()
num_werewolves = int(input("How many werewolves do you want to have in simulation? "))
num_villager = int(input("How many villagers do you want to have in simulation? "))

if ans == "find winner":
    print("The winner: " + find_winner(num_werewolves, num_villager) + "!")
elif ans == "odds of werewolves winning":
    print("The odds for werewolves to win is " + str(odds_of_werewolves_winning(num_werewolves, num_villager)))


