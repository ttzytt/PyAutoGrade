






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
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None





def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    if len(move) != 2:
        return False

    if move[0] not in '123' or move[1] not in 'ABC':
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


def is_board_full(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False  
    return True
