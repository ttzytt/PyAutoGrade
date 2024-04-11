





def deal_3_hands(deck):
    hands = [[], [], []]
    deck_index = 0
    hand_index = 0
    while deck_index < len(deck):
        hands[hand_index].append(deck[deck_index])
        deck_index = deck_index + 1
        
        hand_index = (hand_index + 1) % 3
    return hands




def uno_who_played_what(cards_played):
    hands = [[], [], [], []]
    deck_index = 0
    hand_index = 0
    reverse_or_not = False

    
    while deck_index < len(cards_played):
        hands[hand_index].append(cards_played[deck_index])
        
        
        
        if cards_played[deck_index] == 'skip':
            if reverse_or_not == False:
                hand_index += 1
            else:
                hand_index -= 1
                
        
        
        elif cards_played[deck_index] == 'reverse':
            if reverse_or_not == True:
                reverse_or_not = False
            else:
                reverse_or_not = True
                
        deck_index = deck_index + 1

        if reverse_or_not == False:
            hand_index = (hand_index + 1) % 4
        else:
            hand_index = (hand_index - 1) % 4
    
    return hands
        
