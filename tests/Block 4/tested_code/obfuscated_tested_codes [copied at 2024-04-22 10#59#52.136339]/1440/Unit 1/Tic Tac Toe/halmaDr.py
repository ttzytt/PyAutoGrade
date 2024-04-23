



board = [['x','x','x',' ',' ',' '],['x','x',' ',' ',' ',' '],['x',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ','o'],[' ',' ',' ',' ','o','o'],[' ',' ',' ','o','o','o']]


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
    print('  └───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F ')




def find_winner_x(board):
    for i in range(3):
        for j in range(3-i):
            if board[i][j] != 'x':
                return False
                break
    return True

def find_winner_o(board):
    for i in range(3):
        for j in range(3-i):
            if board[i][j] != 'o':
                return False
                break
    return True
                




def get_piece(player):
    piece = input(player + ' player, choose the piece you want to move: ')
    work_list = []
    return piece

def get_move(player):
    move = input(player + ' player, choose the place u wannt to move to: ')
    return move

def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'


def convert_coord(a,b): 
    row_coord = str(a+1)
    column_coord = chr(b+65)
    board_coord = row_coord + column_coord
    return board_coord
    

def jump_move(piece, board, work_list):
    
    piece_row = ord(piece[0]) - ord('1')
    piece_column = ord(piece[1]) - ord('A')
    
    if piece_row > 1 and piece_column > 1:
        
        if board[piece_row - 1][piece_column - 1] != " " and board[piece_row - 2][piece_column - 2] == ' ':
            if convert_coord(piece_row - 2, piece_column - 2) not in work_list:
                work_list.append(convert_coord(piece_row - 2, piece_column - 2))
                jump_move(convert_coord(piece_row - 2, piece_column - 2), board, work_list)
    if piece_row > 1:
        
        if board[piece_row - 1][piece_column] != " " and board[piece_row - 2][piece_column] == ' ':
            if convert_coord(piece_row - 2, piece_column) not in work_list:
                work_list.append(convert_coord(piece_row - 2, piece_column))
                jump_move(convert_coord(piece_row - 2, piece_column), board, work_list)
    if piece_row > 1 and piece_column < 4: 
        
        if board[piece_row - 1][piece_column + 1] != " " and board[piece_row - 2][piece_column + 2] == ' ':
            if convert_coord(piece_row - 2,piece_column + 2) not in work_list:
                work_list.append(convert_coord(piece_row - 2,piece_column + 2))
                jump_move(convert_coord(piece_row - 2,piece_column + 2), board, work_list)
    if piece_column > 1: 
        
        if board[piece_row][piece_column - 1] != " " and board[piece_row][piece_column - 2] == ' ':
            if convert_coord(piece_row,piece_column - 2) not in work_list:
                work_list.append(convert_coord(piece_row,piece_column - 2))
                jump_move(convert_coord(piece_row,piece_column - 2), board, work_list)
    if piece_column < 4:
        
        if board[piece_row][piece_column + 1] != " " and board[piece_row][piece_column + 2] == ' ':
            if convert_coord(piece_row,piece_column + 2) not in work_list:
                work_list.append(convert_coord(piece_row,piece_column + 2))
                jump_move(convert_coord(piece_row,piece_column + 2), board, work_list)
    if piece_row < 4 and piece_column > 1:
        
        if board[piece_row + 1][piece_column - 1] != " " and board[piece_row + 2][piece_column - 2] == ' ':
            if convert_coord(piece_row + 2,piece_column - 2) not in work_list:
                work_list.append(convert_coord(piece_row + 2,piece_column - 2))
                jump_move(convert_coord(piece_row + 2,piece_column - 2),board, work_list)
    if piece_row < 4:
        
        if board[piece_row + 1][piece_column] != " " and board[piece_row + 2][piece_column] == ' ':
            if convert_coord(piece_row + 2,piece_column) not in work_list:
                work_list.append(convert_coord(piece_row + 2,piece_column))
                jump_move(convert_coord(piece_row + 2,piece_column), board, work_list)
    if piece_row < 4 and piece_column < 4:
        
        if board[piece_row + 1][piece_column + 1] != " " and board[piece_row + 2][piece_column + 2] == ' ':
            if convert_coord(piece_row + 2,piece_column + 2) not in work_list:
                work_list.append(convert_coord(piece_row + 2,piece_column + 2))
                jump_move(convert_coord(piece_row + 2,piece_column + 2), board, work_list)

    return work_list



def walk_move(player, piece, move):
        move_row = ord(move[0]) - ord('1')
        move_column = ord(move[1]) - ord('A')
        piece_row = ord(piece[0]) - ord('1')
        piece_column = ord(piece[1]) - ord('A')
        x1 = piece_row
        x2 = piece_column
        y1 = move_row
        y2 = move_column
        return (
            0 <= x1 < 6
            and 0 <= y1 < 6
            and 0 <= x2 < 6
            and 0 <= y2 < 6
            and board[move_row][move_column] == ' '
            and (abs(x2 - x1) == 1 or abs(y2 - y1) == 1)
        )


def make_move(player, piece, move, board):

    
    move_row = ord(move[0]) - ord('1')
    move_column = ord(move[1]) - ord('A')
    piece_row = ord(piece[0]) - ord('1')
    piece_column = ord(piece[1]) - ord('A')
    
    if piece == " ":
        return False
    elif len(piece) != 2:
        return False
    elif board[piece_row][piece_column] != player:
        return False
    
    elif len(move) != 2:
        return False
    elif move[0] not in ['1', '2', '3','4','5','6'] or move[1] not in ['A', 'B', 'C','D','E','F']:
        return False
    
    
    work_list = jump_move(piece, board, [])
    print(work_list)
    walk_move(player, piece, move)
    if walk_move(player, piece, move) != True and move not in work_list:
        print("Your move is invalid")
        return False

        
    
    board[move_row][move_column] = player
    board[piece_row][piece_column] = ' '

    return True



