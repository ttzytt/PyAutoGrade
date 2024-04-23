



i = 0

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
          + row[8] + ' │ ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8], 9)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   ')


def find_winner(board):
    for i in range(9):
        for j in range(0,5):
            if (board[i][j]!=' ')and(board[i][j] == board[i][j+1]) and (board[i][j+1] ==board[i][j+2]) and (board[i][j+2] == board[i][j+3]) and (board[i][j+3] == board[i][j+4]):

                return True
    for i in range(5):
        for j in range(9):
            if (board[i][j]!=' ')and(board[i][j] == board[i+1][j]) and (board[i+1][j]==board[i+2][j]) and (board[i+2][j] == board[i+3][j]) and (board[i+3][j]== board[i+4][j]):

                return True
    for i in range(5):
        for j in range(5):
            if (board[i][j]!=' ')and(board[i][j] == board[i+1][j-1]) and (board[i+1][j-1] == board[i+2][j-2]) and (board[i+2][j-2] == board[i+3][j-3]) and (board[i+3][j-3] == board[i+4][j-4]):

                return True

    for i in range(4,9):
        for j in range(4,9):
            if (board[i][j]!=' ')and(board[i][j] == board[i-1][j-1]) and (board[i-1][j-1] == board[i-2][j-2]) and (board[i-2][j-2] == board[i-3][j-3]) and (board[i-3][j-3] == board[i-4][j-4]):

                return True

    for i in range(1,8):
        for j in range(1,8):
            if (board[i][j]!=' ')and(board[i][j] == board[i+1][j]) and (board[i-1][j]==board[i][j]) and (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j-1]):
    
                return True
         
    return False






def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, should be a number 1, 2, or 3`
                followed by a capital letter A, B, or C, such as
                '2C'
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is already occupied,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    if len(move) != 2:
        ret = 1
        return False
    if (move[0] != '1' and move[0] != '2' and move[0] != '3' and
       move[0] != '4' and move[0] != '5' and move[0] != '6' and
       move[0] != '7' and move[0] != '8' and move[0] != '9'):
        ret = 1
        return False

    if (move[1] != 'A' and move[1] != 'B' and move[1] != 'C' and
       move[1] != 'D' and move[1] != 'E' and move[1] != 'F' and
       move[1] != 'G' and move[1] != 'H' and move[1] != 'I'):
        ret = 1
        return False

    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')
    
    if board[row][column] != ' ':
        ret = 1
        return False



    
    board[row][column] = player

    return True








def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'
