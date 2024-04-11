






def deal_3_hands(deck): 

    hands = ([],[],[])
    count = 0

    for count in range(len(deck)):
        
        hands[count%3].append(deck[count])
        
        
    return hands






def uno_who_played_what(card): 
    
    
    
    
    
    hands = ([],[],[],[])
    judge = 1 
    count = 0
    list = 0
    
        
    while count < len(card):
        
        hands[list].append(card[count])

        
        if card[count] == 'reverse':
            judge += 1
        elif card[count] != 'reverse':
            judge *= 1 

        
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
            count += 1
            
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
            count += 1
        
    return hands




def play_amount(card): 

    amount = [0,0,0,0]
    
    judge = 1 
    count = 0
    list = 0
        
    while count < len(card):

        amount[list] += 1

        if card[count] == 'reverse':
            judge += 1
        elif card[count] != 'reverse':
            judge *= 1    

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
            count += 1
            
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
            count += 1
        
    return amount



def uno_bonus_5(card,num,start): 

    if num <= start:
        return None
    
    hands = []
    for i in range(num):
        hands.append([])
    judge = 1 
    list = start
    
    for count in range(len(card)):
        
        hands[list].append(card[count])

        
        if card[count] == 'reverse':
            judge += 1
            
        if judge % 2 == 1: 
            if card[count] != 'skip':
                
                if list >= num-1:
                    list -= num-1
                elif list <= num-2:
                    list += 1
            elif card[count] == 'skip':
                if list >= num-2:
                    list -= num-2
                elif list <= num-3:
                    list += 2
            
        elif judge % 2 == 0: 
            if card[count] != 'skip':
                if list <= 0:
                    list += num-1
                elif list >= 1:
                    list -= 1
            elif card[count] == 'skip':
                if list <= 1:
                    list += num-2
                elif list >= 2:
                    list -= 2
                    
    return hands


def uno_bonus_6(card,ini,num,start):

    if num <= start:
        return None

    judge = 1
    list = 1 + start
    if card[0][0] != ini[0] and card[0][1] != ini[1]:
        return 0

    for count in range(1,len(card)):
        if (card[count][0] == card[count-1][0]
            or card[count][1] == card[count-1][1]): 
        
            if card[count][1] == 'reverse':
                judge += 1
        
            if judge % 2 == 1: 
                if card[count][1] != 'skip':
                    if list >= num-1:
                        list -= num-1
                    elif list <= num-2:
                        list += 1
                elif card[count][1] == 'skip':
                    if list >= num-2:
                        list -= num-2
                    elif list <= num-3:
                        list += 2
            
            elif judge % 2 == 0: 
                if card[count][1] != 'skip':
                    if list <= 0:
                        list += num-1
                    elif list >= 1:
                        list -= 1
                elif card[count][1] == 'skip':
                    if list <= 1:
                        list += num-2
                    elif list >= 2:
                        list -= 2
                        
        elif (card[count][0] != card[count-1][0]
            and card[count][1] != card[count-1][1]):

            return list

           
    return None





    
    

        

    
    

   
