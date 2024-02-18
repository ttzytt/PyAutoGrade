





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
    
    
    
    
    for row in range(len(board)):
        if (board[row][0] == board[row][1]
                and board[row][0] == board[row][2]
                and board[row][0] != ' '):
            return board[row][0]
        
    for column in range(len(board)):
        if (board[0][column] == board[1][column]
                and board[0][column] == board[2][column]
                and board[0][column] != ' '):
            return board[0][column]
        
    if (board[0][0] == board[1][1]
            and board[0][0] == board[2][2]
            and board[0][0] != ' '):
        return board[0][0]

    elif (board[2][0] == board[1][1]
              and board[2][0] == board[0][2]
              and board[2][0] != ' '):
        return board[2][0]
    
    else:
        return None

    
    




def get_move(player):
    return input(player + ' player, chose your move: ')
    


def make_move(player, move, board):

    
    
    if len(move) != 2:
        return False
    if move[0] != '1' and move[0] != '2' and move[0] != '3':
        return False
    if move[1] != 'A' and move[1] !='B' and move[1] != 'C':
        return False
    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')
    

    
    if board[row][column] == ' ':
        board[row][column] = player
        return True
    else:
        return False
    





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

