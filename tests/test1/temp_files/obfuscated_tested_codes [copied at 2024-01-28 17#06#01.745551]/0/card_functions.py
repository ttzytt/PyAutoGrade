


    
    





def uno_who_played_what(cards_played, num_players = 4, player_index = 0):
    
    hands = [[] for _ in range(num_players)]
    
    play_order = 1  

    for i in range(len(cards_played)):
        hands[player_index].append(cards_played[i])

        if cards_played[i] == 'skip':
            player_index = (player_index + play_order) % num_players
        elif cards_played[i] == 'reverse':
            play_order *= -1

        player_index = (player_index + play_order) % num_players

    return hands

