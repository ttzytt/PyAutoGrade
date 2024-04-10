




import random
random.seed()






def find_winner(num_werewolf, num_villager):

    if num_werewolf == 0:
        return 'villager'
    elif num_werewolf >= num_villager:
        return 'werewolf'
    else:
        return None



def one_simulation(num_werewolf, num_villager):

    while find_winner(num_werewolf, num_villager) is None: 
        num_villager -= 1 

        if find_winner(num_werewolf, num_villager) is None: 

            num_total = num_werewolf + num_villager
            day_kill = random.randint(1, num_total) 

            if day_kill <= num_werewolf: 
                num_werewolf -= 1
            else:
                num_villager -= 1 

            if find_winner(num_werewolf, num_villager) is not None: 
                return find_winner(num_werewolf, num_villager)
            

        else: 
            return find_winner(num_werewolf, num_villager)




def odds_of_werewolves_winning(num_villager, num_werewolf, num_simulation):

    num_werewolf_win = 0
    
    for i in range(num_simulation):
        if one_simulation(num_werewolf, num_villager) == 'werewolf':
            num_werewolf_win += 1 

    return (num_werewolf_win / num_simulation) 





num_villager = int(input('How many villagers would you like to start with? '))
num_werewolf = int(input('How many werewolves would you like to start with? '))
print("You're starting with " + str(num_villager) + " villagers and ") 
print(str(num_werewolf) + " werewolves.")
num_simulation = int(input('How many times of simulation would you like to have? '))
print("You're doing " + str(num_simulation) + " times of simulation.")
print("The simulations are starting with night first.")
print("The odds of werewolves winning is " + str(odds_of_werewolves_winning(num_villager, num_werewolf, num_simulation)))
