


def deal_3_hands(deck):
    hand_index = 0
    deck_index = 0

    hands = [[], [], []]

    while deck_index < len(deck):
        hands[hand_index].append(deck[deck_index])
        deck_index = deck_index + 1
        hand_index = (hand_index + 1) % 3
    print(hands)
    return hands
        
    

def uno_played_what(cards_played):
    player_index = 0
    card_index = 0
    count = 0

    player_hands = [[],[],[],[]]
    while card_index < len(cards_played):
        
        player_hands[player_index].append(cards_played[card_index])
        
        if cards_played[card_index] == 'reverse':
            count = count + 1
        if count % 2 == 1:
            if player_index < 0:
                player_index = 3
            else:
                player_index = (player_index - 1) % 4
                if cards_played[card_index] == 'skip':
                    player_index = player_index - 1

        else:
            player_index = (player_index + 1) % 4
            if cards_played[card_index] == 'skip':
                player_index = player_index + 1
                
        card_index = card_index + 1
        
    print(player_hands)
    return player_hands
 
        
        
