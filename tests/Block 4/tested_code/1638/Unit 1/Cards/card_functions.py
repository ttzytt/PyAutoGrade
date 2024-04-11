


def deal_3_hands(deck):

    hands = [[], [], []]

    for i in range(len(deck)):
        hands[i % 3].append(deck[i])

    return hands


def uno_who_played_what(cards_played):

    player_number = 0
    players = [[], [], [], []]
    direction = 1

    for i in range(len(cards_played)):
        players[player_number].append(cards_played[i])

        if cards_played[i] == 'reverse':
            direction *= -1
            if direction == 1:
                player_number = (player_number + direction) % 4
            else:
                if player_number > 0:
                    player_number = (player_number + direction) % 4
                else:
                    player_number = 3
            
        elif cards_played[i] == 'skip':
            if direction == 1:
                player_number = (player_number + 2 * direction) % 4
            else:
                if player_number > 1:
                    player_number = (player_number + 2 * direction) % 4
                else:
                    player_number = (player_number + 2)
            
        else:
            if direction == 1:
                player_number = (player_number + direction) % 4
            else:
                if player_number > 0:
                    player_number = (player_number + direction) % 4
                else:
                    player_number = 3            
    return players
