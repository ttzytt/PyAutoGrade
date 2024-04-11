




from operator import itemgetter 
import random 
random.seed()



def create_deck():
    deck = []
    for rank in range(1, 14):
        for suit in ['♥', '♦', '♣', '♠']:
            deck.append([rank, suit])
    return deck


def check_if_full_house(hand):
    hand.sort()
    if((hand[0][0] == hand[1][0]) and (hand[3][0] == hand[4][0])):
        if((hand[2][0] == hand[0][0]) or (hand[2][0] == hand[4][0])):
            return 1
    return 0



def check_if_straight_flush(hand):
    hand.sort(key = itemgetter(1))
    if not(hand[0][1] == hand[4][1]):
        return 0
    hand.sort()
    if((hand[0][0] == 1) and (hand[1][0] == 10) and (hand[2][0] == 11) and (hand[3][0] == 12)
       and (hand[4][0] == 13)):
        return 1
        
    for i in range(1, 5):
        if not(hand[0][0] + i  == hand[i][0]):
            return 0
    return 1



def check_if_flush(hand):
    for i in range(4):
        if (hand[i][1] != hand[i+1][1]):
            return 0
    if(check_if_straight_flush(hand) > 0):
        return 0
    return 1





def calculate_odds(type, num_success):
    success = 0
    times = 0
    deck = create_deck()
    
    while (success != num_success):
        hand = make_hand(deck)
        if (type == "flush"):
            success += check_if_flush(hand)
        elif (type == "straight flush"):
            success += check_if_straight_flush(hand)
        elif (type == "full house"):
            success += check_if_full_house(hand)
        times += 1

    return times/num_success


def make_hand(deck):
    random.shuffle(deck)
    return deck[:5]


def roll_die(die):
    random.shuffle(die)
    return die[0]




def comparison(die):
    roll1 = roll_die(die)
    for i in range(4):
        roll2 = roll_die(die)
        if(roll1 != roll2):
            return 0

    return 1








def calculate_die_odds(nums_success):
    success = 0
    times = 0
    die = ['♥', '♦', '♣', '♠']
    
    while (success != nums_success):
        success += comparison(die)
        times += 1

    return times/nums_success
    


type = input('Enter what card arrangment you would like to check for "straight flush", "flush", or "full house". ')
num_success = int(input('Enter the number of times you want it to succeed: '))
odds = calculate_odds(type, num_success)
print("The odds of being dealt a " + type + " is 1 in " + str(odds) + ".")
die_num_success = int(input('Enter the number of times you want your die to succeed: '))
die_odds = calculate_die_odds(die_num_success)
print("The odds of rolling 5 of the same suit is 1 in " + str(die_odds) + ".")
