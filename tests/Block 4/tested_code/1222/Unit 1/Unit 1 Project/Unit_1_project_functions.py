





"""
The following functions are for use in making a Gobblet Gobblers game.

For all of the code below, a board 5 by 5 is a list of lists of the
form
        [[' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]
(Each entry is an 'x', 'X' or 'o', 'O' or ' '.)

The corners of the board will not be printed and will be off limits. This is done with a
line of code/formula. 

For the user, a board will be printed in the form

              ┌───┐
    1         │   │
          ┌───┼───┼───┐ 
    2     │   │   │   │ 
      ┌───┼───┼───┼───┼───┐
    3 │   │   │   │   │   │
      └───┼───┼───┼───┼───┘
    4     │   │   │   │ 
          └───┼───┼───┘
    5         │   │ 
              └───┘
        A   B   C   D   E
        

Moves/spaces are referred to by strings such as '1C x' or '2C O'.

Functions will check if move is valid, limited number of large/small pieces for each player.
Each player will get:
- 4 Large pieces

If players run out of large pieces, the move will be counted as invalid and they will have to
enter a move with a small version of their piece.

You can either win by getting a 3 in a row diagonally or getting a 5 in a row horizontally/
vertically.

Players tie if board is filled up but there are no winners. 

"""

def draw_row(row, row_number):
    
    if row_number == 3:
        print(str(row_number)
            + ' │ ' + row[0]
            + ' │ ' + row[1]
            + ' │ ' + row[2]
            + ' │ ' + row[3]
            + ' │ ' + row[4]
            + ' │ ')


    elif row_number == 4:
        print(str(row_number)
            + '    '
            + ' │ ' + row[1]
            + ' │ ' + row[2]
            + ' │ ' + row[3]
            + ' │ ')
              
    elif row_number == 2:
        print(str(row_number)
            + '    '
            + ' │ ' + row[1]
            + ' │ ' + row[2]
            + ' │ ' + row[3]
            + ' │ ')
    elif row_number == 1:
        print(str(row_number)
            + '        '
            + ' │ ' + row[2]
            + ' │ ')

    elif row_number == 5:
        print(str(row_number)
            + '        '
            + ' │ ' + row[2]
            + ' │ ')



def draw_board(board):
    print('          ┌───┐ ')
    draw_row(board[0], 1)
    print('      ┌───┼───┼───┐ ')
    draw_row(board[1], 2)
    print('  ┌───┼───┼───┼───┼───┐ ')
    draw_row(board[2], 3)
    print('  └───┼───┼───┼───┼───┘ ')
    draw_row(board[3], 4)
    print('      └───┼───┼───┘ ')
    draw_row(board[4], 5)
    print('          └───┘ ')
    print('    A   B   C   D   E  ')

def find_winner(board):
    
    if (board[2][0].lower() == board[2][1].lower()
            and board[2][0].lower() == board[2][2].lower()
            and board[2][0].lower() == board[2][3].lower()
            and board[2][0].lower() == board[2][4].lower()
            and board[2][0] != ' '):
        if board[2][0].lower() == 'x':
            return 'x'
        else:
            return 'o'

    
    if (board[0][2].lower() == board[1][2].lower()
            and board[0][2].lower() == board[2][2].lower()
            and board[0][2].lower() == board[3][2].lower()
            and board[0][2].lower() == board[4][2].lower()
            and board[0][2] != ' '):
        if board[0][2].lower() == 'x':
            return 'x'
        else:
            return 'o'
        
    
    if (board[2][0].lower() == board[3][1].lower()
            and board[2][0].lower() == board[4][2].lower()
            and board[2][0] != ' '):
        if board[2][0].lower() == 'x':
            return 'x'
        else:
            return 'o'

    if (board[2][0].lower() == board[1][1].lower()
            and board[2][0].lower() == board[0][2].lower()
            and board[2][0] != ' '):
        if board[2][0].lower() == 'x':
            return 'x'
        else:
            return 'o'

    if (board[2][4].lower() == board[3][3].lower()
            and board[2][4].lower() == board[4][2].lower()
            and board[2][4] != ' '):
        if board[2][4].lower() == 'x':
            return 'x'
        else:
            return 'o'
    

    if (board[2][4].lower() == board[1][3].lower()
              and board[2][4].lower() == board[0][2].lower()
              and board[2][4].lower() != ' '):
        if board[2][4].lower() == 'x':
            return 'x'      
        else:
            return 'o'
        
    if (board[3][1].lower() == board[2][2].lower()
            and board[3][1].lower() == board[1][3].lower()
            and board[3][1] != ' '):
        if board[3][1].lower() == 'x':
            return 'x'
        else:
            return 'o'
    

    if (board[3][3].lower() == board[2][2].lower()
              and board[3][3].lower() == board[1][1].lower()
              and board[3][3].lower() != ' '):
        if board[3][3].lower() == 'x':
            return 'x'      
        else:
            return 'o'

    
    else:
        return None

def find_move(player):
    return input(player + ' player, chose your move: ')

def make_move(player, move, board):

    
    
    
    if len(move) != 4:
        return False

    if (move[0] != '1' and move[0] != '2'
            and move[0] != '3' and move[0] != '4'
            and move[0] != '5'):
        return False

    if (move[1] != 'A' and move[1] != 'B'
            and move[1] != 'C' and move[1] != 'D'
            and move[1] != 'E'):
        return False
    
    if move[3] != 'X' and move[3] != 'x' and move[3] != 'o' and move[3] != 'O':
        return False

    if player == 'x':
        if move[3].lower() == 'o':
            return False

    elif player == 'o':
        if move[3].lower() == 'x':
            return False

    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if abs(int(column) - 2) + abs(int(row) - 2) >= 3:
        return False
    
    
    elif board[row][column] == ' ':
        board[row][column] = move[3]
        return True

    
    
    elif board[row][column] == 'x':
        if move[3] == 'O':
            board[row][column] = 'O'
            return True
        else:
            return False
        
    elif board[row][column] == 'o':
        if move[3] == 'X':
            board[row][column] = 'X'
            return True
        else:
            return False

    elif board[row][column] == 'O':
        return False
    
    elif board[row][column] == 'X':
        return False


def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'


