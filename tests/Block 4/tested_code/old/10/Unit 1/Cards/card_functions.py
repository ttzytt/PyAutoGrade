





def deal_3_hands(_deck):
    hands = [[], [], []]
    deck_index = 0
    hand_index = 0
    
    while deck_index < len(_deck):
        hands[hand_index].append(_deck[deck_index])
        deck_index += 1
        hand_index = (hand_index + 1) % 3

    return hands


def uno_who_played_what(cards_played):
    if len(cards_played) == 0:
        return 0
    index = 0
    hands = [[], [], [], []]
    deck_index = 0
    hand_index = 0
    reverse_flag = False

    while deck_index < len(cards_played):
        if cards_played[deck_index] == 'skip':
            
            hands[hand_index].append(cards_played[deck_index])
            deck_index += 1
            hand_index += (hand_index + 1) % 4
            
        if cards_played[deck_index] == 'reverse':
            
            hands[hand_index].append(cards_played[deck_index])
            reverse_flag = True
            deck_index += 1
            hand_index = (hand_index - 1) % 4

        hands[hand_index].append(cards_played[deck_index])
        deck_index += 1
        
        if reverse_flag == False:
            hand_index = (hand_index + 1) % 4
        else:
            hand_index = (hand_index - 1) % 4
            
    return hands




