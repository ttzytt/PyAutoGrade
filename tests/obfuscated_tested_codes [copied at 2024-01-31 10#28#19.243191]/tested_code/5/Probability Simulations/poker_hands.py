from itertools import combinations

def is_full_house(hand):
    

    values = [card[0] for card in hand]
    value_counts = {}
    for value in values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    
    
    return sorted(value_counts.values()) == [2, 3]

def calculate_full_house_odds():
    
    number = "23456789TJQKA"
    suits = "CDHS"
    deck = []
    for number in numbers:
        for suit in suits:
            deck.append(rank + suit)
    
    full_house_count = 0
    total_hand_count = 0

    
    for hand in combinations(deck, 5):
        total_hand_count += 1
        
        
        if is_full_house(hand):
            full_house_count += 1

    
    odds = full_house_count / total_hand_count
    return odds


odds = calculate_full_house_odds()
print("Odds of being dealt a full house:", "{:.6%}".format(odds))
    
