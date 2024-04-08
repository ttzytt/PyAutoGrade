





from operator import itemgetter
import random
random.seed()


def deal_five_cards(deck):
    random.shuffle(deck) 
    return deck[0:5]  


def is_full_house(hand):
    
    hand.sort(key=itemgetter(0))
    
    return (hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] and
            (hand[2][0] == hand[1][0] or hand[2][0] == hand[4][0]))


def is_straight(hand):
    
    hand.sort(key=itemgetter(0))    
    
    return ( hand[2][0] == hand[1][0]+1 and hand[3][0] == hand[2][0]+1 and hand[4][0] == hand[3][0]+1 ) and ( ( hand[1][0] == hand[0][0]+1 ) or ( hand[0][0] == 1 and hand[1][0] == 10) )


def is_flush(hand):
    return hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)
    

def tries_until_full_house(deck):
    tries = 0
    hand = deal_five_cards(deck)
    
    while not is_full_house(hand) and tries < 5000:
        tries += 1 
        hand = deal_five_cards(deck) 
    return tries
    

def average_tries_full_house(num_trials):
    total_tries_until_full_house = 0
    for _ in range(num_trials):  
        total_tries_until_full_house += tries_until_full_house(deck)  
    return int(total_tries_until_full_house / num_trials)  

def tries_until_straight_flush(deck):
    tries = 0
    hand = deal_five_cards(deck)
    
    while not is_straight_flush(hand) and tries < 100000:
        tries += 1 
        hand = deal_five_cards(deck) 
    return tries

def average_tries_straight_flush(num_trials):
    total_tries_until_straight_flush = 0
    for _ in range(num_trials):  
        total_tries_until_straight_flush += tries_until_straight_flush(deck)  
    return int(total_tries_until_straight_flush / num_trials)  

def tries_until_flush(deck):
    tries = 0
    hand = deal_five_cards(deck)
    
    while not is_flush(hand) and tries < 5000:
        tries += 1 
        hand = deal_five_cards(deck) 
    return tries
    
def average_tries_flush(num_trials):
    total_tries_until_flush = 0
    for _ in range(num_trials):  
        total_tries_until_flush += tries_until_flush(deck)  
    return int(total_tries_until_flush / num_trials)  




deck = []
for rank in range(1, 14):
    for suit in ['♠', '♥', '♦', '♣']:
        deck.append([rank, suit])
        
num_trials = int(input('How many trials would you like to run (around 10, otherwise it takes a long time...): '))


print('Probability of getting a full house is 1 out of', average_tries_full_house(num_trials))
print('Probability of getting a straight flush is 1 out of', average_tries_straight_flush(num_trials))
print('Probability of getting a flush is 1 out of', average_tries_flush(num_trials))


