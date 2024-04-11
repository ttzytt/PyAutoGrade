



def uno_who_played_what(cards_played):
    players = [[] for _ in range(4)]  
    reverse = False  
    skip_next = False  

    current_player = 0  

    for card in cards_played:
        if skip_next:
            
            skip_next = False
            current_player = (current_player + 2) % 4
        else:
            
            players[current_player].append(card)

            if card == 'reverse':
                
                reverse = not reverse
            elif card == 'skip':
                
                skip_next = True

            
            if reverse:
                current_player = (current_player - 1) % 4
            else:
                current_player = (current_player + 1) % 4

    return players
