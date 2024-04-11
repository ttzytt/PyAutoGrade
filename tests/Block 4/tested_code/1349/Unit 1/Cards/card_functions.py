



def deal_3_hands(deck):
    
    
    hands = [[], [], []]
    for i in range(len(deck)):
        hands[i % 3].append(deck[i])

    return hands

        

def uno_who_played_what(cards_played, num_players = 4, starting_player = 0):
    
    
    
    
    
    
    hands = []

    
    for i in range(num_players):
        hands.append([])
    
    
    
    
    list_index_revision = 0 - starting_player
    
    number_reverse = 0 

    for i in range(len(cards_played)):
        
        hands[(i - list_index_revision) % num_players].append(cards_played[i])
        
        
        if cards_played[i] == 'reverse':
            number_reverse += 1

        
        elif cards_played[i] == 'skip':
            
            
            if number_reverse % 2 == 1:
                list_index_revision += 1
            else:
                list_index_revision -= 1

        

        if number_reverse % 2 == 1:
            
            
            list_index_revision += 2

    return hands





def catch_cheater(cards_played, initial_card):
    list_index_revision = 0
    last_card = initial_card
    number_reverse = 0
    num_players = 4
    
    for i in range(len(cards_played)):
        if(last_card[0] != cards_played[i][0] and last_card[1] != cards_played[i][1]):
            return (i - list_index_revision) % num_players
        
        if cards_played[i][1] == 'reverse':
            number_reverse += 1

        
        elif cards_played[i][1] == 'skip':
            
            
            if number_reverse % 2 == 1:
                list_index_revision += 1
            else:
                list_index_revision -= 1

        elif cards_played[i][1] == 'draw 2':
            
            if last_card[1] == 'draw 2' and i != 0:
                return (i - list_index_revision) % num_players
        else:
            
            if number_reverse % 2 == 1:
                list_index_revision += 1
            else:
                list_index_revision -= 1

        

        if number_reverse % 2 == 1:
            
            
            list_index_revision += 2

        last_card = cards_played[i]
    return None
       
            
        
        
        
        
        
            
