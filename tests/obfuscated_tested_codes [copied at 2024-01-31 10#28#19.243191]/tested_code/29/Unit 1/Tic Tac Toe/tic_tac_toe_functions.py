








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
    
    if board[0] == ['x', 'x', 'x']:
        return 'x'
    
    elif board[1] == ['x', 'x', 'x']:
        return 'x'
    
    elif board[2] == ['x', 'x', 'x']:
        return 'x'
    
    elif board[0] == ['o', 'o', 'o']:
        return 'o'
    
    elif board[1] == ['o', 'o', 'o']:
        return 'o'
    
    elif board[2] == ['o', 'o', 'o']:
        return 'o'

    
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == 'x':
        return 'x'
    
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == 'o':
        return 'o'
    
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == 'x':
        return 'x'
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == 'o':
        return 'o'
    
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == 'x':
        return 'x'
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == 'o':
        return 'o'
    
    
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'x':
        return 'x'
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'o':
        return 'o'
    
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == 'x':
        return 'x'
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == 'o':
        return 'o'



def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if not(len(move) == 2):
        return False

    if not(ord(move[0]) >= 49 and ord(move[0]) <= 57):
            return False
    if not(ord(move[1]) >= 65 and ord(move[1]) <= 67):
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
