





def deal_3_hands(deck):
    
    hand_1 = []
    hand_2 = []
    hand_3 = []

    
    for i in range(len(deck)):
        
        if i % 3 == 0:
            hand_1.append(deck[i])
        elif i % 3 == 1:
            hand_2.append(deck[i])
        elif i % 3 == 2:
            hand_3.append(deck[i])
            
    return [hand_1, hand_2, hand_3]



def uno_who_played_what(cards_played):
    
    
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []
    
    
    current_card = 0
    
    
    reverse = False
    
    
    player_turn = 0
    
    
    while current_card < len(cards_played):

        
        if player_turn % 4 == 0:
            player_1.append(cards_played[current_card])
        elif player_turn % 4 == 1:
            player_2.append(cards_played[current_card])
        elif player_turn % 4 == 2:
            player_3.append(cards_played[current_card])
        elif player_turn % 4 == 3:
            player_4.append(cards_played[current_card])

        
        if reverse == True and cards_played[current_card] == 'skip':
            player_turn -= 2

        
        if cards_played[current_card] == 'skip':
            player_turn += 1

        
        if cards_played[current_card] == 'reverse':
            if reverse == True:
                reverse = False
            elif reverse == False:
                reverse = True

        
        if reverse == True:
            player_turn -= 2
        
        current_card += 1
        player_turn += 1

    
    return [player_1, player_2, player_3, player_4]
