







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
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 'x':
                return 'x'
            elif board[i][0] == 'o':
                return 'o'
            
            
            if board[i][0] != ' ':
                return board[i][0]

    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == 'x':
                return 'x'
            elif board[0][i] == 'o':
                return 'o'
            
            
            if board[0][i] != ' ':
                return board[i][0]
    
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            return 'x'
        elif board[0][0] == 'o':
            return 'o'
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[2][0] == 'x':
            return 'x'
        elif board[2][0] == 'o':
            return 'o'
    return None



def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    elif not ('1' <= move[0] <= '3'):
        return False
    elif move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
        return False
    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] != ' ':
        return False
    
    board[row][column] = player
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'



def all_filled(board):
    total_board = board[0] + board[1] + board[2]

    for i in range(len(total_board)):
        if total_board[i] == ' ':
            return False
    return True
        
