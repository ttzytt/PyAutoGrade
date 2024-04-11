








def deal_3_hands(deck):
    hands = [[], [], []] 
    
    for i in range(len(deck)):
        hands[i%3].append(deck[i]) 
                                   
                                   
                                   
                                   
                                   
                                   
    return hands






def uno_who_played_what(cards_played):
    
    players_cards = [[], [], [], []] 
    is_skipping = False
    
    
    
    order_shift = 0 
                    
    is_reversed = False
    for i in range(len(cards_played)):
        if not is_skipping:
            players_cards[(i+order_shift)%4].append(cards_played[i])
        else:
            
            if is_reversed:
                order_shift -= 1
            else:
                order_shift += 1
            players_cards[(i+order_shift)%4].append(cards_played[i])
        if cards_played[i] == 'skip':
            is_skipping = True
        else:
            is_skipping = False
        
        if cards_played[i] == 'reverse':
            if is_reversed == False:
                is_reversed = True
            else:
                is_reversed = False

        
        
        if is_reversed:
            order_shift -= 2 
                             
    return players_cards



    
    
