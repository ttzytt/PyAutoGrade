





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
    
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != ' ':
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != ' ':
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != ' ':
        return board[2][0]

    
    if board[0][0] == board[1][0] and board[2][0] == board[0][0] and board[0][0] != ' ':
        return board[0][0]
    if board[0][1] == board[1][1] and board[2][1] == board[0][1] and board[0][1] != ' ':
        return board[0][1]
    if board[0][2] == board[1][2] and board[2][2] == board[0][2] and board[0][2] != ' ':
        return board[0][2]

    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')





def make_move(player, move, board):
    
    
    if len(move) == 0 or len(move) > 2:
        return False
    if move[0] != '1' and move[0] != '2' and move[0] != '3':
        return False
    if move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
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
