


"""
In this program, I acknowledge inspiration from Mark Zhao. I learned from him to convert the 'x' and 'o'
into 1 and -1. As the result, I can check the absolute value of the sum of the numbers
in a whole line to find out whether there is a winner.
"""

def draw_row(row, row_number, layer_index):
    print(' '*4*layer_index, end = '')
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')



def draw_single_board(board, layer_index, layer):
    print(' '*4*layer_index, end = '') 
    print('  ┌───┬───┬───┬───┐ ')
    draw_row(board[0], 1, layer_index)
    print(' '*4*layer_index, end = '')
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[1], 2, layer_index)
    print(' '*4*layer_index, end = '')
    print('  ├───┼───┼───┼───┤ ' + 'layer ' + layer) 
    draw_row(board[2], 3, layer_index)
    print(' '*4*layer_index, end = '')
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[3], 4, layer_index)
    print(' '*4*layer_index, end = '')
    print('  └───┴───┴───┴───┘ ')
    print(' '*4*layer_index, end = '')
    print('    1   2   3   4   ')
    print()


def draw_board(board):
    draw_single_board(board[0], 0, 'A')
    draw_single_board(board[1], 1, 'B')
    draw_single_board(board[2], 2, 'C')
    draw_single_board(board[3], 3, 'D')






def find_winner_all(boards):
    
    check_winner_board_1 = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    check_winner_board_2 = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    check_winner_board_3 = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    check_winner_board_4 = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    
    check_winner_boards = [check_winner_board_1, check_winner_board_2, check_winner_board_3, check_winner_board_4]

    
    
    for m in range(4):
        for i in range(4):
            for j in range(4):
                if boards[m][i][j] == 'x':
                    check_winner_boards[m][i][j] = 1
                elif boards[m][i][j] == 'o':
                    check_winner_boards[m][i][j] = -1
                elif boards[m][i][j] == 'b':
                    check_winner_boards[m][i][j] = 0

    
    
    for m in range(4):
        for i in range(4):
            

            
            
            if abs(check_winner_boards[m][i][0] + check_winner_boards[m][i][1] + check_winner_boards[m][i][2]
                    + check_winner_boards[m][i][3]) == 4:
                return True
            if abs(check_winner_boards[m][0][i] + check_winner_boards[m][1][i] + check_winner_boards[m][2][i]
                    + check_winner_boards[m][3][i]) == 4:
                return True
            if abs(check_winner_boards[0][m][i] + check_winner_boards[1][m][i] + check_winner_boards[2][m][i]
                    + check_winner_boards[3][m][i]) == 4:
                return True

        
        
        if abs(check_winner_boards[0][0][m] + check_winner_boards[1][1][m]
               + check_winner_boards[2][2][m] + check_winner_boards[3][3][m]) == 4:
            return True
        if abs(check_winner_boards[0][3][m] + check_winner_boards[1][2][m]
               + check_winner_boards[2][1][m] + check_winner_boards[3][0][m]) == 4:
            return True

        if abs(check_winner_boards[0][m][0] + check_winner_boards[1][m][1]
               + check_winner_boards[2][m][2] + check_winner_boards[3][m][3]) == 4:
            return True
        if abs(check_winner_boards[0][m][3] + check_winner_boards[1][m][2]
               + check_winner_boards[2][m][1] + check_winner_boards[3][m][0]) == 4:
            return True

        if abs(check_winner_boards[m][0][0] + check_winner_boards[m][1][1]
               + check_winner_boards[m][2][2] + check_winner_boards[m][3][3]) == 4:
            return True
        if abs(check_winner_boards[m][0][3] + check_winner_boards[m][1][2]
               + check_winner_boards[m][2][1] + check_winner_boards[m][3][0]) == 4:
            return True


    
    if abs(check_winner_boards[0][0][0] + check_winner_boards[1][1][1]
               + check_winner_boards[2][2][2] + check_winner_boards[3][3][3]) == 4:
            return True
    if abs(check_winner_boards[0][0][3] + check_winner_boards[1][1][2]
               + check_winner_boards[2][2][1] + check_winner_boards[3][3][0]) == 4:
            return True
    if abs(check_winner_boards[3][0][0] + check_winner_boards[2][1][1]
               + check_winner_boards[1][2][2] + check_winner_boards[0][3][3]) == 4:
            return True
    if abs(check_winner_boards[3][0][3] + check_winner_boards[2][1][2]
               + check_winner_boards[1][2][1] + check_winner_boards[0][3][0]) == 4:
            return True
        
    return None 




