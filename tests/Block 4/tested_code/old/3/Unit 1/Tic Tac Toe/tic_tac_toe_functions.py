







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

    
    if (board[0][0] == board[1][0] == board[2][0] == 'x' 
            or board[0][1] == board[1][1] == board[2][1] == 'x'
            or board[0][2] == board[1][2] == board[2][2] == 'x'
            or board[0][0] == board[0][1] == board[0][2] == 'x' 
            or board[1][0] == board[1][1] == board[1][2] == 'x'
            or board[2][0] == board[2][1] == board[2][2] == 'x'
            or board[0][0] == board[1][1] == board[2][2] == 'x' 
            or board[0][2] == board[1][1] == board[2][0] == 'x'):
        return 'x'

    elif (board[0][0] == board[1][0] == board[2][0] == 'o'
            or board[0][1] == board[1][1] == board[2][1] == 'o'
            or board[0][2] == board[1][2] == board[2][2] == 'o'
            or board[0][0] == board[0][1] == board[0][2] == 'o'
            or board[1][0] == board[1][1] == board[1][2] == 'o'
            or board[2][0] == board[2][1] == board[2][2] == 'o'
            or board[0][0] == board[1][1] == board[2][2] == 'o'
            or board[0][2] == board[1][1] == board[2][0] == 'o'):
        return 'o'

    else:
        
        return None







def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    elif move[0] != '1' and move[0] != '2' and move[0] != '3':
        return False
    elif move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
        return False
    
    row = int(move[0]) - 1
    column = ord(move[1]) - ord('A')
    if board[row][column] != ' ':
        return False
    
    board[row][column] = player
    return True


def get_move(player):
    move = input(player + ', choose you move: ')
    return move





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'
