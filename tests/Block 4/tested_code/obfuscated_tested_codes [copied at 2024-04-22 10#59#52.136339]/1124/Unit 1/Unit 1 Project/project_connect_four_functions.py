



"""
The following functions are for use in making a Tic-Tac-Toe game.

For all of the code below, a board 3 by 3 is a list of lists of the
form
        [ [' ', 'o', ' '],
          ['x', ' ', 'x'],
          ['x', 'o', ' '] ]
(Each entry is an 'x', 'o', or ' '.)

For the user, a board will be printed in the form
      ┌───┬───┬───┐ 
    1 │   │ o │   │ 
      ├───┼───┼───┤ 
    2 │ x │   │ x │ 
      ├───┼───┼───┤ 
    3 │ x │ o │   │ 
      └───┴───┴───┘ 
        A   B   C

Moves/spaces are referred to by strings such as '1A' or '2C'.
"""


"""
Print the given row to the screen.
Input:
    row            a list representing one row of the board
    row_number     int to be printed before the row
"""
def draw_row(row, row_number, num_spaces):
    print(' '*num_spaces + str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')


def draw_board(board):
    print(' Layer W')
    print('  ┌───┬───┬───┬───┐ ')
    draw_row(board[0][0], 1, 0)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[0][1], 2, 0)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[0][2], 3, 0)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[0][3], 4, 0)
    print('  └───┴───┴───┴───┘ ')
    print('    A   B   C   D   ')
    print('     Layer X')
    print('      ┌───┬───┬───┬───┐ ')
    draw_row(board[1][0], 1, 4)
    print('      ├───┼───┼───┼───┤ ')
    draw_row(board[1][1], 2, 4)
    print('      ├───┼───┼───┼───┤ ')
    draw_row(board[1][2], 3, 4)
    print('      ├───┼───┼───┼───┤ ')
    draw_row(board[1][3], 4, 4)
    print('      └───┴───┴───┴───┘ ')
    print('        A   B   C   D   ')
    print('         Layer Y')
    print('          ┌───┬───┬───┬───┐ ')
    draw_row(board[2][0], 1, 8)
    print('          ├───┼───┼───┼───┤ ')
    draw_row(board[2][1], 2, 8)
    print('          ├───┼───┼───┼───┤ ')
    draw_row(board[2][2], 3, 8)
    print('          ├───┼───┼───┼───┤ ')
    draw_row(board[2][3], 4, 8)
    print('          └───┴───┴───┴───┘ ')
    print('            A   B   C   D   ')
    print('             Layer Z')
    print('              ┌───┬───┬───┬───┐ ')
    draw_row(board[3][0], 1, 12)
    print('              ├───┼───┼───┼───┤ ')
    draw_row(board[3][1], 2, 12)
    print('              ├───┼───┼───┼───┤ ')
    draw_row(board[3][2], 3, 12)
    print('              ├───┼───┼───┼───┤ ')
    draw_row(board[3][3], 4, 12)
    print('              └───┴───┴───┴───┘ ')
    print('                A   B   C   D   ')


def find_winner(board):
    
    
    for i_1 in range(4):
        for i_2 in range(4):
            if board[i_1][i_2][0] == board[i_1][i_2][1] == board[i_1][i_2][2] == board[i_1][i_2][3]:
                if board[i_1][i_2][0] == 'x':
                    return 'x'
                elif board[i_1][i_2][0] == 'o':
                    return 'o'

    
    for i_1 in range(4):
        for i_2 in range(4):
            if board[0][i_1][i_2] == board[1][i_1][i_2] == board[2][i_1][i_2] == board[3][i_1][i_2]:
                if board[0][i_1][i_2] == 'x':
                    return 'x'
                elif board[0][i_1][i_2] == 'o':
                    return 'o'

    
    for i in range(4):
        if board[i][0][0] == board[i][1][1] == board[i][2][2] == board[i][3][3]:
            if board[i][0][0] == 'x':
                    return 'x'
            elif board[i][0][0] == 'o':
                    return 'o'
                
        if board[i][3][0] == board[i][2][1] == board[i][1][2] == board[i][0][3]:
            if board[i][3][0] == 'x':
                    return 'x'
            elif board[i][3][0] == 'o':
                    return 'o'

    
    for i in range(4):
        if board[0][i][0] == board[1][i][1] == board[2][i][2] == board[3][i][3]:
            if board[0][i][0] == 'x':
                    return 'x'
            elif board[0][i][0] == 'o':
                    return 'o'

        if board[3][i][0] == board[2][i][1] == board[1][i][2] == board[0][i][3]:
            if board[3][i][0] == 'x':
                    return 'x'
            elif board[3][i][0] == 'o':
                    return 'o'

    
    if board[0][0][0] == board[1][1][1] == board[2][2][2] == board [3][3][3]:
        if board[0][0][0] == 'x':
            return 'x'
        elif board[0][0][0] == 'o':
            return 'o'

    if board[0][3][0] == board[1][2][1] == board[2][1][2] == board [3][0][3]:
        if board[0][3][0] == 'x':
            return 'x'
        elif board[0][3][0] == 'o':
            return 'o'
    if board[3][0][0] == board[2][1][1] == board[1][2][2] == board [0][3][3]:
        if board[3][0][0] == 'x':
            return 'x'
        elif board[3][0][0] == 'o':
            return 'o'
    if board[3][3][0] == board[2][2][1] == board[1][1][2] == board [0][0][3]:
        if board[3][3][0] == 'x':
            return 'x'
        elif board[3][3][0] == 'o':
            return 'o'

    return None



def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, should be a number 1, 2, or 3
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
    
    if len(move) != 3:
        return False
    if not ('W' <= move[0] <= 'Z'):
        return False
        
    if not ('A' <= move[1] <= 'D'):
        return False
        
    if not ('1' <= move[2] <= '4'):
        return False
        

    
    
    row = int(move[2]) - 1
    
    
    
    column = ord(move[1]) - ord('A')
    
    layer = ord(move[0]) - ord('W')
    
    
    if board[layer][row][column] != ' ':
        return False
    
    board[layer][row][column] = player
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'




def rotate_layer(layer, times, board):
    
    if not(layer == 'W' or layer == 'X' or layer == 'Y' or layer == 'Z'):
        return False

    if not(times == '1', times == '2', times == '3'):
        return False
    
    rotation_times = int(times)
    
    new_layer = []

    
    if layer == 'W':
        layer = board[0]
    elif layer == 'X':
        layer = board[1]
    elif layer == 'Y':
        layer = board[2]
    elif layer == 'Z':
        layer = board[3]

    
    while rotation_times > 0:
        new_layer.append([layer[3][0], layer[2][0], layer[1][0], layer[0][0]])
        new_layer.append([layer[3][1], layer[2][1], layer[1][1], layer[0][1]])
        new_layer.append([layer[3][2], layer[2][2], layer[1][2], layer[0][2]])
        new_layer.append([layer[3][3], layer[2][3], layer[1][3], layer[0][3]])

        if layer == board[0]:
            board[0] = new_layer
        elif layer == board[1]:
            board[1] = new_layer
        elif layer == board[2]:
            board[2] = new_layer
        elif layer == board[3]:
            board[3] = new_layer
            
        layer = new_layer
        new_layer = []
    
        rotation_times -= 1
    return True
