





'''
The code isn't very fast so it might take some time to generate the probabilities
especially with straight flush. If running 500+ trials straight flush might
take upwards of 5-7 minutes to run. The other tasks should run relatively quick.
'''

from operator import itemgetter
import random
random.seed()


def make_deck():
    #Ace is 1 and rank is the number while suit is the heart, clover, etc
    ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    suits = ['♠','♥','♦','♣']
    deck = []


    for rank in ranks: #Creates decks by adding values into deck
        for suit in suits:
            deck.append([rank,suit]) 

    return deck


def make_hand(deck):
    random.shuffle(deck)
    return deck[:5]


'''
Runs a simulation that will calculate the odds of being dealt a full house
(two of one rank and three of another rank) when being dealt 5 cards
'''
def num_until_full_house(deck):
    #keeps track of how many times it will have to go through loop

    tries_until_full_house = 0
    full_house = False
    
    while full_house == False:
        #Takes 5 cards from the deck and makes the hand
        hand = make_hand(deck) 
        hand.sort()
        #The first part checks if the first 3 are the same and the last 2 are the same
        #The second part checks if thee first 2 are the same and the last 3 are the same
        if (hand[0][0] == hand[1][0]
               and hand[2][0] == hand[3][0]
               and hand[2][0] == hand[4][0]):
            full_house = True
        elif (hand[0][0]==hand[1][0]
               and hand[0][0] == hand[2][0]
               and hand[3][0]== hand[4][0]):
            full_house = True

        tries_until_full_house += 1
    return tries_until_full_house

   
def full_house_odds_test(num_trials):
    deck = make_deck() #Makes the deck
    simulation_count = 0
    for _ in range(num_trials):
        simulation_count += num_until_full_house(deck)
    return simulation_count/num_trials


'''
Runs a simulation that finds the odds of being dealt a straight flush.
five in a row of the same suit
Ace in this simulation is 1
'''

#R The odds of this one seems much higher than it should be
def num_until_straight_flush(deck):
    tries_until_straight_flush_count = 0
    straight_flush = False
    
    while straight_flush == False:
        #Random Deck
        hand = make_hand(deck)
        hand.sort()
        #Check if rank of the lowest card is 1 (Ace)(special case).
        #Then checks if the next card is a 2 to see if its consequtive (1,2,3,4,5)
        #If second card isn't 2, then Ace will have a value of 14
        
        if hand[0][0] == 1:
            if((hand[0][0]) + 1 != (hand[1][0])):
                   hand[0][0] = 14
                   
                   hand.sort()
     
        
        
        if (hand[0][0] + 1 == hand[1][0]
                and (hand[1][0]) + 1 == (hand[2][0])
                and (hand[2][0]) + 1 == (hand[3][0])
                and (hand[3][0]) + 1 == (hand[4][0])): 
            if (hand[0][1] == hand[1][1]
                    and hand[0][1] == hand[2][1]
                    and hand[0][1] == hand[3][1]
                    and hand[0][1] == hand[4][1]):
                straight_flush = True

            
        tries_until_straight_flush_count += 1

    return tries_until_straight_flush_count

def straight_flush_odds_test(num_trials):
    deck = make_deck() 
    simulation_count = 0
    for _ in range(num_trials):
        simulation_count += num_until_straight_flush(deck)
    return simulation_count/num_trials


'''
Runs a simulation that finds the odds of being dealt a flush
(Any five cards of the same suit, but not a straight flush)
'''

def num_until_flush(deck):
    tries_until_flush_count = 0
    flush = False
    
    while flush == False:
        hand = make_hand(deck)
        hand.sort()
        
        
        
        
        if hand[0][0] == 1:
            if (hand[0][0]) + 1 != (hand[1][0]):
                   hand[0][0] = 14
                   
                   hand.sort()
        
        
        if (hand[0][1] == hand[1][1]
            and hand[0][1] == hand[2][1]
            and hand[0][1] == hand[3][1]
            and hand[0][1] == hand[4][1]):
            if((hand[0][0]) + 1 == (hand[1][0])
                and (hand[2][0]) + 1 == (hand[3][0])
                and (hand[2][0]) + 1 == (hand[3][0])
                and (hand[3][0]) + 1 == (hand[4][0])): 
                flush = False
            else:
                flush = True
        tries_until_flush_count += 1
    return tries_until_flush_count

def flush_odds_test(num_trials):
    deck = make_deck() 
    simulation_count = 0
    for _ in range(num_trials):
        simulation_count += num_until_flush(deck)
    return simulation_count/num_trials

'''
Runs a simulation that will roll a 4 sided dice (1,2,3,4)
and will label them with the 4 suits
It will find the odds of rolling the same suit for all of them
'''
def generate_roll():
    dice_suits = ['♠','♥','♦','♣']
    random.shuffle(dice_suits)
    return dice_suits[0]


    
def is_four_side_dice():
    num_until_same_count = 0
    same_rolls = False
    while same_rolls == False:
        roll = []
        count = 0
        
        while count <= 5:
            
            rolls = generate_roll()
            roll.append(rolls)
            count += 1
        num_until_same_count += 1
        
        if(roll[0] == roll[1]
            and roll[0] == roll[2] 
            and roll[0] == roll[3]
            and roll[0] == roll[4]):
            same_rolls = True

    return num_until_same_count
        

def straight_4_side_dice_test(num_trials):
    simulation_count = 0
    for _ in range(num_trials):
        simulation_count += is_four_side_dice()
    return simulation_count/num_trials

'''
The dice roll can easily be calculated by doing 1/(4^4) to find the odds of rolling
the same suit. This odd is significantly lower than straight flush and flush
because the ranks don't have to be consequtive nor the same. In terms of the code
it also runs much faster probably due to the fact it doesn't need to compute as many
simulations as in straight flush
'''


num_trials = int(input('Enter how many trials you want to go through: '))
full_house_odds = full_house_odds_test(num_trials)
print(f'The odds of being dealt a full house is 1 in {full_house_odds}') 

flush_odds = flush_odds_test(num_trials)
print(f'The odds of being dealt a flush is 1 in {flush_odds}')

dice_odds = straight_4_side_dice_test(num_trials)
print(f'The odds of rolling four same suits on 5 four sided dice is 1 in {dice_odds}')

straight_flush_odds = straight_flush_odds_test(num_trials)
print(f'The odds of being dealt a straight flush is 1 in {straight_flush_odds}')    
