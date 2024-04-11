




def deal_3_hands(deck):
    hands = [[], [], []]

    i_deck = 0

    while i_deck < len(deck):
        hands[i_deck % 3].append(deck[i_deck])
        i_deck += 1
    return hands




def uno_who_played_what(uno_deck):
    i_deck = 0
    i_player = 0
    is_reverse = False

    players = [[], [], [], []]

    while i_deck < len(uno_deck):
        if uno_deck[i_deck] == 'reverse':
            is_reverse = True

        while is_reverse == True and i_deck < len(uno_deck):

            players[i_player % 4].append(uno_deck[i_deck])

            if uno_deck[i_deck] == 'skip':
                i_player -= 2
            else:
                i_player -= 1

            i_deck += 1

            if i_deck != (len(uno_deck)):
                if uno_deck[i_deck] == 'reverse':
                    is_reverse = False

        if i_deck < len(uno_deck):

            players[i_player % 4].append(uno_deck[i_deck])

            if uno_deck[i_deck] == 'skip':
                i_player += 2
            else:
                i_player += 1

            i_deck += 1

    return players



def uno_who_played_what_bonus_1(uno_deck, num_players, starting_player):
    i_deck = 0
    i_player = 0
    is_reverse = False
    players = []

    for i in range(num_players - 1):
        players.append([])

    i_player = starting_player - 1

    print(i_player)

    while i_deck < len(uno_deck):
        if uno_deck[i_deck] == 'reverse':
            is_reverse = True

        while is_reverse == True and i_deck < len(uno_deck):

            players[i_player % num_players].append(uno_deck[i_deck])

            if uno_deck[i_deck] == 'skip':
                i_player -= 2
            else:
                i_player -= 1

            i_deck += 1

            if i_deck != (len(uno_deck)):
                if uno_deck[i_deck] == 'reverse':
                    is_reverse = False

        if i_deck < len(uno_deck):

            players[i_player % 4].append(uno_deck[i_deck])

            if uno_deck[i_deck] == 'skip':
                i_player += 2
            else:
                i_player += 1

            i_deck += 1

    return players









def uno_who_played_what_v2(uno_deck, num_players=4, starting_player=1):
    
    if not uno_deck:
        return None

    
    i_deck = 0
    i_players = starting_player - 1

    
    players = []

    
    negative = 1

    
    is_reverse = False

    
    for i in range(num_players):
        players.append([])

    while i_deck < len(uno_deck):

        players[i_players % num_players].append(uno_deck[i_deck])

        
        
        if uno_deck[i_deck] == 'reverse':
            
            
            if is_reverse:
                is_reverse = False
                negative = 1
            
            else:
                is_reverse = True
                negative = -1

        
        
        if uno_deck[i_deck] == 'skip':
            i_players += (2 * negative)
        else:
            i_players += (1 * negative)

        
        i_deck += 1

    return players








def catch_cheater(uno_deck, initial_card, num_players=4, starting_player=1):
    
    if not uno_deck:
        return None

    
    i_player = starting_player - 1
    i_deck = 0

    
    prev_card = initial_card

    cheater_list = []

    
    negative = 1
    is_reverse = False

    while i_deck < len(uno_deck):

        
        if uno_deck[i_deck][1] != prev_card[1] and uno_deck[i_deck][0] != prev_card[0]:
            cheater_list.append((i_player % num_players))

        
        prev_card = uno_deck[i_deck]

        
        if uno_deck[i_deck][1] == 'reverse':
            if is_reverse:
                is_reverse = False
                negative = 1
            else:
                is_reverse = True
                negative = -1

        
        if uno_deck[i_deck][1] == 'skip':
            i_player += (2 * negative)
        else:
            i_player += (1 * negative)

        i_deck += 1

    
    if not cheater_list:
        return None
    else:
        return cheater_list


def 
