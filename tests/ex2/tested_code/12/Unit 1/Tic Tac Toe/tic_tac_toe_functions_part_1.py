












def draw_row(row, row_number):
    
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ ')
    


def draw_board(board):

    print('  ┌───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')
    



def find_winner(board):
    if (board[0][0] == board[0][1] == board[0][2] == 'x'
           or board[1][0] == board[1][1] == board[1][2] == 'x'
           or board[2][0] == board[2][1] == board[2][2] == 'x'
           or board[0][0] == board[1][0] == board[2][0] == 'x'
           or board[0][1] == board[1][1] == board[2][1] == 'x'
           or board[0][2] == board[1][2] == board[2][2] == 'x'
           or board[0][0] == board[1][1] == board[2][2] == 'x'
           or board[0][2] == board[1][1] == board[2][0] == 'x'):
        return 'x' 
    elif (board[0][0] == board[0][1] == board[0][2] == 'o'
           or board[1][0] == board[1][1] == board[1][2] == 'o'
           or board[2][0] == board[2][1] == board[2][2] == 'o'
           or board[0][0] == board[1][0] == board[2][0] == 'o'
           or board[0][1] == board[1][1] == board[2][1] == 'o'
           or board[0][2] == board[1][2] == board[2][2] == 'o'
           or board[0][0] == board[1][1] == board[2][2] == 'o'
           or board[0][2] == board[1][1] == board[2][0] == 'o'):
        return 'o' 
    else:
        return None

    



def get_move(player):
    return input(player + ' player, chose your move: ')




def make_move(player,move,board):

    if (move == '1A' or move == '2A' or move == '3A' or move == '1B' or move == '2B'
        or move == '3B' or move == '1C' or move == '2C' or move == '3C'):
        

        
        
        
        
        
        
        if (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
            or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '):
            

            board[int(move[0])-1][ord(move[1])-ord('A')] = player
            
            return True
        
    return False



def is_full(board):
    if (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' '
        and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' '
        and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' '):
        if find_winner(board) == None:
            return True
        else:
            return True
    else:
        return False






def next_player(player):
    if player == 'x':
        return 'o'
    else: 
        return 'x'

