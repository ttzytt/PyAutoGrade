



from project_connect_four_functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)








def find_winner_TEST():
    print('Start find_winner_TEST')

    
    board = [ [ ['x', 'x', 'x', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'x', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', 'x '],
          [' ', ' ', ' ', ' '] ], [ [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', 'o'] ] ]
    TEST('row win', 'x', find_winner(board))
    
    board = [ [ ['x', '', '', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '] ], [ [' ', 'x', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'x', ' ', ' '] ], [ [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' '],
          ['o', 'o', 'o', 'x '],
          [' ', ' ', ' ', ' '] ], [ ['x', ' ', ' ', ' '],
          ['o', 'o', 'o', 'o'],
          [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('row win', 'o', find_winner(board))

    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ ['x', ' ', 'o', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ ['x', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('column win', 'x', find_winner(board))
    
    board = [ [ [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', 'x', ' ', ' '],
          ['x', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x'] ], [ [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '] ] ]
    TEST('column win', 'o', find_winner(board))
    

    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', 'x', ' ', ' '],
          [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', 'x'] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          ['o', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('small diagonal row win', 'x', find_winner(board))
    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', 'o'],
          [' ', ' ', 'o', ' '],
          [' ', 'o', ' ', ' '],
          ['o', ' ', ' ', ' '] ], [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('small diagonal row win', 'o', find_winner(board))

    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', 'x', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '] ], [ [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', 'x'],
          ['o', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('small diagonal column win', 'x', find_winner(board))
    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', 'x', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'o'],
          [' ', ' ', ' ', ' '] ] ]
    TEST('small diagonal column win', 'o', find_winner(board))

    
    board = [ [ ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', 'o', ' ', ' '],
          [' ', 'x', ' ', ' '],
          [' ', ' ', ' ', 'o'],
          ['o', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x'] ] ]
    TEST('big diagonal win', 'x', find_winner(board))

    board = [ [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', 'o'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('big diagonal win', 'o', find_winner(board))
    
    board = [ [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('no winner', None, find_winner(board))
    
    board = [ [ ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('no winner', None, find_winner(board))

    print('End find_winner_TEST')
    print()


def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board = [ [ ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('accept legal move', True, make_move('x', 'WB1', board))
    expected_board = [ [ ['o', 'x', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [ ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('accept legal move', True, make_move('o', 'XA3', board))
    expected_board = [ [ ['o', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', 'o', ' '],
          [' ', ' ', ' ', 'x'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    expected_board = board
    TEST('reject move, wrong case', False, make_move('x', 'wA2', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('x', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('x', '3AY', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', 'WA1dficky', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', 'WE1', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', 'QB5', board))
    TEST('dont change after rejected move', expected_board, board)

    
    board = [ [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'x', ' ', ' '] ], [ [' ', 'x', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'o'] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    expected_board = board
    TEST('reject move, space occupied', False, make_move('x', 'WB4', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, space occupied', False, make_move('o', 'ZB2', board))
    TEST('dont change after rejected move', expected_board, board)
    
    print('End make_move_TEST')
    print()


def next_player_TEST():
    print('Start next_player_TEST')
    TEST('x to o', 'o', next_player('x'))
    TEST('o to x', 'x', next_player('o'))
    print('End next_player_TEST')
    print()

def rotate_layer_TEST():
    print('Start rotate_layer_TEST')
    
    board = [ [ ['x', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '],
          ['x', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('accept rotation', True, rotate_layer('W', '3', board))

    expected_board = [ [ [' ', ' ', ' ', ' '],
          ['o', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', ' ', 'x'] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]
    TEST('make rotation', expected_board, board)

    board = [ [ ['x', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '],
          ['x', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]



    TEST('accept rotation', True, rotate_layer('Y', '2', board))

    expected_board = [ [ ['x', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '],
          ['x', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]

    TEST('make rotation', expected_board, board)

    

    board = [ [ ['x', ' ', 'o', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', 'o', ' '],
          ['x', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'o', ' ', ' '],
          [' ', ' ', 'x', ' '] ], [ [' ', 'o', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', 'x', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['x', ' ', 'o', ' '] ] ]
    TEST('reject rotation', False, rotate_layer('YA','2', board))
    TEST('reject rotation', False, rotate_layer('P','2', board))
    TEST('reject rotation', False, rotate_layer('Y','33', board))

    




find_winner_TEST()
make_move_TEST()
next_player_TEST()
rotate_layer_TEST()