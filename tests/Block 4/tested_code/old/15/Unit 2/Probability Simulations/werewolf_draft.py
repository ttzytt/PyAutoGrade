
import random
random.seed()

num_werewolves = input(' What is the number of werewollves ')
num_villagers = input(' What is the number of villagers ')



num_villager = num_villager - 1

if num_villagers <= num_werewolves:
    print(' werewolves win ')
    break
    

    

num_participants = num_werewolves + num_villagers


die_roll = random.randint(1, num_participants)
if die_roll <= num_villagers:
    num_villagers = num_villagers - 1
    if num_villagers <= num_werewolves:
        print(' werewolves win ')
        break
else:
    num_werewolves = num_werewolves - 1
    if num_werewolves == 0:
        print(' villagers win ')
        break




if num_werewolves == 0:
    print(' villagers win ')
elif num_villagers <= num_werewolves:
    print(' werewolves win ')


    
