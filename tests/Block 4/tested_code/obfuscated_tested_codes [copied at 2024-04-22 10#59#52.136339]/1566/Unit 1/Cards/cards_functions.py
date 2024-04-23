









def deal_3_hands(deck):
    hands = [[],[],[]]
      
    for i in range(len(deck)):
        hands[i%3] = hands[i%3] + [deck[i]] 
    return hands






























        
def uno_who_played_what(cards_played, num_players = 4, starting_player = 0):
    
    hands = []
    player = 0
    for _ in range(num_players):
        hands.append([])
        player += 1


    player_index = starting_player
    is_reverse = False

    for card_index in range(len(cards_played)): 
        hands[player_index % num_players] = (hands[player_index % num_players]
                                              + [cards_played[card_index]])
        if cards_played[card_index] == 'reverse':
                
                if is_reverse:
                    is_reverse = False
                    player_index += 1
                else:
                    is_reverse = True 
                    player_index -= 1
                        
        elif cards_played[card_index] == 'skip':
                
                if is_reverse:
                    player_index -= 2
                else:
                    player_index += 2 
                        
        else: 
                if is_reverse:
                    player_index -= 1
                else:
                    player_index += 1
    return hands


      
                  
            









 
