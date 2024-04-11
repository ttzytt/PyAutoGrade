



import random
random.seed()

def kill_day(num_werewolves, num_villager):
    total_people = num_werewolves + num_villager
    who_die = random.randint(1, total_people - 1)
    if who_die <= num_werewolves:
        num_werewolves -= 1
        return 'wolves'
    else:
        num_villager -= 1
        return 'villager'

