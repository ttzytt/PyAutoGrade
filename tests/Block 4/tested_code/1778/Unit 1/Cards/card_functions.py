
def deal_3_hands(deck):
    hands = [[], [], []]
    counter = 0
    while counter < len(deck):
        hands[ counter % 3 ].append(deck[counter])
        counter += 1
    return hands


def uno_who_played_what(cards_played):

    hands = [[], [], [], []]
    counter = 0
    player_counter = 0
    is_reverse = False
    
    while counter < len(cards_played):
        hands[ player_counter % 4 ].append(cards_played[ counter ])

        if cards_played[counter] == 'skip':
            player_counter += 1
            

        elif cards_played[counter] == 'reverse' or is_reverse == True:

            if cards_played[counter] == 'reverse' and is_reverse == True:
                is_reverse = False
            else:
                
                
                player_counter -= 2
                is_reverse = True

        
        counter += 1
        player_counter += 1
        

    return hands

def uno_who_played_what_B1(cards_played, num_players, starting_player):
    hands = []
    
    for i in range(0, num_players):
        hands.append([])
        
    counter = 0
    player_counter = 0
    is_reverse = False
    
    
    while counter < len(cards_played):
        
        
        hands[ (player_counter + (starting_player-1)) % num_players ].append(cards_played[ counter ])

        if cards_played[counter] == 'skip':
            player_counter += 1
            

        elif cards_played[counter] == 'reverse' or is_reverse:

            if cards_played[counter] == 'reverse' and is_reverse:
                is_reverse = False
            else:
                
                
                player_counter -= 2
                is_reverse = True

        
        counter += 1
        player_counter += 1
        

    return hands

def is_legal(card_1, card_2):
    if card_1[0] == card_2[0] or card_1[1] == card_2[1]:
        return True
    else:
        return False

def catch_cheater(cards_played, initial_card, num_players, starting_player):
    valid = is_legal(cards_played[0], initial_card)
    if valid == False:
        counter = 1
    valid = True
    counter = 1
    while valid == True and counter < len(cards_played):
        valid = is_legal(cards_played[counter], cards_played[counter - 1])
        counter += 1

    if counter == len(cards_played) + 1:
        return 'None'
    else:
        return counter + starting_player - num_players - 1
        
        
