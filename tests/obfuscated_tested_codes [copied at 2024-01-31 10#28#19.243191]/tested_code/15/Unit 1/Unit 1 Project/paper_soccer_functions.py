



import time






def create_board(num_rows, num_columns, board):
    i_r = 0

    while i_r < num_rows:
        board.append([])
        for i in range(num_columns):
            board[i_r].append([])
        i_r += 1

    for i_r in range(num_rows):
        for i_c in range(num_columns):
            for i_rr in range(3):
                board[i_r][i_c].append([])
                for i in range(3):
                    board[i_r][i_c][i_rr].append(' ')  
    return board


def extra_turn(board, ball_pos, num_columns):
    counter = 0

    for i_rr in range(3):
        for i_cc in range(3):
            current_space = board[ball_pos[0]][ball_pos[1]][i_rr][i_cc]
            if current_space != ' ' and current_space != '⊙' and current_space != 'x':
                counter += 1
    if ball_pos[0] == 4 and ball_pos[1] == 2 and counter % 2 == 0:
        return True
    if ball_pos[1] == 0 or ball_pos[1] == num_columns - 1:
        return True
    if counter == 1:
        return False
    elif counter % 2 != 0:
        return True
    else:
        return False


def fun_time(switch, len_time):
    if switch == 1:
        time.sleep(len_time)
        return True
    else:
        time.sleep(0)
        return False




def draw_row(row_number, num_columns, board):
    
    for i_rr in range(3):
        
        if i_rr != 0:
            print('')
        
        
        print('│', end="")
        
        for i_c in range(num_columns):
            
            for i_cc in range(3):
                print(' ' + board[row_number][i_c][i_rr][i_cc], end="")
            print(' │', end="")
    print('')


def draw_row_goal(row_number, board, num_columns):
    
    for i_rr in range(3):
        
        if i_rr != 0:
            print('')
        
        
        print('        ', end="")
        print('│', end="")
        
        for i_c in range(1, num_columns + 1):
            
            for i_cc in range(3):
                print(' ' + board[row_number][i_c][i_rr][i_cc], end="")
            print(' │', end="")
    print('')


def erase_border(board, num_columns, num_rows):
    for i_r in range(num_rows):
        for i_rr in range(0, 3, 2):
            board[i_r][0][i_rr][1] = ' '
    for i_r in range(num_rows):
        for i_rr in range(3):
            board[i_r][0][i_rr][0] = ' '

    for i_r in range(num_rows):
        for i_rr in range(3):
            board[i_r][num_columns - 1][i_rr][2] = ' '
    for i_r in range(num_rows):
        for i_rr in range(0, 3, 2):
            board[i_r][num_columns - 1][i_rr][1] = ' '


def show_border(board, num_columns, ball_pos):
    if (board[ball_pos[0]][ball_pos[1]][1][1] != ' ') and ball_pos[1] == 0:
        board[ball_pos[0]][0][0][1] = '|'
        board[ball_pos[0]][0][2][1] = '|'
        board[ball_pos[0]][0][0][0] = '\\'
        board[ball_pos[0]][0][2][0] = '/'
        board[ball_pos[0]][0][1][0] = '-'

    elif (board[ball_pos[0]][ball_pos[1]][1][1] != ' ') and ball_pos[1] == (num_columns - 1):
        board[ball_pos[0]][num_columns - 1][0][1] = '|'
        board[ball_pos[0]][num_columns - 1][2][1] = '|'
        board[ball_pos[0]][num_columns - 1][0][2] = '/'
        board[ball_pos[0]][num_columns - 1][2][2] = '\\'
        board[ball_pos[0]][num_columns - 1][1][2] = '-'


def draw_board(board, num_rows, num_columns):
    print('            x       x       x            ')
    print('        ┌───────┬───────┬───────┐')
    draw_row_goal(0, board, 3)
    print('┌───────┼───────┼───────┼───────┼───────┐ ')
    
    for i in range(1, num_rows - 1):
        draw_row(i, num_columns, board)
        if i < 7:
            print('├───────┼───────┼───────┼───────┼───────┤ ')
    print('└───────┼───────┼───────┼───────┼───────┘')
    draw_row_goal(8, board, 3)
    print('        └───────┴───────┴───────┘')
    print('            ⊙       ⊙       ⊙            ')




def make_move(direction, ball_pos, board, player):
    
    board[ball_pos[0]][ball_pos[1]][1][1] = ' '

    
    
    
    

    if direction == 'north':
        if not board[ball_pos[0]][ball_pos[1]][0][1] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][1] = '|'
        board[ball_pos[0] - 1][ball_pos[1]][2][1] = '|'
        ball_pos[0] -= 1

    elif direction == 'south':
        if not board[ball_pos[0]][ball_pos[1]][2][1] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][1] = '|'
        board[ball_pos[0] + 1][ball_pos[1]][0][1] = '|'
        ball_pos[0] += 1

    elif direction == 'east':
        if not board[ball_pos[0]][ball_pos[1]][1][2] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][1][2] = '—'
        board[ball_pos[0]][ball_pos[1] + 1][1][0] = '—'
        ball_pos[1] += 1

    elif direction == 'west':
        if not board[ball_pos[0]][ball_pos[1]][1][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][1][0] = '—'
        board[ball_pos[0]][ball_pos[1] - 1][1][2] = '—'
        ball_pos[1] -= 1

    elif direction == 'northeast':
        if not board[ball_pos[0]][ball_pos[1]][0][2] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][2] = '/'
        board[ball_pos[0] - 1][ball_pos[1] + 1][2][0] = '/'
        ball_pos[1] += 1
        ball_pos[0] -= 1

    elif direction == 'northwest':
        if not board[ball_pos[0]][ball_pos[1]][0][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][0] = '\\'
        board[ball_pos[0] - 1][ball_pos[1] - 1][2][2] = '\\'
        ball_pos[1] -= 1
        ball_pos[0] -= 1

    elif direction == 'southwest':
        if not board[ball_pos[0]][ball_pos[1]][0][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][0] = '/'
        board[ball_pos[0] + 1][ball_pos[1] - 1][0][2] = '/'
        ball_pos[1] -= 1
        ball_pos[0] += 1

    elif direction == 'southeast':
        if not (board[ball_pos[0]][ball_pos[1]][2][2] == ' '):
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][2] = '\\'
        board[ball_pos[0] + 1][ball_pos[1] + 1][0][0] = '\\'
        ball_pos[1] += 1
        ball_pos[0] += 1

    
    
    else:
        return 'wrong format'
    
    board[ball_pos[0]][ball_pos[1]][1][1] = player

    return 'legal'


def find_winner(board, num_rows):
    for i in range(1, 4):
        if board[num_rows - 1][i][1][1] == 'x':
            return 'x'

    for i in range(1, 4):
        if board[0][i][1][1] == '⊙':
            return '⊙'
