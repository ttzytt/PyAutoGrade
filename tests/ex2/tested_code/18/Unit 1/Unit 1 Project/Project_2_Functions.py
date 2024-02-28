





def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ ')



def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  └───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   ')





def four_in_row(line): 
    streak = 0 
    piece = line[0]
    for i in range(len(line)):
        
        if line[i] == ' ': 
            piece = ' '
            streak = 1
            
        elif piece == line[i]: 
            streak = streak + 1
            
        else: 
            piece = line[i]
            streak = 1
            
        if streak >= 4 and line[i] != ' ': 
            return piece
    

    return None






def find_winner(board):
    
    for x in range(3):
        for y in range(4):
            diagonal_1 = [] 
            for i in range(4):
                diagonal_1.append(board[y+i][x+i])
            if four_in_row(diagonal_1) is not None: 
                return four_in_row(diagonal_1)

    for x in range(5, 2, -1):
        for y in range(4):
            diagonal_2 = [] 
            for i in range(4):
                diagonal_2.append(board[y+i][x-i])
            if four_in_row(diagonal_2) is not None: 
                return four_in_row(diagonal_2)
            
    
    for row in range(len(board)):
        if four_in_row(board[row]) is not None:
            return four_in_row(board[row])
        
    
    for column in range(len(board[0])):
        
        column_as_list = [] 
        for row in range(len(board)):
            column_as_list.append(board[row][column])
            if four_in_row(column_as_list) is not None: 
                return four_in_row(column_as_list)




def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    if not ('1' <= move[0] <= '7' and 'A' <= move[1] <= 'F'):
        return False
        
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == 'x' or board[row][column] == 'o':
        return False
  
    board[row][column] = player
    return True






def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

