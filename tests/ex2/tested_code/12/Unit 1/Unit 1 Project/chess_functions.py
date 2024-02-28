

def draw_row(row, row_number):
    
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ '
          + row[6] + ' │ '
          + row[7] + ' │ ')


def draw_board(board):

    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 8)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   ')

def make_move(board,ori,des):
    piece = board[int(ori[0])-1][ord(ori[1])-ord('A')]
    board[int(ori[0])-1][ord(ori[1])-ord('A')] = ' '
    board[int(des[0])-1][ord(des[1])-ord('A')] = piece

def undo_last_step(board,last_move):
    ori = last_move[0:2]
    des = last_move[2:4]
    piece = board[int(des[0])-1][ord(des[1])-ord('A')]
    board[int(des[0])-1][ord(des[1])-ord('A')] = ' '
    board[int(ori[0])-1][ord(ori[1])-ord('A')] = piece
