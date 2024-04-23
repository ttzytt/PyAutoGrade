





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
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┘')
    print('    A   B   C   D   E   F   G   H   I  ')

def check_winner(board):



    for rows in range(7):
        for columns in range(7):
            if board[rows][columns] != '#':
                if board[rows][columns] != ' ':
                    if board[rows][columns] == board[rows + 1][columns + 1] == board[rows + 2][columns + 2] == board[rows + 3][columns + 3]:
                        if board[rows][columns] == 'x':
                            return 'x'
                        else:
                            return 'o'

    for rows in range(7):
        for columns in range(7, 2, -1):
            if board[rows][columns] != '#':
                if board[rows][columns] != ' ':
                    if board[rows][columns] == board[rows + 1][columns - 1] == board[rows + 2][columns - 2] == board[rows + 3][columns - 3]:
                        if board[rows][columns] == 'x':
                            return 'x'
                        else:
                            return 'o'

def make_move(player, player_input, board):
    
    if len(player_input) < 2:
        return False
    if not (ord(player_input[0]) >= 49 and ord(player_input[0]) <= 57
        and ord(player_input[1]) >= 65 and ord(player_input[1]) <= 73):
        return False

    move = player_input
    row = int(move[0]) - 1
    column = ord(move[1]) - ord('A')    
    if board[row][column] == ' ':
        board[row][column] = player
        return True
        
    elif board[row][column] == '#':
        return False
    elif board[row][column] == 'x' or board[row][column] == 'o':
        return False
    else:
        return False


