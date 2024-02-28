





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
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  

    return None  



def get_move(player):
    while True:
        move = input(player + ' player, choose your move: ')
        
        if len(move) == 2 and move[0].isdigit() and move[1].isalpha():
            return move
        else:
            print('Invalid move format. Use the format: 1A, 2B, 3C')



def make_move(player, move, board):
    
    if len(move) != 2 or not move[0].isdigit() or not move[1].isalpha():
        print('Invalid move format. Use the format: 1A, 2B, 3C')
        return False

    
    row = int(move[0]) - 1
    
    column = ord(move[1]) - ord('A')

    
    if not (0 <= row < 3 and 0 <= column < 3) or board[row][column] != ' ':
        print('Invalid move. The space is either out of bounds or already occupied.')
        return False

    
    board[row][column] = player
    return True




def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

