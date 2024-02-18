




from time import time
from operator import itemgetter
import random

random.seed()


def generate_deck():
    deck = []
    card = []
    for rank in range(1, 14):
        for suit in range(1, 5):
            card = [rank, suit]
            deck.append(card)
    return deck

deck = generate_deck()


def get_ms_time():
    return int(time() * 1000)







def has_full_house(hand):
    hand.sort()
    first_rank = hand[0]
    second_rank = hand[-1]
    
    return (hand == [first_rank, first_rank, first_rank, second_rank, second_rank]
        or hand == [first_rank, first_rank, second_rank,
                    second_rank, second_rank])








def has_straight_flush(hand, check_suit=True):
    hand.sort(key = itemgetter(1, 0)) 
    rank_correct = True
    suit_correct = True

    if check_suit:
        
        if hand[0][1] != hand[4][1]:
            return False
    
    
    ace_straight = [1, 10, 11, 12, 13]
    for i in range(5):
        if hand[i][0] != ace_straight[i]:
            rank_correct = False


    
    if not rank_correct:
        rank_correct = True
        if (hand[4][0] - hand[0][0]) != 4:
            rank_correct = False
            
    return (rank_correct and suit_correct)




def has_flush(hand):
    hand.sort()
    for i in range(4):
        if hand[i][1] != hand[i+1][1]:
            return False
    return True







def full_house_probability(deck):
    tries = 0
    is_full_house = False
    while not is_full_house:
        
        random.shuffle(deck)
        hand = []
        
        for i in range(5):
            hand.append(deck[i][0])
        tries += 1
    
        is_full_house = has_full_house(hand)
    return tries




def straight_flush_probability(deck):
    tries = 0
    is_straight_flush = False
    while not is_straight_flush:
        
        random.shuffle(deck)
        hand = deck[1:6] 
        tries += 1

        is_straight_flush = has_straight_flush(hand)

    return tries





def flush_probability(deck):
    tries = 0
    is_flush = False
    while not is_flush:
        
        random.shuffle(deck)
        hand = deck[1:6]
        tries += 1

        is_flush = (has_flush(hand) and not has_straight_flush(hand, False))
    return tries







def average_until_full_house(num_simulations, deck):
    
    sum_so_far = 0
    for i in range(num_simulations):
        sum_so_far += full_house_probability(deck) 
                                                   
    average = sum_so_far / num_simulations

    return average




def average_until_straight_flush(num_simulations, deck):
    
    sum_so_far = 0
    for i in range(num_simulations):
        sum_so_far += straight_flush_probability(deck) 
                                                       
    average = sum_so_far / num_simulations

    return average




def average_until_flush(num_simulations, deck):
    
    sum_so_far = 0
    for i in range(num_simulations):
        sum_so_far += flush_probability(deck) 
                                              
    average = sum_so_far / num_simulations

    return average







def has_dice_flush(hand):
    for roll in hand:
        if roll != hand[0]:
            return False
    return True


def dice_flush_probability():
    num_rolls = 0
    is_dice_flush = False
    while not is_dice_flush:
        
        set_of_rolls = []
        for i in range(5):
            set_of_rolls.append(random.randint(1, 4))            
        num_rolls += 1
        
        is_dice_flush = has_dice_flush(set_of_rolls)
    return num_rolls




def average_until_dice_flush(num_simulations):
    
    sum_so_far = 0
    for i in range(num_simulations):
        sum_so_far += dice_flush_probability() 
                                               
    average = sum_so_far / num_simulations

    return average


















print('Which simulation would you like to run? ')
get_simulation = input("Type 'fh' for full house, 's' for straight flush, " +
                       "'fl' for flush, 'd' for dice, or 'q' to quit: ")

while get_simulation != 'q':
    print()
    if get_simulation not in ['fh', 's', 'fl', 'd']:
        print('Invalid answer.')
    else:
        get_trials = input('How many times would you like to run the '
                           + 'simulation? ')
        while not get_trials.isnumeric():
            print()
            print('Invalid answer.')
            print()
            get_trials = input('How many times would you like to run the '
                               + 'simulation? ')
            
        
        
        print()
        if get_simulation == 'fh':
            start_time = get_ms_time()
            print('The odds of being dealt a full house is 1 in ' +
                  str(average_until_full_house(int(get_trials), deck)) + '.')
        elif get_simulation == 's':
            start_time = get_ms_time()
            print('The odds of being dealt a straight flush is 1 in ' +
                  str(average_until_straight_flush(int(get_trials), deck))
                  + '.')
        elif get_simulation == 'fl':
            start_time = get_ms_time()
            print('The odds of being dealt a flush is 1 in ' +
                  str(average_until_flush(int(get_trials), deck)) + '.')
        elif get_simulation == 'd':
            start_time = get_ms_time()
            print('The odds of rolling the same value from five 4 sided dice' +
                  ' is 1 in ' +
                  str(average_until_dice_flush(int(get_trials))) + '.')
            
        print('Took ' + str(get_ms_time() - start_time) + ' ms')

        
    print()
    print('Which simulation would you like to run? ')
    get_simulation = input("Type 'fh' for full house, 's' for straight flush" +
                       ", 'fl' for flush, 'd' for dice, or 'q' to quit: ")
    
print()   
print('Thanks for testing out the poker card probability shack!')

