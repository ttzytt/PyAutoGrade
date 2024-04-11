




from pente_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)







def find_winner_2_TEST():
    print('Start find_winner_2_TEST')

    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[9][9] = 'O'

    TEST('First move', None, find_winner_2(board, '10 J'))


    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[9][7] = 'O'
    board[9][8] = 'O'
    board[9][9] = 'O'
    board[9][10] = 'O'
    board[9][11] = 'O'

    TEST('Row win', 'O', find_winner_2(board, '10 L'))


    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[7][9] = 'O'
    board[8][9] = 'O'
    board[9][9] = 'O'
    board[10][9] = 'O'
    board[11][9] = 'O'

    TEST('Column win', 'O', find_winner_2(board, '8 J'))

    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[7][7] = '#'
    board[8][8] = '#'
    board[9][9] = '#'
    board[10][10] = '#'
    board[11][11] = '#'

    TEST('Diagonal win', '#', find_winner_2(board, '12 L'))


    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[7][11] = '#'
    board[8][10] = '#'
    board[9][9] = '#'
    board[10][8] = '#'
    board[11][7] = '#'

    TEST('Diagonal win', '#', find_winner_2(board, '9 K'))

    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[7][7] = '#'
    board[8][8] = '#'
    board[9][9] = '#'
    board[10][10] = '#'

    TEST('4 in a row', None, find_winner_2(board, '8 H'))


    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[0][1] = '#'
    board[1][2] = '#'
    board[2][3] = '#'
    board[3][4] = '#'
    board[4][5] = '#'

    TEST('Edge of board', '#', find_winner_2(board, '2 C'))


    row = []
    board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
    board[0][1] = '#'
    board[1][2] = '#'
    board[2][3] = '#'
    board[3][4] = '#'
    board[4][5] = '#'

    TEST('Move unrelated to win', None, find_winner_2(board, '10 J'))
    print('End find_winner_2_TEST')


def has_5_in_a_row_TEST():
    
    print('Start has_5_in_a_row_TEST')

    TEST('Empty spaces', None, has_5_in_a_row(['·', '·', '·', '·', '·',
                                           '·', '·', '·', '·']))
    TEST('1 piece', None, has_5_in_a_row(['·', '·', '#', '·', '·',
                                           '·', '·', '·']))
    TEST('5 of the same in a row', 'O', has_5_in_a_row([ '·', '·', 'O',
                                           'O', 'O', 'O', 'O']))
    TEST('Mixed 5 in a row', None, has_5_in_a_row(['·', '#', 'O', 'O', '#',
                                           'O', '·', '·', '·']))
    TEST('Spaces', None, has_5_in_a_row(['O', '·', '#', 'O', 'O',
                                           'O', '·', '·', '·']))
    TEST('5 of the same in a row with other pieces surrounding', 'O',
         has_5_in_a_row(['#', '#', '·', 'O', 'O', 'O', 'O', 'O', '#']))
    TEST('4 of the same in a row', None,
         has_5_in_a_row(['O', 'O', 'O', 'O', '·', 'O', '#', '#', '#']))

    print('End has_5_in_a_row_TEST')


