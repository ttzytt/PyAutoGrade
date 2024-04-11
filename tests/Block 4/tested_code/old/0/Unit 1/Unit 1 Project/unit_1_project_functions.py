













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



def size_of(piece):
    if piece == 'x' or piece =='o':
        size = 1
        return size
    elif piece =='X' or piece == 'O':
        size = 2
        return size
    else:
        size = 0
        return size


def make_piece(player, size):
    if player == 'x': 
        if size == 2:
            return 'X'
        else:
            return 'x'
    elif player == 'o':
        if size == 2:
            return 'O'
        else:
            return 'o'
    else:
        return ' '
    
        


def find_winner(board):
    
    for row in range(0,len(board)):
        if (board[row][0].lower() == board[row][1].lower()
            and board[row][0].lower() == board[row][2].lower()
            and board[row][0] != ' '):
            return board[row][0].lower()
    
    for column in range(0, len(board)):
        if (board[0][column].lower() == board[1][column].lower() and
            board[0][column].lower() == board[2][column].lower()
            and board[0][column] != ' '):
            return board[0][column].lower()
    
    if (board[0][0] == board[1][1].lower()
        and board[0][0].lower() == board[2][2].lower()
        and board[0][0] != ' '):
        return board[0][0].lower()
    elif (board[0][2].lower() == board[1][1].lower()
          and board[0][2].lower() == board[2][0].lower()
          and board[0][0] != ' ') :
        return board[1][1].lower()
    else:
        return None

    



def get_move(player):
    return input(player + ' player, choose your move: ')




def get_size(player):
    size = input(player + ' player, choose your size (1 or 2): ')
    if size == '1' or size == '2':
        return int(size)
    else:
        
        
        return 27






def make_move(piece, move, board):
    
    if len(move) != 2:
        return False
    if move[0] != '1' and move[0] != '2' and move[0] != '3':
        return False
    if move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
        return False
    if piece != 'X' and piece != 'O' and piece != 'x'  and piece != 'o':
        return False
    
    
       


    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    

    
    

    initial_piece_size = size_of(board[row][column])
    if size_of(piece) > initial_piece_size:
        board[row][column] = piece
        return True
    else:
        return False





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'


