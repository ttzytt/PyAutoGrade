


def deal_3_hands(deck):
    hands = [ [], [], []]
    deck_index = 0
    hand_index = 0
    while deck_index < len(deck):
        hands[hand_index].append(deck[deck_index])
        deck_index = deck_index + 1
        hand_index = (hand_index + 1) % 3
    return hands
