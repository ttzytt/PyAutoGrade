def draw_row(row, row_number):
    def get_symbol(cell):
        if cell == 'x':
            return '✕'  
        elif cell == 'o':
            return '◯'  
        else:
            return cell  

    print(str(row_number) + ' │ '
          + get_symbol(row[0]) + ' │ '
          + get_symbol(row[1]) + ' │ '
          + get_symbol(row[2]) + ' │ '
          + get_symbol(row[3]) + ' │ '
          + get_symbol(row[4]) + ' │ ')

def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┐')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┤')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┤')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┤')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┤')
    draw_row(board[4], 5)
    print('  └───┴───┴───┴───┴───┘')
    print('    A   B   C   D   E   ')

def find_winner(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] in ['x', 'o']:
                player = board[i][j]
                if j <= 1 and all(board[i][j+k] == player for k in range(4)):
                    return player
                if i <= 1 and all(board[i+k][j] == player for k in range(4)):
                    return player
                if i <= 1 and j <= 1 and all(board[i+k][j+k] == player for k in range(4)):
                    return player
                if i <= 1 and j >= 3 and all(board[i+k][j-k] == player for k in range(4)):
                    return player
    return None

def make_move(player, move, board):
    if len(move) != 2 or move[0] not in '12345' or move[1] not in 'ABCDE':
        return False
    row, col = int(move[0]) - 1, ord(move[1]) - ord('A')
    if board[row][col] != ' ':
        return False
    board[row][col] = player
    return True


board = [[' ' for _ in range(5)] for _ in range(5)]
blocked_cells = ['5B', '5D', '3A', '3E', '1C']
for cell in blocked_cells:
    r, c = int(cell[0]), ord(cell[1]) - ord('A')
    board[r-1][c] = 'X'

player = 'x'
steps = 0

while not (find_winner(board) or steps >= 24):
    draw_board(board)
    next_move = input(player + " player, choose your move: ")
    success = make_move(player, next_move, board)

    while not success:
        print('That is not a valid move.')
        next_move = input(player + " player, choose your move: ")
        success = make_move(player, next_move, board)

    if find_winner(board):
        break

    player = 'o' if player == 'x' else 'x'
    steps += 1

draw_board(board)
winner = find_winner(board)
if winner:
    print(f"The {winner} player wins!")
else:
    print("This is a tie.")
