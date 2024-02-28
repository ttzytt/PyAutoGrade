


from random import randint, shuffle, choice
from time import time 

def get_millis_time():
    return int(time() * 1000)

def all_equal_suits(hand):
    
    for card in hand:
        if card[1] != hand[0][1]:
            return False
    return True

def generate_deck(length):
    deck = []
    for card_number in range(1,14):
        for card_suit in ['♠','♥','♦','♣']:
            deck.append([card_number,card_suit])
    shuffle(deck)
    return deck[:5:]

def check_for_full_house(hand):
    hand.sort(key = lambda x: x[0])
    if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] and \
       ((hand[1][0] == hand[2][0]) ^ (hand[2][0] == hand[3][0])):
        return True
    return False

def check_for_straight_flush(hand):
    
    if not all_equal_suits(hand):
        return False
    
    hand.sort(key = lambda card: card[0])
    
    
    if [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]] == [1, 10, 11, 12, 13]:
        return True
    
    for card_index in range(len(hand)-1):
        if hand[card_index + 1][0] != hand[card_index][0] + 1:
            return False
    return True

print(check_for_straight_flush([[1,'♦'],[13,'♦'], [11,'♦'],[12,'♦'],[10,'♦']]))

def check_for_flush(hand):
    
    return all_equal_suits(hand)


def tries_until_poker_pattern(function):
    tries = 1
    while not function(generate_deck(5)):
        tries += 1
    return tries
            




def average_until_poker_pattern(num_trials):
    deck = []
    for card_number in range(1,14):
        for card_suit in ['♠','♥','♦','♣']:
            deck.append([card_number,card_suit])
    shuffle(deck)
    sum_so_far = 0
    for i in range(num_trials):
        tries = 1
        while not check_for_straight_flush(deck[:5:]):
            tries += 1
        print(i+1,(i+1) * '▇▇')
        sum_so_far += tries
    return sum_so_far/num_trials

while True:
    tries = int(input("tries: "))
    start_time = get_millis_time()
    print("Tries:", average_until_poker_pattern(tries))
    end_time = get_millis_time()
    print("Time Taken:",end_time-start_time,'ms')














def roll_dice(values, number):
    dice = []
    for i in range(number):
        dice.append(choice(values))
    for die in dice:
        if die != dice[0]:
            return False
    return True

def average_until_roll_dice(values, number, tries):
    sum_so_far = 0
    for _ in range(tries):
        count = 1
        while roll_dice(values, number) is False:
            count += 1
        sum_so_far += count
    return sum_so_far / tries

print(average_until_roll_dice([1,2,3,4],5,10))
    


