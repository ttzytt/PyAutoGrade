


def deal_3_hands(deck):
    
    hands = [[], [], []]

    for i in range(len(deck)):
        
        
        hands[i % 3].append(deck[i])

    return hands


def uno_who_played_what(cards_played):
    num_players = 4
    turn_order = list(range(num_players))
    current_turn = 0
    player_cards = [[] for _ in range(num_players)]

    for card in cards_played:
        player_cards[current_turn].append(card)

        if card == 'reverse':
            turn_order.reverse()
        elif card == 'skip':
            current_turn = (current_turn + 2) % num_players
        else:
            current_turn = (current_turn + 1) % num_players

    return player_cards
