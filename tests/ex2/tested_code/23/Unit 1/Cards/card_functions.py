





def deal_3_hands(deck):
    hands = [ [], [], [] ]

    for i in range(len(deck)):
        hands[i % 3].append(deck[i])

    return hands








def uno_who_played_what(cards_played):
    players = [[], [], [], []]
    current_player = 0
    reverse_direction = 1
    
    for i in range(len(cards_played)):
        players[current_player].append(cards_played[i])
        
        if cards_played[i] == 'skip':
            current_player = (current_player + 2 * reverse_direction) % 4

        elif cards_played[i] == 'reverse': 
            reverse_direction *= -1
            current_player = (current_player + reverse_direction) % 4

        else:
            current_player = (current_player + reverse_direction) % 4       

    return players



