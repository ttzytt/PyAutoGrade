

from tic_tac_toe_functions import *










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

    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'x'],
              ['x', 'o', ' '] ]
    TEST('row win', 'x', find_winner(board))
    
    board = [ [' ', ' ', ' '],
              ['x', ' ', 'x'],
              ['o', 'o', 'o'] ]
    TEST('row win', 'o', find_winner(board))

    
    board = [ ['x', ' ', ' '],
              ['x', ' ', 'o'],
              ['x', 'o', 'o'] ]
    TEST('column win', 'x', find_winner(board))
    
    board = [ ['x', 'x', 'o'],
              ['x', ' ', 'o'],
              ['o', 'x', 'o'] ]
    TEST('column win', 'o', find_winner(board))
    

    
    board = [ ['x', ' ', ' '],
              ['x', 'x', ' '],
              ['o', 'o', 'x'] ]
    TEST('diagonal win', 'x', find_winner(board))
    
    board = [ ['x', 'x', 'o'],
              ['x', 'o', 'x'],
              ['o', 'x', 'x'] ]
    TEST('diagonal win', 'o', find_winner(board))

    
    board = [ [' ', 'o', ' '],
              ['x', ' ', 'x'],
              ['x', 'o', ' '] ]
    TEST('no winner', None, find_winner(board))
    
    board = [ ['x', 'o', 'x'],
              ['x', 'o', 'x'],
              ['o', 'x', 'o'] ]
    TEST('no winner', None, find_winner(board))

    print('End find_winner_TEST')
    print()


def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'o'],
              [' ', ' ', 'o'] ]
    TEST('accept legal move', True, make_move('x', '1C', board))
    expected_board = [ [' ', ' ', 'x'],
                       ['x', 'x', 'o'],
                       [' ', ' ', 'o'] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'o'],
              [' ', ' ', 'o'] ]
    TEST('accept legal move', True, make_move('o', '3A', board))
    expected_board = [ [' ', ' ', ' '],
                       ['x', 'x', 'o'],
                       ['o', ' ', 'o'] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' '] ]
    expected_board = board
    TEST('reject move, wrong case', False, make_move('x', '2a', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('x', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('x', 'A3', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '1Aicky', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '1D', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '0A', board))
    TEST('dont change after rejected move', expected_board, board)

    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'o'],
              [' ', ' ', 'o'] ]
    expected_board = board
    TEST('reject move, space occupied', False, make_move('x', '2A', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, space occupied', False, make_move('o', '3C', board))
    TEST('dont change after rejected move', expected_board, board)
    
    print('End make_move_TEST')
    print()


def next_player_TEST():
    print('Start next_player_TEST')
    TEST('x to o', 'o', next_player('x'))
    TEST('o to x', 'x', next_player('o'))
    print('End next_player_TEST')
    print()




find_winner_TEST()
make_move_TEST()
next_player_TEST()

