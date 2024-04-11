


import random


def is_full_house(hand):
    
    value_counts = {}
    for card in hand:
        value = card[0]
        value_counts[value] = value_counts.get(value, 0) + 1

    
    return len(value_counts) == 2 and (2 in value_counts.values() or 3 in value_counts.values())

def poker_full_house_simulation():
    
    num_simulations = 100000
    full_house_count = 0

    
    for _ in range(num_simulations):
        deck = generate_deck()
        hand = random.sample(deck, 5)  
        if is_full_house(hand):
            full_house_count += 1

    
    odds = num_simulations / full_house_count if full_house_count != 0 else 0
    print(f"The odds of being dealt a full house is 1 in {odds}")

def generate_deck():
    
    ranks = list(range(1, 14))
    suits = ['♠', '♥', '♦', '♣']
    deck = [[rank, suit] for rank in ranks for suit in suits]
    return deck


def is_straight_flush(hand):
    
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    
    same_suit = suits.count(suits[0]) == len(suits)

    
    consecutive_sequence = check_consecutive(values)

    return same_suit and consecutive_sequence

def check_consecutive(values):
    
    for i in range(len(values) - 1):
        if values[i] + 1 not in values and values[i] - 1 not in values:
            return False
    return True

def poker_straight_flush_simulation():
    
    num_simulations = 100000
    straight_flush_count = 0

    
    for _ in range(num_simulations):
        deck = generate_deck()
        random.shuffle(deck)
        hand = deck[:5]  
        if is_straight_flush(hand):
            straight_flush_count += 1

    
    odds = num_simulations / straight_flush_count if straight_flush_count != 0 else 0
    print(f"The odds of being dealt a straight flush is 1 in {odds}")

def generate_deck():
    
    ranks = list(range(1, 14))
    suits = ['♠', '♥', '♦', '♣']
    deck = [[rank, suit] for rank in ranks for suit in suits]
    return deck


def is_flush(hand):
    
    suits = [card[1] for card in hand]
    return suits.count(suits[0]) == len(suits)

def poker_flush_simulation():
    
    num_simulations = 100000
    flush_count = 0

    
    for _ in range(num_simulations):
        deck = generate_deck()
        random.shuffle(deck)
        hand = deck[:5]  
        if is_flush(hand):
            flush_count += 1

    
    odds = 1 / (flush_count / num_simulations) if flush_count != 0 else 0
    print(f"The odds of being dealt a flush is 1 in {int(odds)}")

def generate_deck():
    
    ranks = list(range(1, 14))
    suits = ['♠', '♥', '♦', '♣']
    return [[rank, suit] for rank in ranks for suit in suits]



def roll_dice():
    
    return [random.choice(['♠', '♥', '♦', '♣']) for _ in range(5)]

def is_same_suit(hand):
    
    return all(suit == hand[0] for suit in hand)

def dice_simulation():
    
    num_simulations = 100000
    same_suit_count = 0

    for _ in range(num_simulations):
        dice_result = roll_dice()
        if is_same_suit(dice_result):
            same_suit_count += 1

    
    odds_same_suit = num_simulations / same_suit_count if same_suit_count != 0 else 0
    print(f"The odds of rolling the same suit for all five dice is 1 in {odds_same_suit}")

def compare_to_flush_odds():
    
    
    odds_flush_t6 = 1 / odds_of_flush_t6()
    odds_flush_t5 = 1 / odds_of_flush_t5()

    print(f"\nComparison with Flush Odds:")
    print(f"Odds of rolling the same suit for all five dice: 1 in {odds_same_suit}")
    print(f"Odds of getting any flush (T6): 1 in {odds_flush_t6}")
    print(f"Odds of getting any flush (T5): 1 in {odds_flush_t5}")

    
    diff_t6 = abs(odds_same_suit - odds_flush_t6)
    diff_t5 = abs(odds_same_suit - odds_flush_t5)

    print(f"Difference with T6: {diff_t6}  # Include reason for difference")
    print(f"Difference with T5: {diff_t5}  # Include reason for difference")


poker_full_house_simulation()
poker_straight_flush_simulation()
poker_flush_simulation()
dice_simulation()
compare_to_flush_odds()
