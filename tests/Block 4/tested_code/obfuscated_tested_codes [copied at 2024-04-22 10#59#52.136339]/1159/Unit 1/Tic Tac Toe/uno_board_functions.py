'''
DO NOT RUN THIS CODE
'''

'''
HAVE FUN WITH UNO USING PYTHON!
'''





def draw_row(row, row_number):
    
    print(str(row_number) + ' │ '
          + row[0] + '   │ '
          + row[1] + '   │ ')


def draw_board(board):

    print('  ┌───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┤ ')
    draw_row(board[1], 2)
    print('  └───┴───┘ ')
    print('    A   B   ')



    


def make_move(card,board,list,judge):
    
    if list == 0:
        board[0][0] = card
    elif list == 1:
        board[0][1] = card
    elif list == 2:
        board[1][1] = card
    elif list == 3:
        board[1][0] = card




    


    
    

          
