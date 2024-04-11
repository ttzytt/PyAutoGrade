





def deal_3_hands(deck):
    i = 0
    hand_1 = []
    hand_2 = []
    hand_3 = []
    while i < len(deck): 
        if i % 3 == 0:
            hand_1.append(deck[i])
        elif i % 3 == 1:
            hand_2.append(deck[i])
        elif i % 3 == 2:
            hand_3.append(deck[i])
        i += 1
    return [hand_1, hand_2, hand_3]

        

def uno_who_played_what(cards_played):
    i = 0
    player_turn = 0
    reverse_or_not = False
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []

    while i < len(cards_played):
        if player_turn % 4 == 0:
            player_1.append(cards_played[i])
        elif player_turn % 4 == 1:
            player_2.append(cards_played[i])
        elif player_turn % 4 == 2:
            player_3.append(cards_played[i])
        elif player_turn % 4 == 3:
            player_4.append(cards_played[i])



        if cards_played[i] == 'skip':
            player_turn += 1

        elif cards_played[i] == 'reverse' or reverse_or_not == True:
            if cards_played[i] == 'reverse' and reverse_or_not == True:
                reverse_or_not = False
            else:
                player_turn -= 2
                reverse_or_not = True   
                
        i += 1
        player_turn += 1

    return [player_1, player_2, player_3, player_4]
            
            
            
