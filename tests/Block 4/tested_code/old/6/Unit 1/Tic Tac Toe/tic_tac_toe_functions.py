  





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
    if (board[0][0] == board[1][0] == board[2][0] == 'x') or \
       (board[0][1] == board[1][1] == board[2][1] == 'x') or \
       (board[0][2] == board[1][2] == board[2][2] == 'x') or \
       (board[0][0] == board[1][1] == board[2][2] == 'x') or \
       (board[0][2] == board[1][1] == board[2][0] == 'x') or \
       (board[0][0] == board[0][1] == board[0][2] == 'x') or \
       (board[1][0] == board[1][1] == board[1][2] == 'x') or \
       (board[2][0] == board[2][1] == board[2][2] == 'x'):

        return 'x'
    
    elif (board[0][0] == board[1][0] == board[2][0] == 'o') or \
       (board[0][1] == board[1][1] == board[2][1] == 'o') or \
       (board[0][2] == board[1][2] == board[2][2] == 'o') or \
       (board[0][0] == board[1][1] == board[2][2] == 'o') or \
       (board[0][2] == board[1][1] == board[2][0] == 'o') or \
       (board[0][0] == board[0][1] == board[0][2] == 'o') or \
       (board[1][0] == board[1][1] == board[1][2] == 'o') or \
       (board[2][0] == board[2][1] == board[2][2] == 'o'):

        return 'o' 
    
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    if move[0] not in ['1', '2', '3'] or \
       move[1] not in ['A', 'B', 'C']:
        return False

    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    if board[row][column] != ' ':
        return False

    
    else:
        board[row][column] = player
        return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'
