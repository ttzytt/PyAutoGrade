





def deal_3_hands(decks):
    
    hands = [[],[],[]]
    
    for i in range(len(decks)):
        if i % 3 == 0:
            hands[0].append(decks[i])
        elif i % 3 == 1:
            hands[1].append(decks[i])
        else:
            hands[2].append(decks[i])
    
    return hands


def uno_who_played_what(cards_played, num_players=4,starting_player=1):
    
    Featured_value = [0]*len(cards_played)
    
    Signal = 1
    if len(cards_played)!= 0:
        if cards_played[0] == 'reverse':
             Signal = -1
    
    results = []
    for i in range(num_players):
        results.append([])
    for i in range(1,len(cards_played)):
        
        if cards_played[i-1] == 'skip':
            Featured_value[i] = Featured_value[i-1] + 2*Signal
        
        else:
            Featured_value[i] = Featured_value[i-1] + Signal
        
        if cards_played[i] == 'reverse':
            Signal = Signal * (-1)
    
    for i in range(len(cards_played)):
        for j in range(num_players):
            if Featured_value[i] % num_players == j:
                results[(j+starting_player-1)%num_players].append(cards_played[i])
    return results







def uno_who_played_what_1(cards_played, num_players=4,starting_player=1):
    
    Featured_value = [0]*len(cards_played)
    
    Signal = 1
    if len(cards_played)!= 0:
        if cards_played[0] == 'reverse':
             Signal = -1
    
    results = []
    
    for i in range(num_players):
        results.append([])
    for i in range(1,len(cards_played)):
        
        if cards_played[i-1][0] == 'skip':
            Featured_value[i] = Featured_value[i-1] + 2*Signal
        
        else:
            Featured_value[i] = Featured_value[i-1] + Signal
        
        if cards_played[i][0] == 'reverse':
            Signal = Signal * (-1)
    
    for i in range(len(cards_played)):
        for j in range(num_players):
            if Featured_value[i] % num_players == j:
                results[(j+starting_player-1)%num_players].append(cards_played[i])
    return results






def catch_cheater(cards_played, initial_card,num_players=4,starting_player=1):
    
    cards_played_1 = []
    cards_played_1.append(initial_card)
    for i in range(len(cards_played)):
        cards_played_1.append(cards_played[i])
    
    
    for i in range(len(cards_played_1)):
        cards_played_1[i].append(i)     
    
    records = []
    
    for i in range(1,len(cards_played_1)):
        if cards_played_1[i][0] != cards_played_1[i-1][0] and cards_played_1[i][1] != cards_played_1[i-1][1]:
            records.append(cards_played_1[i])
    
    if records == []:
        return None
    
    check = uno_who_played_what_1(cards_played_1,num_players,starting_player)
    for i in range(len(check)):
        for j in range(len(check[i])):
            if check[i][j] == records[0]:
                return i
              
                    

