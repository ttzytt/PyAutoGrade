







def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')




def draw_board(board):
    print('  ┌───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  └───┴───┴───┴───┘ ')
    print('    A   B   C   D   ')

    








def find_winner_in_list(line):
    if ((line[0] == 'x' or line[0] == '@')
            and (line[1] == 'x' or line[1] == '@')
            and (line[2] == 'x' or line[2] == '@')
            and (line[3] == 'x' or line[3] == '@')):
        return 'x'
    elif ((line[0] == 'o' or line[0] == '@')
            and (line[1] == 'o' or line[1] == '@')
            and (line[2] == 'o' or line[2] == '@')
            and (line[3] == 'o' or line[3] == '@')):
        return 'o'
    else:
        return None











def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if len(move) != 1:
        return False
    elif not ('A' <= move[0] <= 'D'):
        return False

    
    
    
    
    column = ord(move[0]) - ord('A')

    
    

    
    if board[0][column] != ' ':
        return False
    
    
    row = 3
    while not (board[row][column] == ' '):
        row = row - 1
    board[row][column] = player
    return True




def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

