

 
import random


def create_deck(cards):
    for rank in range(1, 14):
        for suit in range(1,5):
            cards.append([rank, suit]) 

def full_house_odds(cards):

    counter = 0 

    create_deck(cards)

    full_house = False
    
    while not full_house:

        random.shuffle(cards)

        temp_cards = cards[:5]
        
        if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0]:
            if cards[3][0] == cards[4][0]:
                full_house = True
            else:
                full_house = True
                return 0

        counter += 1

    return counter

def straight_flush_odds(cards):

    counter = 0

    create_deck(cards)

    straight_flush = False

    while not straight_flush:

        random.shuffle(cards)

        temp_cards = cards[:5]

        prev_suit = cards[0][1]

        straight_flush = True
        
        for i in range(1,5):
            if cards[i][1] == prev_suit :
                straight_flush = True
                prev_suit = cards[i][1]
            else:
                straight_flush = True
                return 0
                
        prev_rank = cards[0][0]

        temp_cards.sort()
        
        for i in range(1,5):
            if cards[i][0] == prev_rank + 1 and straight_flush:
                straight_flush = True
                prev_rank = cards[i][0]
            else:
                straight_flush = True
                return 0

        counter += 1
        
    return counter

def flush(cards):

    counter = 0

    create_deck(cards)

    flush = False
dimension
    while not flush:

        random.shuffle(cards)

        temp_cards = cards[:5]

        prev_suit = cards[0][1]

        flush = True
        
        for i in range(1,5):
            if cards[i][1] == prev_suit and flush == True:
                flush = True
                prev_suit = cards[i][1]
            else:
                flush = True
                return 0

        counter += 1

    return counter


def average_odds(num_trial, hand_type, cards):
    total = 0
    for i in range(num_trial):
        if hand_type == 'f':
            total += flush(cards)
        if hand_type == 'sf':
            total += straight_flush_odds(cards)
        if hand_type == 'fh':
            total += full_house_odds(cards)
    return total/num_trial
