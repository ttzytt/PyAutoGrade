




import random

deck_cards = []





def create_deck(deck_cards):
    for rank in range(1, 14):
        
        for suit in range(1,5):
            deck_cards.append([rank, suit])








def full_house(deck_cards):
    
    random.shuffle(deck_cards)

    
    temp_cards = deck_cards[:5]

    
    temp_cards.sort()

    
    if temp_cards[0][0] == temp_cards[1][0]:
        if temp_cards[1][0] == temp_cards[2][0]:
            if temp_cards[3][0] == temp_cards[4][0]:
                
                return 1
    
    return 0




def straight_flush(deck_cards):

    random.shuffle(deck_cards)

    temp_cards = deck_cards[:5]

    
    for i in range(1,5):
        if temp_cards[i][1] != temp_cards[i - 1][1]:
            return 0
    temp_cards.sort()

    
    
    for i in range(1,5):
        if temp_cards[i][0] != temp_cards[i - 1][0] + 1:
            return 0

    return 1




def flush(deck_cards):

    random.shuffle(deck_cards)

    temp_cards = deck_cards[:5]

    
    for i in range(1,5):
        if temp_cards[i][1] != temp_cards[i - 1][1]:
            return 0
    return 1






def odds_hand(num_trial, hand_type, deck_cards):
    create_deck(deck_cards)

    total = 0
    
    for i in range(num_trial):
        if hand_type == 'f':
            total += flush(deck_cards)
        if hand_type == 'sf':
            total += straight_flush(deck_cards)
        if hand_type == 'fh':
            total += full_house(deck_cards)

    
    if hand_type == 'fh':
        total *= 2
    
    return ('There is one in a ' + str(num_trial/total) + ' chance of getting a ' + hand_type)

    
