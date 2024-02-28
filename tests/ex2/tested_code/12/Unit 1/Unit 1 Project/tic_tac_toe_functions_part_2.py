





def draw_row(row, row_number):
    
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ '
          + row[6] + ' │ '
          + row[7] + ' │ '
          + row[8] + ' │ '
          + row[9] + ' │ ')
    


def draw_board(board):

    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8], 9)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[9], 0)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')





def six_blocks(board):

    
    for column in range(10):

            for row in range(5):

                if ((board[column][row] == board[column][row+1]
                    == board[column][row+2] == board[column][row+3] == board[column][row+4])
                    and board[column][row+5] == ' '):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for row in range(10):

            for column in range(5):

                if ((board[column][row] == board[column+1][row]
                    == board[column+2][row] == board[column+3][row] == board[column+4][row])
                    and board[column+5][row] == ' '):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for column in range(5):

            for row in range(5):

                if ((board[column][row] == board[column+1][row+1]
                    == board[column+2][row+2] == board[column+3][row+3] == board[column+4][row+4])
                    and board[column+5][row+5] == ' '):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for column in range(5):

            for row in range(9,4,-1):

                if ((board[column][row] == board[column+1][row-1]
                    == board[column+2][row-2] == board[column+3][row-3] == board[column+4][row-4])
                    and board[column+5][row-5] == ' '):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'
                    

    for column in range(10):

            for row in range(1,6):

                if ((board[column][row] == board[column][row+1]
                    == board[column][row+2] == board[column][row+3] == board[column][row+4])
                    and board[column][row-1] == ' '):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for row in range(10):

            for column in range(1,6):

                if ((board[column][row] == board[column+1][row]
                    == board[column+2][row] == board[column+3][row] == board[column+4][row])
                    and board[column-1][row] == ' '):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for column in range(1,6):

            for row in range(1,6):

                if ((board[column][row] == board[column+1][row+1]
                    == board[column+2][row+2] == board[column+3][row+3] == board[column+4][row+4])
                    and board[column-1][row-1] == ' '):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    
    for column in range(1,6):

            for row in range(8,3,-1):

                if ((board[column][row] == board[column+1][row-1]
                    == board[column+2][row-2] == board[column+3][row-3] == board[column+4][row-4])
                    and board[column-1][row+1] == ' '):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'






def find_winner(board,move,last_move): 

    if len(last_move) >= 3 and len(move) >= 3:

        if last_move[2] == 'W' and move[2] == 'R':

            return None

    if len(move) >= 3:

        if move[2] == 'W':

            return None
        
    elif len(move) <= 2:

        if last_move == 'NNN' and six_blocks(board) == None: 

            return None

        
        for column in range(10):

            for row in range(6):

                if (board[column][row] == board[column][row+1]
                    == board[column][row+2] == board[column][row+3] == board[column][row+4]):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

        
        for row in range(10):

            for column in range(6):

                if (board[column][row] == board[column+1][row]
                    == board[column+2][row] == board[column+3][row] == board[column+4][row]):
                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

        
        for column in range(6):

            for row in range(6):

                if (board[column][row] == board[column+1][row+1]
                    == board[column+2][row+2] == board[column+3][row+3] == board[column+4][row+4]):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

        
        for column in range(6):

            for row in range(9,3,-1):

                if (board[column][row] == board[column+1][row-1]
                    == board[column+2][row-2] == board[column+3][row-3] == board[column+4][row-4]):

                    if board[column][row] == 'x':
                        return 'x'
                    elif board[column][row] == 'o':
                        return 'o'

    return None






def make_move(player,move,board):

    
    if (len(move) >= 3 and move[2] != 'W' and move[2] != 'R') or len(move) < 2: 
        if move == 'quit' or move == 'undo':
        
            return True

    
    
    elif len(move) == 2 or move[2] == 'W' or move[2] == 'R': 

        if len(move) >= 3:

            if len(move) == 3 and (move[2] == 'W' or move[2] == 'R'):

                if about_to_win(board) == False:

                    return 'format'

            elif len(move) >= 4:

                return 'format'

        if ((move[0] == '1' or move[0] == '2' or move[0] == '3' or move[0] == '4' or move[0] == '5'
                or move[0] == '6' or move[0] == '7' or move[0] == '8' or move[0] == '9' or move[0] == '0')
            and (move[1] == 'A' or move[1] == 'B' or move[1] == 'C' or move[1] == 'D' or move[1] == 'E'
                or move[1] == 'F' or move[1] == 'G' or move[1] == 'H' or move[1] == 'I' or move[1] == 'J')):
                

            row = int(move[0])-1
            column = ord(move[1])-ord('A')
            
            if board[row][column] == ' ':
                

                
                board[row][column] = player
                
                return True

            else:

                return 'occupied'

    return 'format'



def undo_last_step(board,last_step,move,player):

    if (move == 'undo' and last_step != 'undo'
        and board[int(last_step[0])-1][ord(last_step[1])-ord('A')] != player):
        
        

        board[int(last_step[0])-1][ord(last_step[1])-ord('A')] = ' '

        return True

    return False

        




