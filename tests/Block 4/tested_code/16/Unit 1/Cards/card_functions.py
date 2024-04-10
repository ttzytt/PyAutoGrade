




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








def uno_who_played_what(cards_played, num_players = 4, starting_player = 0):
    play_order = []
    for i in range(num_players):
        play_order.append([])
    player = starting_player 
    i = 0 
    
    while (i < len(cards_played)):
        if (cards_played[i] == 'skip'): 
            play_order[player].append(cards_played[i]) 
            player += 1

        elif (cards_played[i] == 'reverse'): 
            play_order[player].append(cards_played[i]) 
            player -= 1 
            if(player < 0):
                player += num_players 
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
                        player += num_players
            if ( i < len(cards_played)):
                play_order[player].append(cards_played[i]) 

        else:
            play_order[player].append(cards_played[i]) 
    
        player += 1
        
        if (player >= num_players): 
            player -= num_players

        i += 1

    return play_order 





def catch_cheater(cards_played, initial_card):
    if(len(cards_played) == 0): 
       return None

    
    if((cards_played[0][0] != initial_card[0]) and
       (cards_played[0][1] != initial_card[1])):
        return 0
    
    previous_card_color = cards_played[0][0] 

    
    for i in range(1, len(cards_played)):
        if((previous_card_color != cards_played[i][0]) and
           (cards_played[i - 1][1] != cards_played[i][1])):
            return i
        i += 1

    return None 
            


        
        
