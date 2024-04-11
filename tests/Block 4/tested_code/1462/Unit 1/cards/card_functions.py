


def deal_3_hands(deck):

    hands = [[], [], []] 

    for i in range(len(deck)):
        
        hands[i%3].append(deck[i]) 
    return hands


def uno_who_played_what(cards_played):

    hands = [[], [], [], []] 
    hands_index = 0  
    reverse_times = 0 

    for i in range(len(cards_played)):

        
        hands[hands_index % 4].append(cards_played[i])
         
        if cards_played[i] == 'skip':
            
            
            
            hands_index += 2 * ((-1) ** reverse_times)

        elif cards_played[i] == 'reverse':
            
            reverse_times += 1
            
            
            hands_index += (-1) ** reverse_times

        else:
            
            hands_index += (-1) ** reverse_times

    return hands








































