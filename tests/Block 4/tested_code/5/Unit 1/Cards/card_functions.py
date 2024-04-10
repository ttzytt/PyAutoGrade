








def deal_3_hands(deck):

    
    hands = [[], [], []]
    
    for i in range(len(deck)):
        number = i % 3
        hands[number].append(deck[i])
    return hands




def uno_who_played_what(cards_played):
    
    hands = [[], [], [], []]
    hands_index = 0
    num_to_skip = 0  

    
    for i in range(len(cards_played)):
        hands[hands_index].append(cards_played[i])
        if cards_played[i] == 'skip':
            hands_index = (hands_index + 1) % 4
        hands_index = (hands_index + 1) % 4
    return hands

   

