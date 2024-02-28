


import random

def find_winner(num_werewolves, num_villagers):
    players = ['werewolf'] * num_werewolves + ['villager']* num_villagers

    while True:
        random.shuffle(players)
        killed = players.pop()

        if killed == 'werewolf'
