






def draw_row(row, row_number):
    print(f'{row_number} │', end='')
    for cell in row:
        print(f' {cell} │', end='')
    print()


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┐ ')
    for i in range(5):
        draw_row(board[i], i + 1)  
        if i < 4:
            print('  ├───┼───┼───┼───┼───┤ ')
    print('  └───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E ')



def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

    

def get_move(player):
    while True: 
        move = input(f"Player {player}, enter your move (row and column): ")
        if len(move) == 2 and move[0].isdigit() and move[1].isalpha(): 
            row = int(move[0]) - 1
            col = ord(move[1].lower()) - ord('a')
            if 0 <= row < 5 and 0 <= col < 5:
                return row, col
        print('Invalid input or out of bounds. Please enter in the format "1A", "2B", "3C", etc.')



def make_move(player, move, board):
    
    row, col = move 
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else: 
        print("Space is already occupied. Try again.")
        return False


def is_board_full(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                return False
    return True



def calculate_score(board, board_points, player):
    points = 0

    
    for row in range(5):
        count = 0
        tmp_points = 0 
        for col in range(5):
            if board[row][col] == player:
                tmp_points += board_points[row][col]
                count += 1
            else:
                if count >= 3:
                    points += tmp_points
                
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points
    
    
    for col in range(5):
        count = 0
        tmp_points = 0
        for row in range(5):
            if board[row][col] == player:
                tmp_points += board_points[row][col]
                count += 1
            else:
                if count >= 3:
                    points += tmp_points
                
                count = 0
                tmp_points = 0
                
        if count >= 3:
            points += tmp_points
    
    
    for i in range(2,7):
        count = 0
        tmp_points = 0
        for j in range(5):
            
            if 0 <= i-j < 5:
                if board[j][i-j] == player:
                    tmp_points += board_points[j][i-j]
                    count += 1
                else:
                    if count >= 3:
                        points += tmp_points
                    
                    count = 0
                    tmp_points = 0
            else:
                if count >= 3:
                    points += tmp_points
                    
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points
    
    
    for i in range (-2, 3): 
        count = 0
        tmp_points = 0
        for j in range(5):
            
            if 0 <= i+j <5:
                if board[j][i+j] == player:
                    tmp_points += board_points[j][i+j]
                    count += 1
                else:
                    if count >= 3:
                        points += tmp_points
                    
                    count = 0
                    tmp_points = 0
            else:
                if count >= 3:
                    points += tmp_points
                    
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points

    return points

