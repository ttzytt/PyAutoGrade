







def deal_3_hands(deck):
    hands = [[], [], []] 
    for i in range(len(deck)):
        hands[i%3].append(deck[i]) 
                                   
                                   
                                   
                                   
                                   
                                   
    return hands






def uno_who_played_what(cards_played, num_players, starting_player):
    
    
    players_cards = []
    
    for i in range(num_players):
        players_cards.append([])
    is_skipping = False
    
    order_shift = starting_player - 1 
                                      
                                      
                                      
                                      
                                      
    is_reversed = False
    
    for i in range(len(cards_played)):
        if is_skipping:
            
            if is_reversed:
                order_shift -= 1
            else:
                order_shift += 1
                
        players_cards[(i+order_shift)%num_players].append(cards_played[i])
        
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


def catch_cheater(cards_played, initial_card, num_players, starting_player):
    
    is_reversed = False
    is_skipping = False
    cheater = None
    order_shift = starting_player - 1 
                                      
                                      
                                      
                                      
                                      
                                      
    
    if initial_card[1] == 'skip':
        order_shift += 1
    elif initial_card[1] == 'reverse':
        is_reversed = True
        
    previous_card = initial_card
    
    for i in range(len(cards_played)):
        if is_skipping:
            
            if is_reversed:
                order_shift -= 1
            else:
                order_shift += 1
        current_player = (i+order_shift)%num_players 
                                                     
                                                     
        if not (previous_card[0] == cards_played[i][0] or
                previous_card[1] == cards_played[i][1]): 
                                                         
            cheater = current_player + 1
            return cheater

        
        if cards_played[i][1] == 'skip':
            is_skipping = True
        else:
            is_skipping = False
        
        if cards_played[i][1] == 'reverse':
            if is_reversed == False:
                is_reversed = True
            else:
                is_reversed = False

        
        if is_reversed:
            order_shift -= 2 
                             
        previous_card = cards_played[i]
        
    return cheater



