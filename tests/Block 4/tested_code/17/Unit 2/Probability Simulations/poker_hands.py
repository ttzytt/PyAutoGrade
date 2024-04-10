




import random

random.seed()



def deal_five_card_hand(deck):
    random.shuffle(deck)
    return deck[:5]

def check_full_house(hand):
    rank_of_hand = [card[0] for card in hand]
    rank_of_hand.sort()

    
    if rank_of_hand[0] == rank_of_hand[1] and rank_of_hand[2] == rank_of_hand[3] == rank_of_hand[4]:
        return True
    if rank_of_hand[0] == rank_of_hand[1] == rank_of_hand[2] and rank_of_hand[3] == rank_of_hand[4]:
        return True

    return False

def simulate_full_house():
    deck = [[rank, suit] for rank in range(1, 14) for suit in ['♠', '♥', '♦', '♣']]

    tries = 0
    while True:
        hand = deal_five_card_hand(deck)
        tries += 1
        if check_full_house(hand):
            break

    return tries

def main():
    print("Welcome to the Poker Simulation!")
    while True:
        tries = simulate_full_house()
        print(f"The odds of being dealt a full house is 1 in {tries}.")

        play_again = input("Do you want to try again? (yes/no): ").lower()
        if play_again != 'yes':
            break



def check_flush(hand):
    suit_of_hand = [card[1] for card in hand]
    suit_of_hand.sort()

    
    if suit_of_hand[0] == suit_of_hand[1] == suit_of_hand[2] == suit_of_hand[3] == suit_of_hand[4]:
        return True

    return False

def simulate_flush():
    deck = [[rank, suit] for rank in range(1, 14) for suit in ['♠', '♥', '♦', '♣']]

    tries = 0
    while True:
        hand = deal_five_card_hand(deck)
        tries += 1
        if check_flush(hand):
            break

    return tries

def main_2():
    print("Welcome to the Poker Simulation!")
    while True:
        tries = simulate_flush()
        print(f"The odds of being dealt a flush is 1 in {tries}.")

        play_again = input("Do you want to try again? (yes/no): ").lower()
        if play_again != 'yes':
            break



def check_straight_flush(hand):
    suit_of_hand = [card[1] for card in hand]
    suit_of_hand.sort()

    ranks = [card[0] for card in hand]
    ranks.sort()

    
    if suit_of_hand[0] == suit_of_hand[1] == suit_of_hand[2] == suit_of_hand[3] == suit_of_hand[4]:
        if ranks[0] == ranks[1] - 1 and ranks[1] == ranks[2] - 1 and ranks[2] == ranks[3] - 1 and ranks[3] == ranks[4] - 1:
            return True

    return False

def simulate_straight_flush():
    deck = [[rank, suit] for rank in range(1, 14) for suit in ['♠', '♥', '♦', '♣']]

    tries = 0
    while True:
        hand = deal_five_card_hand(deck)
        tries += 1
        if check_straight_flush(hand):
            break

    return tries

def main_3():
    print("Welcome to the Poker Simulation!")
    while True:
        tries = simulate_straight_flush()
        print(f"The odds of being dealt a straight flush is 1 in {tries}.")

        play_again = input("Do you want to try again? (yes/no): ").lower()
        if play_again != 'yes':
            break




def rolls_until_all_values():    
    rolled_values = []
    rolls = 0

    while True:
        roll = random.choice(['♠', '♥', '♦', '♣'])
        rolls += 1
        if not rolled_values or roll == rolled_values[0]:
            rolled_values.append(roll)
        else:
            rolled_values = [roll]

        if len(rolled_values) == 5:
            break
        
    return rolls    

def average_rolls_until_all_values(num_trials):
    total_rolls = 0
    for _ in range(num_trials):
        total_rolls += rolls_until_all_values()

    average_rolls = total_rolls / num_trials
    return average_rolls

def total_average_in_all_flush(num_trials):
    total_rolls = average_rolls_until_all_values/(simulate_flush + simulate_straight_flush )
    


