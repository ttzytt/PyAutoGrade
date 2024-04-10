





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
    for i in range(3):
        if((board[i][0] != ' ') and
           (board[i][0] == board[i][1]) and
           (board[i][0] == board[i][2])):
            return board[i][0]
        elif((board[0][i] != ' ') and
             (board[0][i] == board[1][i]) and
             (board[0][i] == board[2][i])):
            return board[0][i]
    if(board[1][1] != ' '):
        if((board[0][0] == board[1][1]) and
           (board[2][2] == board[1][1])):
            return board[1][1]
        elif((board[0][2] == board[1][1]) and
           (board[2][0] == board[1][1])):
            return board[1][1]
    if((board[0][0] != ' ') and (board[0][1] != ' ') and
       (board[0][2] != ' ') and (board[1][0] != ' ') and
       (board[1][1] != ' ') and (board[1][2] != ' ') and
       (board[2][0] != ' ') and (board[2][1] != ' ') and
       (board[2][2] != ' ')):
        return 'tie'
            
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if((len(move) != 2) or not('A' <= move[1] < 'D') or
       not(str(0) < move[0] < str(4))):
        return False
    

    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    if(board[row][column] != ' '):
        return False
    
    board[row][column] = player
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

