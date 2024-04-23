


import random
random.seed()

def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + str(row[0]) + ' │ '
          + str(row[1]) + ' │ '
          + str(row[2]) + ' │ '
          + str(row[3]) + ' │ '
          + str(row[4]) + ' │ ')



def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  └───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   ')

def get_number():
    n = random.randint(1, 9)
    print('Next number is: ' + str(n))
    return n
    
def get_move(player):
    move = input('Player ' + player + ', choose your move or skip: ')
    return move


def make_move(n, move, board):

    
    if len(move) != 2:
        return False
    if move[0] not in ['1', '2', '3', '4', '5'] or \
       move[1] not in ['A', 'B', 'C', 'D', 'E']:
        return False

    
    row = int(move[0]) - 1
    column = ord(move[1]) - ord('A')

    if board[row][column] != ' ':
        return False
    else:
        board[row][column] = n
        return True


def find_winner(board):

    
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
                break
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
                break
        if consecutive_row:
            return True

    
    for i in range(len(board)):
        consecutive_column = True
        for j in range(len(board) - 1):
            if board[j][i] == ' ' or board[j + 1][i] == ' ':
                consecutive_column = False
                break
            elif abs(int(board[j][i]) - int(board[j + 1][i])) != 1:
                consecutive_column = False
                break
    if consecutive_column:
        return True

    
    for i in range(len(board) - 1):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
            break
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
            break
    if consecutive_diagonal_1:
        return True

    
    for i in range(len(board) - 1):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][4 - (i + 1)] == ' ':
            consecutive_diagonal_2 = False
            break
        elif abs(int(board[i][4 - i]) - int(board[i + 1][4 - (i + 1)])) != 1:
            consecutive_diagonal_2 = False
            break
    if consecutive_diagonal_2:
        return True

    return False



def next_player(player):
    if player == '1':
        return '2'
    else:
        return '1'


board = [ ['1', '1', '1', '3', '5'],
          [' ', ' ', '2', '4', '6'],
          ['3', '4', '3', '3', '5'],
          [' ', '2', '4', ' ', '8'],
          ['1', ' ', '5', ' ', '9'] ]

print(find_winner(board))

