


import random

random.seed


deck = [] 
for suit in range(0, 4):
    for card_num in range(0, 13):
        deck.append([card_num, suit])

random.shuffle(deck)

def is_full_house(hand):
    hand = deck[0:5:1]
    hand.sort(key = itemgetter(0)) 
    
    if hand[0][0] == hand[1][0]: 
        if hand[2][0] == hand[3][0]== hand[4][0]:
            return hand
    elif hand[0][0] == hand[1][0] == hand[2][0]:
        if hand[3][0] == hand[4][0]:
            return hand
    

def full_house(deck):
    user_input = input('How many trials do you want to do: ')
    count = 0
    sum_so_far = 0
    for i in range(user_input):
        while not is_full_house(hand):
            count = count + 1
            random.shuffle(deck)
            
        sum_so_far += count
    average = (sum_so_far / user_input)
    return count
    
    
    print('The odd of getting a full house is 1 in' + str(average))

def is_straight_flush(hand):
    hand = deck[0:5:1]
    hand.sort(key = itemgetter(1))
    if hand[0][1] == hand[4][1]:
        if hand[4][0] - hand[0][0] == 4:
            return hand

def straight_flush(deck):
    user_input = input('How many trials do you want to do: ')
    count = 0
    sum_so_far = 0
    for i in range(user_input):
        while not is_straight_flush(hand):
            count = count + 1
            random.shuffle(deck)
        sum_so_far += count
    average = (sum_so_far / user_input)
    return count

    print('The odd of getting a straight flush is 1 in' + str(average))

def is_flush(hand):
    hand = deck[0:5:1]
    hand.sort(key = itemgetter(1))
    if hand[0][1] == hand[4][1]:
        if hand[4][0] - hand[0][0] != 4:
            return hand

def flush(deck):
    user_input = input('How many trials do you want to do: ')
    count = 0
    sum_so_far = 0
    for i in range(user_input):
        while not is_flush(hand):
            count = count + 1
            random.shuffle(deck)
            
        sum_so_far += count
    average = (sum_so_far / user_input)
    return count

    print('The odd of getting a flush is 1 in' + str(average))


