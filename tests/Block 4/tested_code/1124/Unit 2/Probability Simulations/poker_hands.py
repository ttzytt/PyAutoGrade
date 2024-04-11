





from operator import itemgetter

import random

random.seed()


def full_house_check(deck):
    random.shuffle(deck)

    hand = deck[0:5]

    
    
    
    ranks_of_hand = []
    
    for i in range(5):
        ranks_of_hand.append(hand[i][0])
        
    ranks_of_hand.sort()
    
    
    if ranks_of_hand[0] == ranks_of_hand[1]:
        if ranks_of_hand[2] == ranks_of_hand[3] == ranks_of_hand[4]:
            return True

    if ranks_of_hand[0] == ranks_of_hand[1] == ranks_of_hand[2]:
        if ranks_of_hand[3] == ranks_of_hand[4]:
            return True
        
    return False






def probability_full_house(num_trials):
    total = 0
    
    for _ in range(num_trials):
        
        full_house = False 
        number_of_tries = 0
        
        while full_house == False:

            if full_house_check(deck) == True:
                full_house = True
            
            number_of_tries += 1
        total += number_of_tries
    
    return round(total/num_trials)






def straight_flush_check(deck):
    
    random.shuffle(deck)
    hand = deck[0:5]
    
    
    hand.sort(key = itemgetter(1, 0))

    
    if hand[0][1] != hand[4][1]:
        return False

    
    
    if hand[0][0] == 1 and hand[1][0] == 10 and hand[2][0] == 11 and hand[3][0] == 12 and hand[4][0] == 13:
        return True
    if hand[4][0] - hand[0][0] != 4:
        return False
        
    return True





def probability_straight_flush(num_trials):
    total = 0
    
    for _ in range(num_trials):
        
        straight_flush = False
        number_of_tries = 0
        
        while straight_flush == False:
            if straight_flush_check(deck) == True:
                straight_flush = True

            number_of_tries += 1
        total += number_of_tries

    return round(total/num_trials)

    


def flush_check(deck):
    
    random.shuffle(deck)
    hand = deck[0:5]

    
    hand.sort(key = itemgetter(1, 0))
    
    
    if hand[0][1] != hand[4][1]:
        return False
    
    if hand[0][0] == 1 and hand[1][0] == 10 and hand[2][0] == 11 and hand[3][0] == 12 and hand[4][0] == 13:
        return False
    if hand[4][0] - hand[0][0] == 4:
        return False

    return True





def probability_flush(num_trials):
    total = 0
    
    for _ in range(num_trials):
        flush = False
        number_of_tries = 0
        while flush == False:
            
            if flush_check(deck) == True:
                flush = True

            number_of_tries += 1
        total += number_of_tries
    return round(total/num_trials)






def flush_comparison_check():
    rolls = []

    for _ in range(5):
        rolls.append(random.choice([1, 2, 3, 4]))
    
    
    rolls.sort()

    if rolls[0] != rolls[4]:
        return False

    return True






def probability_flush_comparison(num_trials):
    total = 0
    for _ in range(num_trials):
        flush = False
        number_of_tries = 0
        while flush == False:
            
            if flush_comparison_check() == True:
                flush = True

            number_of_tries += 1
        total += number_of_tries
    return round(total/num_trials)




deck = []
different_suits = ['♠', '♥', '♦', '♣']
for suit in different_suits:
    for i in range(13):
        deck.append([i+1, suit])
                    
num_trials = int(input('How many trials do you want?'))


print('Probability of full house is 1 in ' + str(probability_full_house(num_trials)) + '.')
print('Probability of straight flush is 1 in ' + str(probability_straight_flush(num_trials)) + '.')
print('Probability of flush is 1 in ' + str(probability_flush(num_trials)) + '.')
print('Probability of flush is 1 in ' + str(probability_flush_comparison(num_trials)) + '.')




'''R
Forgot to put the explanation of the flush comparison
Should add better spacing between functions and in the functions themselves
Some comments are too long
You should add more detail/comments in the last few functions(flush comparison and flush)
'''
