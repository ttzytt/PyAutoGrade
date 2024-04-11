





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
    
    winner_board = [ [ 0, 0, 0],
                     [ 0, 0, 0],
                     [ 0, 0, 0] ]

    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'o':
                winner_board[i][j] = 1
            if board[i][j] == 'x':
                winner_board[i][j] = -1

    
    for test_row in range(3):
        if sum(winner_board[test_row]) == 3:
            return 'o'
        if sum(winner_board[test_row]) == -3:
            return 'x'

    
    column_value = [[],[],[]]
    for i in range(3):
        for j in range(3):
            column_value[i].append(winner_board[j][i])

    for test_column in range(3):
        if sum(column_value[test_column]) == 3:
             return 'o'
        if sum(column_value[test_column]) == -3:
            return 'x'

    
    diag_1 = winner_board[0][0] + winner_board[1][1]+ winner_board[2][2]
    diag_2 = winner_board[2][0] + winner_board[1][1]+ winner_board[0][2]

    if diag_1 == 3 or diag_2 == 3:
        return 'o'
    if diag_1 == -3 or diag_2 == -3:
        return 'x'
        
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    elif str(move[0]) != '1' and str(move[0]) != '2' and str(move[0]) != '3':
        return False
    elif move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
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

