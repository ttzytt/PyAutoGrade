




from operator import itemgetter
import random
random.seed()






def deal_five_card_hand(deck):
    random.shuffle(deck)
    hand = deck[ :5]  
    return hand
    


def check_full_house():
    hand = deal_five_card_hand(deck) 
    hand.sort(key = itemgetter(0)) 
    
    if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] and (hand[2][0] == hand[0][0] or hand[2][0] == hand[4][0]):
        return True
    
    return False
    

def tries_till_full_house():
    tries = 0
    while check_full_house() == False:
        tries += 1
    return tries


def average_tries_till_full_house(num_trials):
    sum_of_tries = 0
    for _ in range(num_trials): 
        sum_of_tries += tries_till_full_house()

    return(sum_of_tries/num_trials)



def check_straight_flush():
    hand = deal_five_card_hand(deck) 
    
    for card in hand:
        if card[1] != hand[0][1]: 
            return False
    hand.sort(key = itemgetter(0))  
    if hand[4][0] - hand[0][0] == 4: 
        return True
    elif hand[0][0] == 1 and hand[1][0] == 11:
        return True
    return False


def tries_till_straight_flush():
    tries = 0
    while check_straight_flush() == False: 
        tries += 1
    return tries


def average_tries_till_straight_flush(num_trials):
    sum_of_tries = 0
    for _ in range(num_trials):
        sum_of_tries += tries_till_straight_flush()
    return (sum_of_tries/num_trials)


def check_flush():
    hand = deal_five_card_hand(deck)
    for card in hand:
        if card[1] != hand[0][1]: 
            return False
    hand.sort(key = itemgetter(0))
    
    if hand[4][0] - hand[0][0] == 4:
        return False
    return True


def tries_till_flush():
    tries = 0
    while check_flush() == False:
        tries += 1
    return tries


def average_tries_till_flush(num_trials):
    sum_of_tries = 0
    for _ in range(num_trials):
        sum_of_tries += tries_till_flush()
    return (sum_of_tries/num_trials)


def dice_rolling(dice):
    dice_rolls = [] 
    
    for i in range (6):
        dice_rolls.append(random.choice(dice)) 
    dice_rolls.sort()
    if dice_rolls[0] == dice_rolls[4]:
        return True
    return False

def tries_till_same_suit():
    tries = 0
    while dice_rolling(dice) == False:
        tries += 1
    return tries

def average_tries_till_same_suit(num_trials):
    sum_of_tries = 0
    for _ in range(num_trials):
        sum_of_tries += tries_till_same_suit()
    return (sum_of_tries/num_trials)


    



deck = []
for rank in range(1, 14):
    for suit in ['♠', '♥', '♦', '♣']:
        deck.append([rank, suit])

dice = ['♠', '♥', '♦', '♣']

num_trials = int(input('How many trials do you want? '))

print ('Probablility of getting a full house is 1 out of ' + str(average_tries_till_full_house(num_trials)))
print ('Probablility of getting a straight flush is 1 out of ' + str(average_tries_till_straight_flush(num_trials)))
print ('Probablility of getting a flush is 1 out of ' + str(average_tries_till_flush(num_trials)))
print ('Probablility of getting 5 same suits is 1 out of ' + str(average_tries_till_same_suit(num_trials)))