def get_move(player):
    return input(player + ' player, choose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        a capital letter A, B, C or D is followed by two string numbers 1, 2, 3 or 4
                A, B, C, D tells to make move on which 'layer' of the board set, and the numbers tells
                where to exactly make the move
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is already occupied,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, boards):
    if len(move) != 3:
        return False
    
    
    
    if (not (ord('A') <= ord(move[0]) <= ord('D')) or not (1 <= int(move[1]) <= 4) or not (1 <= int(move[2]) <= 4)):
        return False

    which_board = ord(move[0]) - ord('A')
    
    row = int(move[1]) - 1
    
    
    
    column = int(move[2]) - 1

    
    if boards[which_board][row][column] == ' ':
        boards[which_board][row][column] = player
        return True
    return False





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'


"""
  ┌───┬───┬───┬───┐ 
1 │   │   │   │   │ 
  ├───┼───┼───┼───┤ 
2 │   │   │   │   │ 
  ├───┼───┼───┼───┤ layer A
3 │ x │   │   │   │ 
  ├───┼───┼───┼───┤ 
4 │   │   │   │   │ 
  └───┴───┴───┴───┘ 
    1   2   3   4   

      ┌───┬───┬───┬───┐ 
    1 │   │   │   │   │ 
      ├───┼───┼───┼───┤ 
    2 │   │   │   │   │ 
      ├───┼───┼───┼───┤ layer B
    3 │   │ x │ o │   │ 
      ├───┼───┼───┼───┤ 
    4 │   │   │   │   │ 
      └───┴───┴───┴───┘ 
        1   2   3   4   

          ┌───┬───┬───┬───┐ 
        1 │   │   │   │   │ 
          ├───┼───┼───┼───┤ 
        2 │   │   │   │   │ 
          ├───┼───┼───┼───┤ layer C
        3 │   │   │ x │   │ 
          ├───┼───┼───┼───┤ 
        4 │   │   │   │ o │ 
          └───┴───┴───┴───┘ 
            1   2   3   4   

              ┌───┬───┬───┬───┐ 
            1 │ o │   │   │   │ 
              ├───┼───┼───┼───┤ 
            2 │   │   │   │   │ 
              ├───┼───┼───┼───┤ layer D
            3 │   │   │   │ x │ 
              ├───┼───┼───┼───┤ 
            4 │   │   │   │   │ 
              └───┴───┴───┴───┘ 
                1   2   3   4
This occasion will cause the x player to win.

  ┌───┬───┬───┬───┐ 
1 │ x │ o │   │   │ 
  ├───┼───┼───┼───┤ 
2 │   │   │   │   │ 
  ├───┼───┼───┼───┤ layer A
3 │   │   │   │   │ 
  ├───┼───┼───┼───┤ 
4 │   │   │   │   │ 
  └───┴───┴───┴───┘ 
    1   2   3   4   

      ┌───┬───┬───┬───┐ 
    1 │   │   │   │   │ 
      ├───┼───┼───┼───┤ 
    2 │ o │ x │   │   │ 
      ├───┼───┼───┼───┤ layer B
    3 │   │   │   │   │ 
      ├───┼───┼───┼───┤ 
    4 │   │   │   │   │ 
      └───┴───┴───┴───┘ 
        1   2   3   4   

          ┌───┬───┬───┬───┐ 
        1 │   │   │   │   │ 
          ├───┼───┼───┼───┤ 
        2 │   │   │   │   │ 
          ├───┼───┼───┼───┤ layer C
        3 │ o │   │ x │   │ 
          ├───┼───┼───┼───┤ 
        4 │   │   │   │   │ 
          └───┴───┴───┴───┘ 
            1   2   3   4   

              ┌───┬───┬───┬───┐ 
            1 │   │   │   │   │ 
              ├───┼───┼───┼───┤ 
            2 │   │   │   │   │ 
              ├───┼───┼───┼───┤ layer D
            3 │   │   │   │   │ 
              ├───┼───┼───┼───┤ 
            4 │   │   │   │ x │ 
              └───┴───┴───┴───┘ 
                1   2   3   4   

This occasion will also cause the x player to win.
"""
