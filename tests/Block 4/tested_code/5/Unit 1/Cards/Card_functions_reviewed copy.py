




def deal_3_hands(deck):

    
    hands = [[],[],[]]
    
    for i in range(len(deck)):
        
        hands[i%3].append(deck[i])
        
    return hands








def uno_who_played_what(cards_played):

    
    hands = [ [],[],[],[] ]
    count = 0
    is_reverse = False

    for i in range(len(cards_played)):
        hands[count%4].append(cards_played[i])
        
        
        if cards_played[i] == 'reverse':
            if is_reverse:
                is_reverse = False
                count += 1
            else:
                is_reverse = True
                count -= 1
                
        
        elif cards_played[i] == 'skip':
            if is_reverse == True:
                count -= 2
            else:
                count += 2
                
        else:
            if is_reverse:
                count -= 1
            else:
                count += 1

    return hands



            
            
            
    

