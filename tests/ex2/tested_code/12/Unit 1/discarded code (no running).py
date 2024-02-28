





        
    
            
            
        

    
    














    




import random
    random.seed()
    automove = random.choice(['1A','2A','3A','1B','2B','3B','1C','2C','3C'])
    which_one_move = 1

    if which_one_move % 2 == 1: # User's turn
        if (move == '1A' or move == '2A' or move == '3A' or move == '1B' or move == '2B'
            or move == '3B' or move == '1C' or move == '2C' or move == '3C'):

            if (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
                or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '): 
            
                board[int(move[0])-1][ord(move[1])-ord('A')] = player
                which_one_move += 1
            
                return True
        
        return False

    elif which_one_move % 2 == 0: 
        move = automove
        while (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
            or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '): 
            move = random.choice(['1A','2A','3A','1B','2B','3B','1C','2C','3C'])
            
        if make_move(player,move,board) == True:
            board[int(move[0])-1][ord(move[1])-ord('A')] = player
            which_one_move += 1
            return True
        return False

