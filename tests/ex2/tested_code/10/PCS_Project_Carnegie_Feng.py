




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
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[8], 9)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┘')
    print('    A   B   C   D   E   F   G   H   I  ')

def find_winner(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if(i >= 4):
                if(board[i][j] == 'x' and board[i-1][j] == 'x' and board[i-2][j] == 'x' and board[i-3][j] == 'x' and board[i-4][j] == 'x'):
                    return 'x'
            if(i <= 4):
                if(board[i][j] == 'x' and board[i+1][j] == 'x' and board[i+2][j] == 'x' and board[i+3][j] == 'x' and board[i+4][j] == 'x'):
                    return 'x'
            if(j >= 4):
                if(board[i][j] == 'x' and board[i][j-1] == 'x' and board[i][j-2] == 'x' and board[i][j-3] == 'x' and board[i][j-4] == 'x'):
                    return 'x'
            if(j <= 4):
                if(board[i][j] == 'x' and board[i][j+1] == 'x' and board[i][j+2] == 'x' and board[i][j+3] == 'x' and board[i][j+4] == 'x'):
                    return 'x'
            if(i >= 4 and j >= 4):
                if(board[i][j] == 'x' and board[i-1][j-1] == 'x' and board[i-2][j-2] == 'x' and board[i-3][j-3] == 'x' and board[i-4][j-4] == 'x'):
                    return 'x'
            if(i <= 4 and j >= 4):
                if(board[i][j] == 'x' and board[i+1][j-1] == 'x' and board[i+2][j-2] == 'x' and board[i+3][j-3] == 'x' and board[i+4][j-4] == 'x'):
                    return 'x'
            if(i <= 4 and j <= 4):
                if(board[i][j] == 'x' and board[i+1][j+1] == 'x' and board[i+2][j+2] == 'x' and board[i+3][j+3] == 'x' and board[i+4][j+4] == 'x'):
                    return 'x'
            if(i >= 4 and j <= 4):
                if(board[i][j] == 'x' and board[i-1][j+1] == 'x' and board[i-2][j+2] == 'x' and board[i-3][j+3] == 'x' and board[i-4][j+4] == 'x'):
                    return 'x'
                
            if(i >= 4):
                if(board[i][j] == 'o' and board[i-1][j] == 'o' and board[i-2][j] == 'o' and board[i-3][j] == 'o' and board[i-4][j] == 'o'):
                    return 'o'
            if(i <= 4):
                if(board[i][j] == 'o' and board[i+1][j] == 'o' and board[i+2][j] == 'o' and board[i+3][j] == 'o' and board[i+4][j] == 'o'):
                    return 'o'
            if(j >= 4):
                if(board[i][j] == 'o' and board[i][j-1] == 'o' and board[i][j-2] == 'o' and board[i][j-3] == 'o' and board[i][j-4] == 'o'):
                    return 'o'
            if(j <= 4):
                if(board[i][j] == 'o' and board[i][j+1] == 'o' and board[i][j+2] == 'o' and board[i][j+3] == 'o' and board[i][j+4] == 'o'):
                    return 'o'
            if(i >= 4 and j >= 4):
                if(board[i][j] == 'o' and board[i-1][j-1] == 'o' and board[i-2][j-2] == 'o' and board[i-3][j-3] == 'o' and board[i-4][j-4] == 'o'):
                    return 'o'
            if(i <= 4 and j >= 4):
                if(board[i][j] == 'o' and board[i+1][j-1] == 'o' and board[i+2][j-2] == 'o' and board[i+3][j-3] == 'o' and board[i+4][j-4] == 'o'):
                    return 'o'
            if(i <= 4 and j <= 4):
                if(board[i][j] == 'o' and board[i+1][j+1] == 'o' and board[i+2][j+2] == 'o' and board[i+3][j+3] == 'o' and board[i+4][j+4] == 'o'):
                    return 'o'
            if(i >= 4 and j <= 4):
                if(board[i][j] == 'o' and board[i-1][j+1] == 'o' and board[i-2][j+2] == 'o' and board[i-3][j+3] == 'o' and board[i-4][j+4] == 'o'):
                    return 'o'
                
    return 'f'

def get_move(player):
    return input(player + ' player, chose your move: ') 

def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    elif move[0] != '1' and move[0] != '2' and move[0] != '3' and move[0] != '4' and move[0] != '5' and move[0] != '6' and move[0] != '7' and move[0] != '8' and move[0] != '9':
        return False
    elif move[1] != 'A' and move[1] != 'B' and move[1] != 'C' and move[1] != 'D' and move[1] != 'E' and move[1] != 'F' and move[1] != 'G' and move[1] != 'H' and move[1] != 'I':
        return False
    
    
    row = int(move[0]) - 1
    
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == 'x' or board[row][column] == 'o':
        return False
    else:
        board[row][column] = player
        return True

def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'
    
board = [[" " for i in range(9)] for i in range(9)]
player = 'x'
steps = 0

while not (find_winner(board) != 'f' or steps > 81):  
    draw_board(board)

    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    steps += 1
    
if find_winner(board) == 'x':
    print('The x player wins!')
elif find_winner(board) == 'o':
    print('The o player wins!')
else:
    print('This is a tie.')




