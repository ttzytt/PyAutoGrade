




def deal_3_hands(deck):
    hands = [[], [], []] 

    for card_index in range(len(deck)): 
        current_hand = hands[card_index % 3] 
        current_hand.append(deck[card_index])

    return hands



def uno_who_played_what(cards_played):
    hands = [[], [], [], []]
    
    current_player = 0
    card_index = 0
    is_reversed = False
    
    while card_index < len(cards_played):
        card = cards_played[card_index]
        hands[current_player].append(card) 
        
         
        if card == 'skip':
            current_player += 1
            
        elif card == 'reverse':
            if is_reversed == False:
                is_reversed = True
                
        elif card != 'reverse': 
            if is_reversed == True:
                is_reversed = False
            
            
        if is_reversed == True:
            
            current_player = (current_player - 1) % 4 
        else:
            current_player = (current_player + 1) % 4

        card_index += 1

    return hands

def uno_who_played_what(cards_played, num_players, starting_player):
    hands = [[] for _ in range(num_players)]  
    
    current_player = starting_player
    card_index = 0
    is_reversed = False

    if num_players == 0:
        return None

    while card_index < len(cards_played):
        card = cards_played[card_index]
        hands[current_player].append(card)  

        if card == 'skip':
            current_player = (current_player + 1) % num_players  

        elif card == 'reverse':
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True

        if is_reversed:
            current_player = (current_player - 1) % num_players  
        else:
            current_player = (current_player + 1) % num_players  

        card_index += 1

    return hands




    
