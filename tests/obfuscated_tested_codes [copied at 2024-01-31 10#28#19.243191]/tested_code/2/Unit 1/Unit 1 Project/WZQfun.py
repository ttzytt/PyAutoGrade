


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
    print('    A   B   C   D   E   F   G   H   I   J')
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[8], 9)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[9], 0)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘')
    print('    A   B   C   D   E   F   G   H   I   J')


def make_move(player, move, board):
    if len(move) != 2:
        return False

    if move[0] not in '1234567890' or move[1] not in 'ABCDEFGHIJ':
        return False 

    row = int(move[0]) - 1

    
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
     


def is_board_full(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False  
    return True
    

def find_winner(board):
    
    for row in range(10):
        for col in range(6):
            
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == board[row][col+4] and board[row][col] != ' ':
                return board[row][col]
    
    for col in range(10):
        for row in range(6):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == board[row+4][col]and board[row][col] != ' ':
                return board[row][col]
    
    for col in range(6):
        for row in range(6):
           
                if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4]and board[row][col] != ' ':
                    return board[row][col]
    
    for col in range(4, 10):
        for row in range(6):
            
                if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row+4][col-4]and board[row][col] != ' ':
                    return board[row][col]
    return None  

def get_move(player):
    return input(player + ' player, chose your move: ')
