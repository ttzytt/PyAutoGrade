




def draw_board(board):
    
    def draw_row(row, row_number):
        printed_row = str(row_number)
        
        if row_number >= 10:
            printed_row += ' │'
        else:
            printed_row += '  │'

        
        for i in range(19):
            printed_row += row[i]
            printed_row += '   '
        print(printed_row)

    
    for i in range(19):
        print('   │')
        draw_row(board[i], (i+1))

    
    print()
    printed_letters = ' '
    for i in range(19):
        printed_letters += '   '
        printed_letters += chr(i+65)
    print(printed_letters)




def find_outermost_pieces(board):
    topmost_piece_row = None
    leftmost_piece_column = None
    bottommost_piece_row = None
    rightmost_piece_column = None

    
    i = 0
    while topmost_piece_row == None:
        for column in range(19):
            if board[i][column] != '.':
                topmost_piece_row = i
        i += 1
    
    
    i = 0
    while leftmost_piece_column == None:
        for row in range(19):
            if board[row][i] != '.':
                leftmost_piece_column = i
        i += 1

    
    i = 18
    while bottommost_piece_row == None:
        for column in range(19):
            if board[i][column] != '.':
                bottommost_piece_row = i
        i -= 1

    
    i = 18
    while rightmost_piece_column == None:
        for row in range(19):
            if board[row][i] != '.':
                rightmost_piece_column = i
        i -= 1

    return topmost_piece_row, leftmost_piece_column, bottommost_piece_row, \
           rightmost_piece_column



def has_5_in_a_row(testing_sequence):
    
    
    

    streak = 0
    current_streak_player = testing_sequence[0]
    for i in range(len(testing_sequence)):
        if testing_sequence[i] != current_streak_player: 
            current_streak_player = testing_sequence[i]
            streak = 1
        elif testing_sequence[i] == '·': 
            current_streak_player = None
            streak = 1
        else: 
            streak += 1
        if streak >= 5:
            return current_streak_player
    return None

            


def find_winner(board):
    topmost_piece_row, leftmost_piece_column, bottommost_piece_row, \
                       rightmost_piece_column = find_outermost_pieces(board)
    
    for i in range(topmost_piece_row, bottommost_piece_row+1):
        testing_sequence = [] 
        for column in range(leftmost_piece_column, rightmost_piece_column+1):
            testing_sequence.append(board[i][column])
        winner = has_5_in_a_row(testing_sequence)
        if winner != None:
            return winner
    
    for i in range(leftmost_piece_column, rightmost_piece_column+1):
        testing_sequence = [] 
        for row in range(topmost_piece_row, bottommost_piece_row+1):
            testing_sequence.append(board[row][i]) 
        winner = has_5_in_a_row(testing_sequence)
        if winner != None:
            return winner
    
    return None



def find_winner_2(board, move):
    
    
    
    


    move_list = move.split()
    row = int(move_list[0]) - 1
    column = ord(move_list[1]) - ord('A')


    
    testing_sequence = []
    
    starting_index_rows = max(column - 4, 0)
    ending_index_rows = min(column + 4, 18)
    
    for i in range(starting_index_rows, ending_index_rows+1):
        testing_sequence.append(board[row][i])
    winner = has_5_in_a_row(testing_sequence)
    if winner is not None:
        return winner

    
    testing_sequence = []
    
    starting_index_columns = max(row - 4, 0)
    ending_index_columns = min(row + 4, 18)
    
    for i in range(starting_index_columns, ending_index_columns+1):
        testing_sequence.append(board[i][column])
    winner = has_5_in_a_row(testing_sequence)
    if winner is not None:
        return winner


    
    
    
    x = column
    y = row
    i = 0
    
    while y > 0 and x > 0 and i < 4: 
        x -= 1 
        y -= 1
        i += 1
    starting_indices_diagonals = [y, x]
    x = column
    y = row
    i = 0

    
    while y < 18 and x < 18 and i < 4:
        x += 1 
        y += 1
        i += 1
    ending_indices_diagonals = [y, x]

    
    testing_sequence = []
    for i in range(starting_indices_diagonals[0], 
                   ending_indices_diagonals[0] + 1):
        testing_sequence.append(board[i][starting_indices_diagonals[1] +
                                         (i - starting_indices_diagonals[0])])
    winner = has_5_in_a_row(testing_sequence)
    if winner is not None:
        return winner


    
    x = column
    y = row
    i = 0
    while y > 0 and x < 18 and i < 4:
        x += 1
        y -= 1
        i += 1
    starting_indices_diagonals = [y, x]

    x = column
    y = row
    i = 0
    while y < 18 and x > 0 and i < 4:
        x -= 1
        y += 1
        i += 1
    ending_indices_diagonals = [y, x]

    
    testing_sequence = []
    for i in range(starting_indices_diagonals[0], 
                   ending_indices_diagonals[0] + 1):
        testing_sequence.append(board[i][starting_indices_diagonals[1] - 
                                         (i - starting_indices_diagonals[0])])
    winner = has_5_in_a_row(testing_sequence)
    if winner is not None:
        return winner
    return None








