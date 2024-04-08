


import random
random.seed



def get_cards():
    hand = []
    while len(hand) < 5:
        card = []
        rank = random.randint(1, 13)
        card.append(rank)
        
        suit = random.choice(['♠','♥','♦','♣'])
        card.append(suit)
        
        
        if card not in hand:
            
            hand.append(card)
        
    hand.sort()
    return hand


def find_full_house(hand):
    for i in range(len(hand)):
        hand[i] = hand[i][0]
        
    return ((hand[0] == hand[1] == hand[2] and hand[3] == hand[4])
            or (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]))


def find_straight_flush(hand):
    
    if (hand[0][1] == hand[1][1] == hand[2][1]
            == hand[3][1] == hand[4][1]):

        return (hand[0][0] + 4 == hand[1][0] + 3 == hand[2][0] + 2
                == hand[3][0] + 1 == hand[4][0])
    else:
        return False


def find_flush(hand):
    if (hand[0][0] + 4 == hand[1][0] + 3 == hand[2][0] + 2
            == hand[3][0] + 1 == hand[4][0]):
        return False
    else:
        return (hand[0][1] == hand[1][1] == hand[2][1]
                == hand[3][1] == hand[4][1]) 


def get_dice():
    cases = []
    while len(cases) < 5:
        suit = random.randint(1,4)
        cases.append(suit)
    return cases

def find_flush_dice(cases):
    return (cases[0] == cases[1] == cases[2] == cases[3] == cases[4])