def about_to_win(board):

    
    for column in range(10):
        
        if (board[column][6] == board[column][7] == board[column][8] == board[column][9]
            and board[column][5] == ' '):
            
            if board[column][6] == 'x':
                return 'x'
            elif board[column][6] == 'o':
                return 'o'


    for column in range(10):

        if (board[column][0] == board[column][1] == board[column][2] == board[column][3]
            and board[column][4] == ' '):

            if board[column][0] == 'x':
                return 'x'
            elif board[column][0] == 'o':
                return 'o'


    for row in range(10):

        if (board[0][row] == board[1][row] == board[2][row] == board[3][row]
            and board[4][row] == ' '):

            if board[0][row] == 'x':
                return 'x'
            elif board[0][row] == 'o':
                return 'o'

    for row in range(10):

        if (board[6][row] == board[7][row] == board[8][row] == board[9][row]
            and board[5][row] == ' '):

            if board[6][row] == 'x':
                return 'x'
            elif board[6][row] == 'o':
                return 'o'


    for column in range(6):
        
        if (board[column][0] == board[column+1][1] == board[column+2][2] == board[column+3][3]
            and board[column+4][4] == ' '):

            if board[column][0] == 'x':
                return 'x'
            elif board[column][0] == 'o':
                return 'o'

            
    for column in range(9,3,-1):

        if (board[column][0] == board[column-1][1] == board[column-2][2] == board[column-3][3]
            and board[column-4][4] == ' '):

            if board[column][0] == 'x':
                return 'x'
            elif board[column][0] == 'o':
                return 'o'


    for column in range(6):

        if (board[column][9] == board[column+1][8] == board[column+2][7] == board[column+3][6]
            and board[column+4][5] == ' '):

            if board[column][9] == 'x':
                return 'x'
            elif board[column][9] == 'o':
                return 'o'


    for column in range(9,3,-1):

        if (board[column][9] == board[column-1][8] == board[column-2][7] == board[column-3][6]
            and board[column-4][5] == ' '):

            if board[column][9] == 'x':
                return 'x'
            elif board[column][9] == 'o':
                return 'o'


    for row in range(6):

        if (board[0][row] == board[1][row+1] == board[2][row+2] == board[3][row+3]
            and board[4][row+4] == ' '):

            if board[0][row] == 'x':
                return 'x'
            elif board[0][row] == 'o':
                return 'o'

    for row in range(9,3,-1):

        if (board[0][row] == board[1][row-1] == board[2][row-2] == board[3][row-3]
            and board[4][row-4] == ' '):

            if board[0][row] == 'x':
                return 'x'
            elif board[0][row] == 'o':
                return 'o'


    for row in range(6):

        if (board[9][row] == board[8][row+1] == board[7][row+2] == board[6][row+3]
            and board[5][row+4] == ' '):

            if board[9][row] == 'x':
                return 'x'
            elif board[9][row] == 'o':
                return 'o'


    for row in range(9,3,-1):

        if (board[9][row] == board[8][row-1] == board[7][row-2] == board[6][row-3]
            and board[5][row-4] == ' '):

            if board[9][row] == 'x':
                return 'x'
            elif board[9][row] == 'o':
                return 'o'

    for column in range(10):

        for row in range(5):
            
            if (board[column][row+1] == board[column][row+2] == board[column][row+3]
                == board[column][row+4] and (board[column][row] == ' ' or board[column][row+5] == ' ')):

                if board[column][row+1] == 'x':
                    return 'x'
                elif board[column][row+1] == 'o':
                    return 'o'

    for row in range(10):

        for column in range(5):
            
            if (board[column+1][row] == board[column+2][row] == board[column+3][row]
                == board[column+4][row] and (board[column][row] == ' ' or board[column+5][row] == ' ')):

                if board[column+1][row] == 'x':
                    return 'x'
                elif board[column+1][row] == 'o':
                    return 'o'
                
    for column in range(5):

        for row in range(5):

            if (board[column+1][row+1] == board[column+2][row+2] == board[column+3][row+3]
                == board[column+4][row+4] and (board[column][row] == ' ' or board[column+5][row+5] == ' ')):

                if board[column+1][row+1] == 'x':
                    return 'x'
                elif board[column+1][row+1] == 'o':
                    return 'o'

    for column in range(5):

        for row in range(9,4,-1):

            if (board[column+1][row-1] == board[column+2][row-2] == board[column+3][row-3]
                == board[column+4][row-4] and (board[column][row] == ' ' or board[column+5][row-5] == ' ')):

                if board[column+1][row-1] == 'x':
                    return 'x'
                elif board[column+1][row-1] == 'o':
                    return 'o'

    
    for column in range(10):

        for row in range(6):

            if (board[column][row] == ' ' and (board[column][row+1] == board[column][row+2] == board[column][row+3])
                and board[column][row+4] == ' '):

                if board[column][row+1] == 'x':
                    return 'x'
                elif board[column][row+1] == 'o':
                    return 'o'
                
    for row in range(10):
        
        for column in range(6):

            if (board[column][row] == ' ' and (board[column+1][row] == board[column+2][row] == board[column+3][row])
                and board[column+4][row] == ' '):

                if board[column+1][row] == 'x':
                    return 'x'
                elif board[column+1][row] == 'o':
                    return 'o'
              
    for column in range(6):

        for row in range(6):

            if (board[column][row] == ' ' and (board[column+1][row+1] == board[column+2][row+2] == board[column+3][row+3])
                and board[column+4][row+4] == ' '):

                if board[column+1][row+1] == 'x':
                    return 'x'
                elif board[column+1][row+1] == 'o':
                    return 'o'
               
    for column in range(6):

        for row in range(9,3,-1):

            if (board[column][row] == ' ' and (board[column+1][row-1] == board[column+2][row-2] == board[column+3][row-3])
                and board[column+4][row-4] == ' '):
            
                if board[column+1][row-1] == 'x':
                    return 'x'
                elif board[column+1][row-1] == 'o':
                    return 'o'

    return False



def is_full(board,move,last_move):

    for row in range(10):

        for column in range(10):

            
            if board[row][column] == ' ':

                return False

    
    if find_winner(board,move,last_move) != None:

        return False

    return True



def next_player(player):
    
    if player == 'x':
        return 'o'
    
    elif player == 'o':
        return 'x'





        




