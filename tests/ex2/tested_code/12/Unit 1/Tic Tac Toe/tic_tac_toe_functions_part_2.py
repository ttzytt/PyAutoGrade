










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
          + row[8] + ' │ '
          + row[9] + ' │ ')
    


def draw_board(board):

    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8], 9)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[9], 0)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')






def find_winner(board):
    for ver in range(10):

        for hor in range(6):

            if board[ver][hor] == board[ver][hor+1] == board[ver][hor+2] == board[ver][hor+3] == board[ver][hor+4]:
                if board[ver][hor] == 'x':
                    return 'x'
                elif board[ver][hor] == 'o':
                    return 'o'

    for hor in range(10):

        for ver in range(6):

            if board[ver][hor] == board[ver+1][hor] == board[ver+2][hor] == board[ver+3][hor] == board[ver+4][hor]:
                if board[ver][hor] == 'x':
                    return 'x'
                elif board[ver][hor] == 'o':
                    return 'o'

    for ver in range(6):

        for hor in range(6):

            if board[ver][hor] == board[ver+1][hor+1] == board[ver+2][hor+2] == board[ver+3][hor+3] == board[ver+4][hor+4]:

                if board[ver][hor] == 'x':
                    return 'x'
                elif board[ver][hor] == 'o':
                    return 'o'

            
    for ver in range(6):

        for hor in range(9,3,-1):

            if board[ver][hor] == board[ver+1][hor-1] == board[ver+2][hor-2] == board[ver+3][hor-3] == board[ver+4][hor-4]:

                if board[ver][hor] == 'x':
                    return 'x'
                elif board[ver][hor] == 'o':
                    return 'o'

    return None






def get_move(player):
    return input(player + ' player, chose your move: ')






def make_move(player,move,board):

    if ((move[0] == '1' or move[0] == '2' or move[0] == '3' or move[0] == '4' or move[0] == '5'
            or move[0] == '6' or move[0] == '7' or move[0] == '8' or move[0] == '9' or move[0] == '0')
        and (move[1] == 'A' or move[1] == 'B' or move[1] == 'C' or move[1] == 'D' or move[1] == 'E'
            or move[1] == 'F' or move[1] == 'G' or move[1] == 'H' or move[1] == 'I' or move[1] == 'J')):
        

        if (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
            or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '):
            

            board[int(move[0])-1][ord(move[1])-ord('A')] = player
            
            return True
        
    return False





def make_automove(player,automove,board):

    if (board[int(automove[0])-1][ord(automove[1])-ord('A')] == ''
        or board[int(automove[0])-1][ord(automove[1])-ord('A')] == ' '):
        
            
        board[int(automove[0])-1][ord(automove[1])-ord('A')] = player
            
        return True
        
    return False



def is_full(board):
    if (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[0][3] != ' ' and board[0][4] != ' '
        and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[1][3] != ' ' and board[1][4] != ' '
        and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ' and board[2][3] != ' ' and board[2][4] != ' '
        and board[3][0] != ' ' and board[3][1] != ' ' and board[3][2] != ' ' and board[3][3] != ' ' and board[3][4] != ' '
        and board[4][0] != ' ' and board[4][1] != ' ' and board[4][2] != ' ' and board[4][3] != ' ' and board[4][4] != ' '):
        if find_winner(board) == None:
            return True
        else:
            return True
    else:
        return False



def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

