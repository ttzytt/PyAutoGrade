




PLAYERS_NUM = 4   
REVERSE_CARD = 'reverse'
SKIP_CARD = 'skip'


def uno_who_played_what(cards_played):
    players = []  
    for _ in range(PLAYERS_NUM):
        players.append([])  
    
    current_player = 1  
    is_reversed = False 
    
    for card in cards_played:
        players[current_player - 1].append(card)  

        
        if card == REVERSE_CARD:  
            if is_reversed == False:
                is_reversed = True
                current_player -= 1
            else:
                is_reversed = False
                current_player += 1  
        elif card == SKIP_CARD:  
            if is_reversed == False:
                current_player += 2
            else:
                current_player -= 2          
        else:  
            if is_reversed == False:
                current_player += 1
            else:
                current_player -= 1      
        
        
        current_player = current_player % PLAYERS_NUM
    
    return players
