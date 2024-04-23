





'''
'''
from operator import itemgetter
import random
random.seed()



def is_full_house():
    

    rank_count = 0
    full_house = False
    
    while full_house == False:
        hands = make_deck()
        hands.sort()
        
        
        if((hands[0][0] == hands[1][0] == hands[2][0]
               and hands[3][0] == hands[4][0]) or (hands[0][0]==hands[1][0]
               and hands[2][0] == hands[3][0] == hands[4][0])):
            full_house = True
        rank_count += 1
    return rank_count
   
def full_house_odds_test(num_trials):
    simulation_count = 0
    for i in range(1, num_trials):
        simulation_count += is_full_house()
    return simulation_count/num_trials

def make_deck():
    
    ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    suits = ['♠','♥','♦','♣']
    deck = []


    for rank in ranks: 
        for suit in suits:
            deck.append([rank,suit]) 

    random.shuffle(deck) 
    return deck[:5:] 









def is_straight_flush():
    count = 0
    straight_flush = False
    
    while straight_flush == False:
        hands = make_deck()
        hands.sort()
        
        
        
        
        if hands[0][0] == 1:
            if(int(hands[0][0]) + 1 != int(hands[1][0])):
                   hands[0][0] = 1
        hands.sort()
        
        
        if(hands[0][1] == hands[1][1]
            and hands[0][1] == hands[2][1] 
            and hands[0][1] == hands[3][1]
            and hands[0][1] == hands[4][1]):
            straight_flush = True
        else:
            straight_flush = False
        count += 1
    return count

def straight_flush_odds_test(num_trials):
    simulation_count = 0
    for i in range(1, num_trials):
        simulation_count += is_straight_flush()
    return simulation_count/num_trials







def is_flush():
    count = 0
    flush = False
    
    while flush == False:
        hands = make_deck()
        hands.sort()
        
        if hands[0][0] == 1:
            if(int(hands[0][0]) + 1 != int(hands[1][0])):
                   hands[0][0] = 1
        hands.sort()
        
        if(int(hands[0][0]) + 1 == int(hands[1][0])
            and int(hands[2][0]) + 1 == int(hands[3][0])
            and int(hands[3][0]) + 1 == int(hands[4][0])): 
            if(hands[0][1] == hands[1][1]
                and hands[0][1] == hands[2][1]
                and hands[0][1] == hands[3][1]
                and hands[0][1] == hands[4][1]):
                flush = True
        else:
             flush = False
        count += 1
    return count

def straight_flush_odds_test(num_trials):
    simulation_count = 0
    for i in range(1, num_trials):
        simulation_count += is_flush()
    return simulation_count/num_trials

num_trials = int(input('Enter how many trials you want to go the simulation: '))
flush_odds = straight_flush_odds_test(num_trials)
print(f'The odds of being dealt a straight flush is 1 in {flush_odds}')

def generate_roll():
    dice_suits = ['♠','♥','♦','♣']
    dice_values = random.randint(1,4)
    dice_rolls = []
    
    for values in dice_values: 
        for suit in dice_suits:
            deck.append([value,suit]) 

    random.shuffle(deck) 
    print(dice_rolls)
    return dice_rolls[:5:] 


    
def is_four_side_dice():





    same_count = 0
    same_roll = False
    
    while same_roll == False:
        hands = generate_roll()
        hands.sort()
        
        
        if((hands[0][0] == hands[1][0] == hands[2][0]
               and hands[3][0] == hands[4][0]) or (hands[0][0]==hands[1][0]
               and hands[2][0] == hands[3][0] == hands[4][0])):
            same_roll = True
        same_count += 1
    return same_count
        
    
def straight_4_side_dice_test(num_trials):
    simulation_count = 0
    for i in range(1, num_trials):
        simulation_count += is_four_side_dice()
    return simulation_count/num_trials












    