def find_first_capture(board, move, player):
    
    
    
    


    move_list = move.split()
    row = int(move_list[0]) - 1
    column = ord(move_list[1]) - ord('A')

    
    direction_x = 0
    direction_y = 0

    if player == '#':
        opponent = 'O'
    else:
        opponent = '#'

    
    
    bounding_indices_y = [max(row - 1, 0), min(row + 1, 18)]
    bounding_indices_x = [max(column - 1, 0), min(column + 1, 18)]

    
    for y in range(bounding_indices_y[0], bounding_indices_y[1] + 1):
        for x in range(bounding_indices_x[0], bounding_indices_x[1] + 1):
            if board[y][x] == opponent: 
                
                direction_y = y - row
                direction_x = x - column

                if (0 <= y + (2 * direction_y) <= 18
                        and 0 <= x + (2 * direction_x) <= 18):
                    
                    if (board[y + direction_y][x + direction_x] == opponent
                    and (board[y + (2 * direction_y)][x + (2 * direction_x)]
                         == player)): 
                                      

                        
                        board[y + direction_y][x + direction_x] = '·'
                        board[y][x] = '·'
                        print('Capture!')










def has_second_capture_pattern(board, y, x):
    
    

    if board[y][x] == '·': 
        return
    elif board[y][x] == 'O':
        opposite_of_top_left = '#'
    else:
        opposite_of_top_left = 'O'

    testing_section = [[], [], [], []] 
    for i in range(y, y+4):
        for j in range(x, x+4):
            testing_section[i-y].append(board[i][j])

    if board[y][x] == board[y+1][x+1]: 
        
        capture_pattern = [[board[y][x], '·', '·', opposite_of_top_left],
                           ['·', board[y][x], '·', '·'],
                           ['·', '·', board[y][x], '·'],
                           [opposite_of_top_left, '·', '·', board[y][x]]]   
        if capture_pattern == testing_section:
            print('Capture!')
            for i in range(4):
                board[y+i][x+i] = '·' 
    else: 
        
        capture_pattern = [[board[y][x], '·', '·', opposite_of_top_left],
                           ['·', '·', opposite_of_top_left, '·'],
                           ['·', opposite_of_top_left, '·', '·'],
                           [opposite_of_top_left, '·', '·', board[y][x]]]
        if capture_pattern == testing_section:
            print('Capture!')
            for i in range(4):
                board[y+3-i][x+i] = '·' 

    




def find_second_capture(board):
    
    
    

    for y in range(16): 
                        
        for x in range(16):
            has_second_capture_pattern(board, y, x)




def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    move_list = move.split()
    
    if (not len(move_list) == 2 
        or not len(move_list[0]) <= 2
        or not len(move_list[1]) == 1
        or not move_list[0].isnumeric() 
        or not 1 <= int(move_list[0]) <= 19
        or not 'A' <= move_list[1] <= 'S'):
        return False
    
    row = int(move_list[0]) - 1
    
    
    
    column = ord(move_list[1]) - ord('A')
    if board[row][column] != '·':
        return False
    
    board[row][column] = player
    return True





def next_player(player):
    if player == '#':
        return 'O'
    else:  
        return '#'
