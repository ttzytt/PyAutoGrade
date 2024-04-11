



"""
The following functions are for use to make the game.

For all of the code below, a board 6 by 6 is a list of lists of the
form
        [ [ 0, 1, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, -1, 0],
          [ 0, 0, 0, 1, 0, 0],
          [ 0, 0, -1, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0] ]
(Each entry is 1 ('o'), -1 ('x'), or 0 (None).)

For the user, a board will be printed in the form
  ┌───┬───┬───┬───┬───┬───┐ 
1 │   │ o │   │   │   │   │ 
  ├───┼───┼───┼───┼───┼───┤ 
2 │   │   │   │   │   │   │ 
  ├───┼───┼───┼───┼───┼───┤ 
3 │   │   │   │   │ x │   │ 
  ├───┼───┼───┼───┼───┼───┤ 
4 │   │   │   │ o │   │   │ 
  ├───┼───┼───┼───┼───┼───┤ 
5 │   │   │ x │   │   │   │ 
  ├───┼───┼───┼───┼───┼───┤ 
6 │   │   │   │   │   │   │ 
  └───┴───┴───┴───┴───┴───┘ 
    A   B   C   D   E   F   

Moves/spaces are referred to by strings such as '1A' or '2C'.
"""

def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ ')



def draw_board(board):
    visual_board = [ [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ']]
    for i in range(6):
        for j in range(6):
            if board[i][j] == 1:
                visual_board[i][j] = 'o'
            if board[i][j] == -1:
                visual_board[i][j] = 'x'

    print('  ┌───┬───┬───┬───┬───┬───┐ ')
    draw_row(visual_board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(visual_board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(visual_board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(visual_board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(visual_board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(visual_board[5], 6)
    print('  └───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   ')




def find_winner(board):

    
    def row_test(i, board):
        sum_row = sum(board[i])
        front_check = sum_row - board[i][0]
        back_check = sum_row - board[i][5]
        
        if front_check == 5 or back_check == 5:
            return 'o'
        if front_check == -5 or back_check == -5:
            return 'x'

    
    for i in range(6):
        if row_test(i, board) == 'o':
            return 'o'
        if row_test(i, board) == 'x':
            return 'x'
   
    
    column_board = [[],[],[],[],[],[]]
    for i in range(6):
        for j in range(6):
            column_board[i].append(board[j][i])

    
    for i in range(6):
        if row_test(i, column_board) == 'o':
            return 'o'
        if row_test(i, column_board) == 'x':
            return 'x'

    
    long_diag_list = [ [], [] ]
    for i in range(6):
        long_diag_list[0].append(board[i][i])
        long_diag_list[1].append(board[i][5 - i])

    for i in range(2):
        if row_test(i, long_diag_list) == 'o':
            return 'o'
        if row_test(i, long_diag_list) == 'x':
            return 'x'
    
        
    
    def sum_diag(row, column, direction):
        diag_sum = 0
        if direction == 1:
            while row <= 5 and column <= 5:
                diag_sum = diag_sum + board[row][column]
                row = row + 1
                column = column + 1
        if direction == -1:
            while row <= 5 and column >= 0:
                diag_sum = diag_sum + board[row][column]
                row = row + 1
                column = column - 1
        return diag_sum
        
    diag_1_1 = sum_diag(0, 1, 1)
    diag_1_2 = sum_diag(1, 0, 1)
    diag_2_1 = sum_diag(0, 4, -1)
    diag_2_2 = sum_diag(1, 5, -1)
    
    if diag_1_1 == 5 or diag_1_2 == 5 or diag_2_1 == 5 or diag_2_2 == 5:
        return 'o'
    if diag_1_1 == -5 or diag_1_2 == -5 or diag_2_1 == -5 or diag_2_2 == -5:
        return 'x'
        
    return None



def get_move(player):
    return input(player + ' player, chose your move: ')


def get_spin(player):
    return input(player + ' player, chose the center of your spin center: ')


def make_move(player, move, board):
    if player == 'o':
        player_sign = 1
    else:
        player_sign = -1

    
    if len(move) != 2:
        return False
    elif str(move[0]) < '1' or str(move[0]) > '6':
        return False
    elif move[1] < 'A' or move[1] > 'F':
        return False

    
    row = int(move[0]) - 1
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == 0:
        board[row][column] = player_sign
        return True
    else:
        return False


def make_spin(player, center, board):
    
    if len(center) != 2:
        return False
    elif str(center[0]) < '2' or str(center[0]) > '5':
        return False
    elif center[1] < 'B' or center[1] > 'E':
        return False
    
    row = int(center[0]) - 1
    column = ord(center[1]) - ord('A')
    
    spinned_square = [[],[],[]]

    for i in range(3):
        for j in range(3):
            spinned_square[i].append(board[row - 1 + i][column - 1 + j])

    
    for i in range(3):
        for j in range(3):
            board[row - 1 + i][column - 1 + j] = spinned_square[2 - j][i]
    
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'



    
