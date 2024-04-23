






def deal_3_hands(deck):
    hands = [[], [], []] 
    index_hand = 0 
    index_deck = 0 
    while (index_deck < len(deck)): 
        hands[index_hand].append(deck[index_deck])
        index_hand += 1 
        index_deck += 1 
        if(index_hand == 3):
            index_hand = 0

    return hands







def uno_who_played_what(cards_played):
    play_order = [[], [], [], []]
    player = 0 
    i = 0 
    
    while (i < len(cards_played)):
        if (cards_played[i] == 'skip'): 
            play_order[player].append(cards_played[i]) 
            player += 1

        elif (cards_played[i] == 'reverse'): 
            play_order[player].append(cards_played[i]) 
            player -= 1 
            if(player < 0):
                player += 4 
            i += 1 
            if (i < len(cards_played)):
                while ((i < len(cards_played)) and (cards_played[i] != 'reverse')):
                    if (cards_played[i] == 'skip'): 
                        play_order[player].append(cards_played[i]) 
                        player -= 2 
                    else:
                        play_order[player].append(cards_played[i]) 
                        player -= 1 
                    i += 1

                    if (player < 0):
                        player += 4
            if ( i < len(cards_played)):
                play_order[player].append(cards_played[i]) 

        else:
            play_order[player].append(cards_played[i]) 
    
        player += 1
        
        if (player >= 4): 
            player -= 4

        i += 1

    return play_order 
        