def make_move_TEST():
    print('Start make_move_TEST')

    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)

    TEST('accept legal move', True, make_move('#', '1 C', board))
    expected_board[0][2] = '#'
    TEST('make legal move', expected_board, board)

    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[5][5] = 'O'
    expected_board = board

    TEST('Illegal move (spot taken)', False, make_move('#', '6 F', board))
    TEST('Reject illegal move', expected_board, board)


    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    expected_board = board
    TEST('reject move, wrong case', False, make_move('O', '2 a', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('O', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('O', 'A 3', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('O', '1 Aicky',
                                                           board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('#', '20', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('#', '0A', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('#', 'F 13', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no space', False, make_move('#', '1A', board))
    TEST('dont change after rejected move', expected_board, board)


    print('End make_move_TEST')

    
def find_first_capture_TEST():
    print('Start find_first_capture_TEST')
    
    
    
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = 'O'
    expected_board = board

    find_first_capture(board, '10 J', 'O')
    TEST('no captures, dont change board', expected_board, board)

        
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = 'O'
    board[8][9] = '#'
    board[7][9] = '#'
    expected_board = board

    find_first_capture(board, '10 J', 'O')
    TEST('no captures, dont change board', expected_board, board)
    
    find_first_capture(board, '8 J', '#')
    TEST('no captures, dont change board', expected_board, board)

    
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = 'O'
    board[8][8] = '#'
    board[7][7] = '#'
    board[6][6] = 'O'
    expected_board = board

    
    
    find_first_capture(board, '8 J', '#')
    TEST('self capture, dont change board', expected_board, board)

    expected_board[8][8] = '·'
    expected_board[7][7] = '·'

    
    find_first_capture(board, '7 G', 'O')
    TEST('capture, delete two middle pieces', expected_board, board)


    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][18] = 'O'
    board[8][17] = '#'
    board[7][16] = '#'
    board[6][15] = 'O'
    expected_board[9][18] = 'O'
    expected_board[6][15] = 'O'

    find_first_capture(board, '10 S', 'O')
    TEST('edge capture, delete two middle pieces', expected_board, board)


    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[0][1] = 'O'
    board[1][2] = '#'
    board[2][3] = '#'
    board[3][4] = 'O'
    board[0][2] = '#'
    board[0][3] = '#'
    board[0][4] = 'O'
    board[1][1] = '#'
    board[2][1] = '#'
    board[3][1] = 'O'
    expected_board[0][1] = 'O'
    expected_board[3][4] = 'O'
    expected_board[0][4] = 'O'
    expected_board[3][1] = 'O'

    find_first_capture(board, '1 B', 'O')
    TEST('triple capture, delete three middle pieces', expected_board, board)
    print('End find_first_capture_TEST')

def find_second_capture_TEST():
    print('Start find_second_capture_TEST')
    
    
    
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = 'O'
    expected_board = board

    find_second_capture(board)
    TEST('no captures, dont change board', expected_board, board)

        
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = '#'
    board[8][8] = '#'
    board[7][7] = '#'
    board[6][6] = '#'
    board[9][6] = 'O'
    expected_board = board

    find_second_capture(board)
    TEST('no captures, dont change board', expected_board, board)

    
    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][9] = 'O'
    board[10][10] = 'O'
    board[11][11] = 'O'
    board[12][12] = 'O'
    board[9][12] = '#'
    board[12][9] = '#'
    expected_board[9][12] = '#'
    expected_board[12][9] = '#'
    
    find_second_capture(board)
    TEST('capture, delete 4 diagonal pieces', expected_board, board)


    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[9][18] = '#'
    board[10][17] = '#'
    board[11][16] = '#'
    board[12][15] = '#'
    board[9][15] = 'O'
    board[12][18] = 'O'
    expected_board[9][15] = 'O'
    expected_board[12][18] = 'O'

    find_second_capture(board)
    TEST('edge capture, delete 4 diagonal pieces', expected_board, board)


    
    row = []
    board = []
    expected_board = []
    for j in range(19):
        row = ['·'] * 19
        board.append(row)
        row = ['·'] * 19
        expected_board.append(row)
    board[0][10] = 'O'
    board[1][11] = 'O'
    board[2][12] = 'O'
    board[3][13] = 'O'
    board[0][13] = '#'
    board[3][10] = '#'
    board[3][7] = 'O'
    board[4][8] = 'O'
    board[5][9] = 'O'
    board[6][10] = 'O'
    board[6][7] = '#'
    expected_board[0][13] = '#'
    expected_board[3][10] = '#'
    expected_board[6][7] = '#'


    find_second_capture(board)
    TEST('double capture, delete 8 diagonal pieces', expected_board, board)
    print('End find_second_capture_TEST')

def next_player_TEST():
    print('Start next_player_TEST')
    TEST('# to O', 'O', next_player('#'))
    TEST('O to #', '#', next_player('O'))
    print('End next_player_TEST')

find_winner_2_TEST()
print()
has_5_in_a_row_TEST()
print()
make_move_TEST()
print()
find_first_capture_TEST()
print()
find_second_capture_TEST()
print()
next_player_TEST()
