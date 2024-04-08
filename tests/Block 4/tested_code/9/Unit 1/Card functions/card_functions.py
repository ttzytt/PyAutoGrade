





def deal_3_hands(deck): 

    hands = [[],[],[]]
    count = 0

    for count in range(len(deck)):
        
        hands[count%3].append(deck[count])
        
        
    return hands






def uno_who_played_what(cards_played): 

    
    hands = [[],[],[],[]]
    judge = 1 
    list = 0
   
    for count in range(len(cards_played)):
        
        hands[list].append(cards_played[count])

        
        if cards_played[count] == 'reverse':
            judge += 1
        
        if judge % 2 == 1: 
            if cards_played[count] != 'skip':
                
                if list >= 3:
                    list -= 3
                elif list <= 2:
                    list += 1
            elif cards_played[count] == 'skip':
                if list >= 2:
                    list -= 2
                elif list <= 1:
                    list += 2
            
        elif judge % 2 == 0: 
            if cards_played[count] != 'skip':
                if list <= 0:
                    list += 3
                elif list >= 1:
                    list -= 1
            elif cards_played[count] == 'skip':
                if list <= 1:
                    list += 2
                elif list >= 2:
                    list -= 2
           
    return hands




def who_played_how_many(card): 

    amount = [0,0,0,0]
    
    judge = 1 
    list = 0
        
    for count in range(len(card)):

        amount[list] += 1

        if card[count] == 'reverse':
            judge += 1

        if judge % 2 == 1: 
            if card[count] != 'skip':
                if list >= 3:
                    list -= 3
                elif list <= 2:
                    list += 1
            elif card[count] == 'skip':
                if list >= 2:
                    list -= 2
                elif list <= 1:
                    list += 2

        elif judge % 2 == 0: 
            if card[count] != 'skip':
                if list <= 0:
                    list += 3
                elif list >= 1:
                    list -= 1
            elif card[count] == 'skip':
                if list <= 1:
                    list += 2
                elif list >= 2:
                    list -= 2

    return amount




def uno_who_played_what_2(cards_played,num_players,starting_player): 

    if num_players <= starting_player:
        return None
    
    hands = []
    for i in range(num_players):
        hands.append([]) 
    judge = 1 
    list = starting_player 
    
    for count in range(len(cards_played)):
        
        hands[list].append(cards_played[count])

        
        if cards_played[count] == 'reverse':
            judge += 1
            
        if judge % 2 == 1: 
            if cards_played[count] != 'skip':
                
                if list >= num_players - 1:
                    list -= num_players - 1
                elif list <= num_players - 2:
                    list += 1
            elif cards_played[count] == 'skip':
                if list >= num_players - 2:
                    list -= num_players - 2
                elif list <= num_players - 3:
                    list += 2
            
        elif judge % 2 == 0: 
            if cards_played[count] != 'skip':
                if list <= 0:
                    list += num_players - 1
                elif list >= 1:
                    list -= 1
            elif cards_played[count] == 'skip':
                if list <= 1:
                    list += num_players - 2
                elif list >= 2:
                    list -= 2
                    
    return hands



def catch_cheater(cards_played,initial_card,num_players,starting_player): 

    if num_players <= starting_player:
        return None
        
        

     
    judge = 1
    list = 1 + starting_player
    
    if (cards_played[0][0] != initial_card[0]
        and cards_played[0][1] != initial_card[1]):
        
        return 0
        
        

    for count in range(1,len(cards_played)):
        
        
        if (cards_played[count][0] == cards_played[count-1][0]
            or cards_played[count][1] == cards_played[count-1][1]):
            
            
        
            if cards_played[count][1] == 'reverse':
                judge += 1
        
            if judge % 2 == 1: 
                if cards_played[count][1] != 'skip':
                    if list >= num_players - 1:
                        list -= num_players - 1
                    elif list <= num_players - 2:
                        list += 1
                elif cards_played[count][1] == 'skip':
                    if list >= num_players - 2:
                        list -= num_players - 2
                    elif list <= num_players - 3:
                        list += 2
            
            elif judge % 2 == 0: 
                if cards_played[count][1] != 'skip':
                    if list <= 0:
                        list += num_players - 1
                    elif list >= 1:
                        list -= 1
                elif cards_played[count][1] == 'skip':
                    if list <= 1:
                        list += num_players - 2
                    elif list >= 2:
                        list -= 2
                        
        elif (cards_played[count][0] != cards_played[count-1][0]
            and cards_played[count][1] != cards_played[count-1][1]):

            return list
            
       
    return None
    





    
    

        

    
    

   
