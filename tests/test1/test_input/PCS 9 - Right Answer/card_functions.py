
# Returns a list containing the hands of each player in an Uno game, based on the game's history.
# Input:
    # cards_played: Description: Uno game's history
    #               Possible elements: any number, 'skip', and 'reverse'.
# The implemented rules are:
# - If the card is 'skip', skip the next player's turn. This means that the
#                          next card played will be the next next player's move.
# -                'reverse', reverses the turn order.
#                          (e.g. goes from Player 1 -> Player 2 to Player 2 -> Player 1)
def uno_who_played_what(cards_played, num_players = 4, player_index = 0):
    
    hands = [[] for _ in range(num_players)]
    
    play_order = 1  # reverse negates this

    for i in range(len(cards_played)):
        hands[player_index].append(cards_played[i])

        if cards_played[i] == 'skip':
            player_index = (player_index + play_order) % num_players
        elif cards_played[i] == 'reverse':
            play_order *= -1

        player_index = (player_index + play_order) % num_players

    return hands

