


from random import randint, shuffle, choice, seed
from time import time 

seed()


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


        for card_suit in [1,2,3,4]:
              deck.append([card_number,card_suit])
    shuffle(deck)
    return deck[:5:]





def check_for_full_house(hand):
    suits = []
    for card in hand:
        suits.append(card[0])
    suits.sort()
    
    return suits[0] == suits[1] and suits[3] == suits[4] and \
       ((suits[1] == suits[2]) ^ (suits[2] == suits[3]))




def check_for_straight_flush(hand):
    
    if not all_equal_suits(hand):
        return False
    
    hand.sort(key = lambda card: card[0])
    
    
    return hand[4][0] - hand[0][0] == 4 or (hand[4][0] - hand[0][0] == 12 and hand[4][0]-hand[1][0] == 3)
    





def check_for_flush(hand):
    
    return all_equal_suits(hand) and not check_for_straight_flush(hand)


def tries_until_poker_pattern(function):
    tries = 1
    
    deck = []
    for card_number in range(1,14):


        for card_suit in [1,2,3,4]:
              deck.append([card_number,card_suit])
    shuffle(deck)
    while not function(deck[:5:]): 
        tries += 1
        shuffle(deck) 
    return tries













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
    for i in range(tries):
        count = 1
        while roll_dice(values, number) is False:
            count += 1
        sum_so_far += count
        if (i * 100) // tries > (i * 100 - 100)// tries: 
            print(((i * 10) // tries + 1) * '▇▇',f'{(i * 100) // tries}%')
    print(10 * '▇▇','100%')
    return sum_so_far / tries





def average_until_poker_pattern(num_trials):
    sum_so_far = 0
    user_choice = input("'f' for full house, 's' for straight flush" +
                        ", 'x' for flush, and 'd' for dice.").lower()
    while user_choice not in ['f','s','x','d']:
        print("was not an option >:(")
        user_choice = input("'f' for full house, 's' for straight flush" +
                            ", and 'x' for flush ").lower()
    if user_choice == 'f':
        target_function = check_for_full_house
    elif user_choice == 's':
        target_function = check_for_straight_flush
    elif user_choice == 'f':
        target_function = check_for_flush
    else:
        target_function = None
        return average_until_roll_dice([1,2,3,4],5,int(num_trials))
    for i in range(num_trials):
        sum_so_far += tries_until_poker_pattern(target_function)
        if (i * 100) // num_trials > (i * 100 - 100)// num_trials: 
            print(((i * 10) // num_trials + 1) * '▇▇',f'{(i * 100) // num_trials}%')
    print(10 * '▇▇','100%')
    return sum_so_far/num_trials
        

while True:
    tries = int(input("tries: "))
    start_time = get_millis_time()
    print("Tries:", average_until_poker_pattern(tries))
    end_time = get_millis_time()
    print("Time Taken:",end_time-start_time,'ms')



    


