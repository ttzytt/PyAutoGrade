



import random



def find_winner(num_werewolves, num_villager):

    
    people = []
    for i in range(num_werewolves):
        people.append('w')
    for i in range(num_villager):
        people.append('v')

    
    win = False
    while win == False:
        
        random.shuffle(people)
        people = people[1:]

        
        if people[0] == 'w':
            num_werewolves = num_werewolves - 1
        elif people[0] == 'v':
            num_villager = num_villager - 1

        if num_werewolves == 0:
            win = 'villagers'

        if num_werewolves == num_villager:
            win = 'werewolves'

        
        people.sort()
        people = people[1:]
        num_villager = num_villager - 1

        if num_werewolves == 0:
            win = 'villagers'

        if num_werewolves == num_villager:
            win = 'werewolves'

    return win



def odds_of_werewolves_winning(num_werewolves, num_villager):

    werewolf_win = 0
    
    for i in range(1000):
        win = find_winner(num_werewolves, num_villager)
        if win == 'werewolves':
            werewolf_win = werewolf_win + 1

    return (werewolf_win/1000)


num_werewolves = int(input("Number of werewolves: "))
num_villager = int(input("Number of villagers: "))
result = odds_of_werewolves_winning(num_werewolves, num_villager)
print("The odds of werewolves winning is " + str(result) + ".")












      


        

