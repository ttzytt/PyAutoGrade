


from operator import itemgetter
import random
random.seed()




def make_deck():

    full_deck = []

    for suit in ['♠', '♥', '♦', '♣']:
        for rank in range(1, 14):
            full_deck.append([rank, suit])

    return full_deck


def get_hand(full_deck):

    random.shuffle(full_deck)

    return full_deck[ :5]


def simulate_odds(is_target_hand):

    hand = get_hand(full_deck)
    count = 0
    
    while not is_target_hand(hand):
        count += 1
        hand = get_hand(full_deck) 
        
    return count


def average_until_target_hand(num_trials, is_target_hand):
    
    total = 0

    for i in range(num_trials):
        total += simulate_odds(is_target_hand)

    return total / num_trials




def is_full_house(hand):

    
    hand.sort(key = itemgetter(0))

    if hand[0][0] == hand[1][0] and hand[-1][0] == hand[-2][0]:   
        if hand[2][0] == hand[-2][0] or hand[2][0] == hand[1][0]:   
            return True

    return False




def is_straight_flush(hand):
    
    
    hand.sort(key = itemgetter(1))

    
    for i in range(len(hand) - 1):
        if hand[i][1] != hand[i + 1][1]:
            return False

    
    hand.sort(key = itemgetter(0))

    
    if hand[0][0] == 1  and \
       hand[1][0] == 10 and \
       hand[2][0] == 11 and \
       hand[3][0] == 12 and \
       hand[4][0] == 13:

        return True

    
    else:
        
        for i in range(len(hand) - 1):
            if hand[i][0] + 1 != hand[i + 1][0]:
                return False

    return True




def is_flush(hand):

    
    hand.sort(key = itemgetter(1))

    
    for i in range(len(hand) - 1):
        if hand[i][1] != hand[i + 1][1]:
            return False

    return True




def make_dice_rolls():

    rolls = []

    for i in range(5):
        rolls.append(random.choice(['♠', '♥', '♦', '♣']))

    return rolls


def is_same_suit(rolls):
    
    for i in range(len(rolls) - 1):
        if rolls[i] != rolls[i + 1]:
            return False

    return True


def simulate_5_same_suit_dice_odds(is_same_suit):

    rolls = make_dice_rolls()
    count = 0
    
    while not is_same_suit(rolls):
        count += 1
        rolls = make_dice_rolls()

    return count


def average_until_5_same_suit_dice(num_trials, is_same_suit):
    
    total = 0

    for i in range(num_trials):
        total += simulate_5_same_suit_dice_odds(is_same_suit)

    return total / num_trials


def simulate_dice_rolls():
    want_to_know_dice_odds = input('\nImagine you have a collection of 4-sided dice ' +
                               'in which the sides are labeled with the 4 suits. ' +
                               'Do you want to know, if you roll 5 dice, ' +
                               'the odds of rolling the same suit for all five?\n' +
                               'Yes / No\n').lower()

    if want_to_know_dice_odds == 'yes':
        print('\nThe odds is 1 in ' +
              str(int(average_until_5_same_suit_dice(num_trials, is_same_suit))) + '.')
    
    elif want_to_know_dice_odds == 'no':
        print('\nNo, you have to know.\n' +
              'The odds is 1 in ' +
              str(int(average_until_5_same_suit_dice(num_trials, is_same_suit))) + '.')




full_deck = make_deck()
user_choice = input('What type of hand do you want to dealt?\n' +
                    'a. Full House\n' +
                    'b. Straight\n' +   
                    'c. Flush\n').lower()

num_trials = int(input('Enter the number of trials: '))

if user_choice == 'a':

    print('\nThe odds of being dealt a full house is 1 in ' +
          str(int(average_until_target_hand(num_trials, is_full_house))) + '.')

elif user_choice == 'b':
    
    print('\nThe odds of being dealt a straight flush is 1 in ' +
          str(int(average_until_target_hand(num_trials, is_straight_flush))) + '.')

    simulate_dice_rolls()

else:

    print('\nThe odds of being dealt a straight flush is 1 in ' +
          str(int(average_until_target_hand(num_trials, is_flush))) + '.')

    simulate_dice_rolls()









