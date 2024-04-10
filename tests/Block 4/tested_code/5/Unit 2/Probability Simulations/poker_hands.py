

from poker_hand_functions import *




def odds_of_full_house():
    time = 1
    hand = get_cards()
    while find_full_house(hand) == False:
        time += 1
        hand = get_cards()
    print('The probability should be 1 in ' +  str(time))
    return time
            
        
def average_odds_of_full_house(times):
    total = 0
    for i in range(times):
        time = 1
        hand = get_cards()
        while find_full_house(hand) == False:
            time += 1
            hand = get_cards()
        total += time
    print('The average probability is 1 in ' + str(total / times))
    return total/times 



def odds_of_straight_flush():
    time = 1
    hand = get_cards()
    while find_straight_flush(hand) == False:
        time += 1
        hand = get_cards()
        find_straight_flush(hand)
    print('The probability should be 1 in ' +  str(time))
    return time

def average_odds_of_straight_flush(times):
    total = 0
    for i in range(times):
        time = 1
        hand = get_cards()
        while find_straight_flush(hand) == False:
            time += 1
            hand = get_cards()
            find_straight_flush(hand)
        total += time
    print('The average probability is 1 in ' + str(total / times))
    return times/total 



def odds_of_flush():
    time = 1
    hand = get_cards()
    while find_flush(hand) == False:
        time += 1
        hand = get_cards()
        find_flush(hand)
    print('The probability should be 1 in ' +  str(time))
    return time

def average_odds_of_flush(times):
    total = 0
    for i in range(times):
        time = 1
        hand = get_cards()
        while find_flush(hand) == False:
            time += 1
            hand = get_cards()
            find_flush(hand)
        total += time
    print('The average probability is 1 in ' + str(total / times))
    return times/total



def odds_of_dice_flush():
    time = 1
    cases = get_dice()
    while find_flush_dice(cases) == False:
        time += 1
        cases = get_dice()
        
    print('The probability should be 1 in ' +  str(time))
    return time

def average_odds_of_dice_flush(times):
    total = 0
    for i in range(times):
        time = 1
        cases = get_dice()
        while find_flush_dice(cases) == False:
            time += 1
            cases = get_dice()
            find_flush_dice(cases)
        total += time
    print('The average probability is 1 in ' + str(total / times))
    return times/total

def comparison(times):
    slope = average_odds_of_dice_flush(times)/ (average_odds_of_flush(times) + average_odds_of_straight_flush(times))
    print('their relationship is ' + str(slope) + ' times.')    
