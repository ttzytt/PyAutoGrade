'''
Written by Alex
Reviewed by Ethan
DO NOT RUN THIS CODE
'''



import random
random.seed()
'''
# The original given numbers are from 1-52
# this function can sort them into 1-13 and corresponding figures (♠♥♦♣)
def sort_cards(list):
    for count in range(len(list)):
        if list[count] <= 13:
            list[count] = [list[count]%13,'♠']
        elif list[count] >= 14 and list[count] <= 26:
            list[count] = [list[count]%13,'♥']
        elif list[count] >= 27 and list[count] <= 39:
            list[count] = [list[count]%13,'♦']
        elif list[count] >= 40:
            list[count] = [list[count]%13,'♣']
    return list

# Giving 5 random cards and sort them
# (they are sorted from smallest number to largest number)
def give_cards():
    cards = []
    card = random.randint(1,52)
    while len(cards) < 5:
        if card not in cards:
            cards.append(card)
        card = random.randint(1,52)
    sort_cards(cards)
    cards.sort()
    return cards
'''

def give_cards():
    cards = []
    suit = random.choice(['♠','♥','♦','♣'])
    number = random.randint(1,13)
    card = [number,suit]
    while len(cards) < 5:
        if card not in cards:
            cards.append(card)
        suit = random.choice(['♠','♥','♦','♣'])
        number = random.randint(1,13)
        card = [number,suit]
    cards.sort()
    return cards


def find_full_house(cards):
    if cards[0][0] == cards[1][0] and cards[2][0] == cards[3][0] == cards[4][0]:
            return True
    elif cards[0][0] == cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]:
            return True
    return False


def find_consecutive(cards):
    for count in range(len(cards)):
        cards[count] = cards[count][0]
    for count in range(len(cards)-1):
        if abs(cards[count] - cards[count+1]) != 1:
            return False
    return True


'''
def find_consecutive(cards):
    if cards[0][0] == cards[1][0]+1 == cards[2][0]+2 == cards[3][0]+3 == cards[4][0]+4:
        return True
    elif cards[0][0] == cards[1][0]-1 == cards[2][0]-2 == cards[3][0]-3 == cards[4][0]-4:
        return True
    return False
'''

def find_straight_flush(cards):
    if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]:
        return find_consecutive(cards)
    return False


def find_flush(cards):
    if (cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]
        and find_consecutive(cards) == False):
        return True
    return False


def give_dices():
    dices = []
    dice = random.randint(1,4)
    while len(dices) < 5:
        dices.append(dice)
        dice = random.randint(1,4)
    return dices


def find_dices_flush(dices):
    if dices[0] == dices[1] == dices[2] == dices[3] == dices[4]:
        return True
    return False

