


def deal_3_hands(deck):
    
    hand_1 = []
    hand_2 = []
    hand_3 = []
    for i in range(0,len(deck),3):
        hand_1.append(deck[i])
    for i in range(1,len(deck),3):
        hand_2.append(deck[i])
    for i in range(2,len(deck),3):
        hand_3.append(deck[i]) 
    return([hand_1, hand_2, hand_3])





def deal_n_hands(deck, hands):
    table_hands = []
    for hand in range(hands):
        hand_list = []
        for i in range(len(deck)):
            if i % hands == hand:
                hand_list.append(deck[i])
        table_hands.append(hand_list)
    return table_hands

def deal_n_hands_but_cooler(deck,hands):
    table_hands = [[] for x in range(hands)]
    for i in range(len(deck)):
        table_hands[i%hands].append(deck[i])
    return table_hands








    
    
    
    
    
    
    





def uno_who_played_what(cards_played, num_players, starting_player):
    
    if num_players <= 0 or type(num_players) is not int:
        return None
    if starting_player >= num_players  or starting_player < 0 or type(starting_player) is not int:
        return None

    
    
    skip_buffered_list = []
    for i in range(len(cards_played)):
        if cards_played[i] == 'skip':
            skip_buffered_list.append('skip') 
            skip_buffered_list.append('buffer')
        else:
            skip_buffered_list.append(cards_played[i])

    
    is_clockwise = True
    hands = []
    for x in range(num_players):
        hands.append([])

    
    if starting_player == 0:
        last_selected_hand = len(hands) - 1
    else:
        last_selected_hand = starting_player - 1

    
    for i in range(len(skip_buffered_list)):
        
        if is_clockwise:
            last_selected_hand += 1
        else:
            last_selected_hand -=1
        last_selected_hand = last_selected_hand % num_players
        
        hands[last_selected_hand].append(skip_buffered_list[i])
        
        if skip_buffered_list[i] == 'reverse':
            is_clockwise = not is_clockwise

    
    for hand in range(len(hands)):
        unbuffered_hand = []
        for card in range(len(hands[hand])):
            if not hands[hand][card] == 'buffer':
                unbuffered_hand.append(hands[hand][card])
        hands[hand] = unbuffered_hand
    return hands

def catch_cheater(cards_played, initial_card, num_players, starting_player):
    
    if len(cards_played) == 0:
        return None
    
    
    
    def is_legal_move(card_1, card_2):
        if card_1[0] == card_2[0] or card_1[1] == card_2[1]:
            return True
        return False

    increasing_move_order = True
    
    
    if not is_legal_move(initial_card, cards_played[0]):
        return starting_player
    if cards_played[0][1] == 'skip':
        starting_player += 1
    if cards_played[0][1] == 'reverse':
        increasing_move_order = False

    
    if increasing_move_order:
        player_turn = starting_player + 1 
    else:
        player_turn = starting_player - 1
        
    player_turn = player_turn % num_players 
                                            

    
    for i in range(len(cards_played)-1):
        added_skip = 0
        if not is_legal_move(cards_played[i], cards_played[i+1]):
            return player_turn
        if cards_played[i+1][1] == 'skip':
            added_skip = 1
        elif cards_played[i+1][1] == 'reverse':
            increasing_move_order = not increasing_move_order

        
        if increasing_move_order:
            player_turn += (1 + added_skip)
        else:
            player_turn -=  (1 + added_skip)
        player_turn = player_turn % num_players
    return None
