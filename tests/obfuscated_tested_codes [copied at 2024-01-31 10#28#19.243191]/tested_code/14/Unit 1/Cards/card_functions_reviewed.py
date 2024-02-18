




def deal_3_hands(deck):
    
    
    hands = [[], [], []]
    for i in range(len(deck)):
        hands[i % 3].append(deck[i])

    return hands

        




def uno_who_played_what(cards_played):
    player_number = 4
    
    
    hands = [[], [], [], []]
    
    
    
    list_index_revision = 0
    
    number_reverse = 0 

    for i in range(len(cards_played)):
        
        if cards_played[i] == 'reverse':
            number_reverse += 1
            
            hands[(i - list_index_revision) % player_number].append(cards_played[i])

        
        elif cards_played[i] == 'skip':
            
            hands[(i - list_index_revision) % player_number].append(cards_played[i])
            
            
            if number_reverse % 2 == 1:
                list_index_revision += 1
            else:
                list_index_revision -= 1

        
        else:
            hands[(i - list_index_revision) % player_number].append(cards_played[i])

        if number_reverse % 2 == 1:
            
            
            list_index_revision += 2

    return hands









def uno_who_played_what_B5(cards_played, num_players, starting_player):
    
    
    
    
    hands = []

    
    for i in range(num_players):
        hands.append([])
    
    
    
    
    list_index_revision = 1 - starting_player
    
    number_reverse = 0 

    for i in range(len(cards_played)):
        
        if cards_played[i] == 'reverse':
            number_reverse += 1
            
            hands[(i - list_index_revision) % num_players].append(cards_played[i])

        
        elif cards_played[i] == 'skip':
            
            hands[(i - list_index_revision) % num_players].append(cards_played[i])
            
            
            if number_reverse % 2 == 1:
                list_index_revision += 1
            else:
                list_index_revision -= 1

        
        else:
            hands[(i - list_index_revision) % num_players].append(cards_played[i])

        if number_reverse % 2 == 1:
            
            
            list_index_revision += 2

    return hands

        
        
        
        
            
