


import random
random.seed()


def find_winner(num_werewolves, num_villager):

    
    
    num_werewolves = int(num_werewolves)
    num_villager = int(num_villager)

    
    
    
    while num_werewolves != 0 and num_werewolves != num_villager and num_villager != 0:

        
        
        
        
        list_of_people = []
        for i in range(num_werewolves):
            list_of_people.append('w')
        for i in range(num_villager):
            list_of_people.append('v')

        
        person_to_be_removed = random.choice(list_of_people)

        if person_to_be_removed == 'v':
            num_villager -= 1
            
            if num_villager == num_werewolves:
                return "Werewolves"
        elif person_to_be_removed == 'w':
            num_werewolves -= 1
            
        num_villager -= 1

    
    if num_werewolves == 0:
        return "Villagers"
    elif num_werewolves == num_villager:
        return "Werewolves"


def odds_of_werewolves_winning(num_werewolves, num_villager):

    
    
    villager_wins = 0
    werewolves_win = 0

    
    
    
    for i in range(10000):
        if find_winner(num_werewolves, num_villager) == "Werewolves":
            werewolves_win += 1

    
    return werewolves_win/(10000)
            



num_werewolves = input("How many werewolves to start? ") 
num_villagers = input("How many villagers to start? ")


print("The odds of werewolves winning is:" + str(odds_of_werewolves_winning(num_werewolves, num_villagers)))







