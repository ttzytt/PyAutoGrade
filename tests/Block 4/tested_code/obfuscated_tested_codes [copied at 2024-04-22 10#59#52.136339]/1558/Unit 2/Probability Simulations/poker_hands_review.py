


"""
I did not receive help or look up
information other than from the teacher and the course materials.
"""

"""
Set of simulations which generate hands from a deck of card and calculate the odds of
different poker hands and dice rolls. Asks the user for an input of how many trials to go
through. Goes through full house odds, straight flush odds, flush odds, and rolling 5 4 sided
die with the four suits on the,. Prints all the odds at the end rounded to 3 decimal places
"""

import random
random.seed()

"""
Makes a full deck of cards from the rank and suit
"""
def make_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = [] 
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit]) 
    return deck



    
"""
Simulation that calculates the odds of being dealt a full house
two of one rank and three of another
"""
def full_house_odds(num_trials):
    deck = make_deck()
    full_house_count = 0 

    for trial in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]

        
        ranks = [card[0] for card in hand] 
        unique_ranks = set(ranks) 

        if len(unique_ranks) == 2: 
                                   

            for rank in unique_ranks:

                
                count_ranks = sum(card[0] == rank for card in hand) 
                if (count_ranks == 3 or count_ranks == 2): 

                    full_house_count += 1 
                    
                    break 
                          
                           

    if full_house_count == 0: 
        return 0
     
    chances = num_trials/full_house_count 
    return chances


"""
Simulaition that calculates the odds of being dealt a straight flush, five in a
row, all the same suit. An ace can count as below a 2 or above a king but not
both. User inputs how many times the program runs to create an accurate average. 
"""
def straight_flush_odds(num_trials):
    deck = make_deck()
    straight_flush_count = 0

    for trial in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]

        
        ranks = [card[0] for card in hand] 
        ranks.sort() 
                     

        suits = [card[1] for card in hand]
        unique_suits = set(suits) 

        if len(unique_suits) == 1: 
            
            if ranks[0] == 1 and ranks[-1] == 13:
                ranks[0] = 14
                ranks.sort() 
                
            for i in range(len(ranks) - 1):
                straight_flush_count += 1 
                if ranks[i] != ranks[i + 1] - 1: 
                    straight_flush_count -= 1
                    break
                

    if straight_flush_count == 0: 
        return 0
     
    chances = num_trials/straight_flush_count 
    return chances 

"""
Simulation that calculates the odds of being dealt a flush, any five cards of the
same suit but not in a row. User inputs how many times the program runs to create
an accurate average. 
 """
def flush_odds(num_trials):
    deck = make_deck()
    flush_count = 0

    for i in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]
      
        suits = [card[1] for card in hand]
        unique_suits = set(suits) 

        if len(unique_suits) == 1:
            flush_count += 1 
        
        
    if flush_count == 0: 
        return 0
     
    chances = num_trials/flush_count 
    return chances

"""
Simulation where five four-sided die are rolled, where each side is one of the 4 suits and at
the end calculates the odds of rolling the same suit for all five. User inputs how many times
the program runs to create an accurate average. 
"""
def same_suit_odds(num_trials):
    same_suit_count = 0
    
    for trial in range(num_trials): 
        rolls = []
        
        for i in range(5):
            rolls.append(random.choice([1, 2, 3, 4])) 
        rolls.sort()
        
        if rolls[0] == rolls[4]: 
            same_suit_count += 1

        

    if same_suit_count == 0:  
        return 0
        

    chances = num_trials / same_suit_count 
    return chances
    
    
"""
Asks user how any trials they want and prints all of the odds at the end. Prints the odds it
the format "The odds of getting a _ are approximately one in _" 
"""

num_trials = int(input("Enter the number of trials: "))

chances_fho = full_house_odds(num_trials) 
print(f"The chances of getting a full house are approximately one in {chances_fho:.3f}")

chances_sfo = straight_flush_odds(num_trials) 
print(f"The chances of getting a straight flush are approximately one in {chances_sfo:.3f}")

chances_fo = flush_odds(num_trials) 
print(f"The chances of getting a flush are approximately one in {chances_fo:.3f}")


"""
Getting 5 dice to roll to the same side is more probable than the flush because the deck has more things to choose
from than the 4 sided dice. it is also more probable than the straight flush because the chance of all the cards
having the same suit is already more improbable than the dice roll and the cards also have to be in order. 
"""


