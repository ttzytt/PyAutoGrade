

"""
I did not receive help or look up
information other than from the teacher
and the course materials.
"""

"""
The following functions are for use in a connect four remove game.

In this version of connect four, players can also remove one of their chips on
the bottom of the board, which causes any other pieces in that row to fall down
one spot. The first player to have 4 in a a line wins.
They can be in a row, column or diagonal.

The board will be printed in the form

Numbers which are stored in program
    ┌───┬───┬───┬───┬───┬───┐ 
4   │   │   │   │   │   |   |
    ├───┼───┼───┼───┼───┼───┤
3   │   │   │   │   │   |   |
    ├───┼───┼───┼───┼───┼───┤
2   │   │   │   │   │   |   |
    ├───┼───┼───┼───┼───┼───┤ 
1   │   │   │   │   │   |   |
    ├───┼───┼───┼───┼───┼───┤ 
0   │   │   │   │   │   |   |
    └───┴───┴───┴───┴───┴───┘
      1   2   3   4   5   6  What is printed
      0   1   2   3   4   5  What is stored in program

"""

def draw_row(row):
    print('  │ ' + row[0] + ' │ '
          + row[1] + ' │ ' 
          + row[2] + ' │ ' 
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┐')
    draw_row(board[4])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[3])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[2])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[1])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[0])
    print('  └───┴───┴───┴───┴───┴───┘')
    print('    1   2   3   4   5   6  ')

"""
Checks the board for a winner after each turn and returns which player
it is if there is one

Inputs:
    player      must be either 'x' or 'o'
    
    board       see top of file
Output:
    If there is a winner, it returns True and returns False if there isn't one
"""
def check_winner(board, player):
    
    for col in range(3):
        
         for row in range(5):
             
             
             if (board[row][col] == player
                     and board[row][col + 1] == player
                     and board[row][col + 2] == player
                     and board[row][col + 3] == player):
                 
                  return True

    
    for col in range(6):
        
         for row in range(2):
             
             if (board[row][col] == player
            
                     and board[row + 1][col] == player
                     and board[row + 2][col] == player
                     and board[row + 3][col] == player):
                 
                 return True

    
    for row in range(2):
        
        for col in range(3):
            
            if (board[row][col] == player
            
                    and board[row + 1][col + 1] == player 
                    and board[row + 2][col + 2] == player 
                    and board[row + 3][col + 3] == player):
                
                return True

    
    for row in range(2):
        
        for col in range(3, 6):
            
            if (board[row][col] == player
                
                    and board[row + 1][col - 1] == player 
                    and board[row + 2][col - 2] == player
                    and board[row + 3][col - 3] == player):
                
                return True

    return False


def find_winner(board):
    if check_winner(board, 'x'): 
        return 'Player X wins!'
    elif check_winner(board, 'o'): 
        return 'Player O wins!'
     
   


def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, a number of a column 1 - 6
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the column is full,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    if len(move) > 2: 
        return False
    
    elif len(move) == 2: 
        if move[0] != 'R':
            return False
        
    elif move < '1' or move > '6': 
        return False
            
    elif not (player == 'x' or player == 'o'): 
        return False
        
    
    
    column = int(move) - 1 
    
    for row in range(0, 5): 
        if row == 5:
            if board[row][column] != ' ': 
                return False
        else:
            if board[row][column] == ' ':
               board[row][column] = player 
                                           
               return True
                
                

"""
Modify board by making removing the chip at the bottom of the row the player
selected if it is the same players' chip, and moves any other chips in that row
down one spot

Inputs:
    player      must be either 'x' or 'o'
    move        must be an R, followed by a number of the column, 1 - 6
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is occupied by the other
    player or by no one,
    then the board will not be modified and the function returns False.
"""
def remove_chip(player, move, board):
    if move[1] < '1' or move[1] > '6': 
        return False
    
    column = int(move[1]) - 1 
    
    if board[0][column] != player: 
        return False

        
    for row in range(5 - 1):  
                              
        board[row][column] = board[row + 1][column]

    board[4][column] = ' '
    return True

            
    
                
                    
            



def next_player(player):
    if player == 'x': 
        return 'o'
    
    else:  
        return 'x'
 


