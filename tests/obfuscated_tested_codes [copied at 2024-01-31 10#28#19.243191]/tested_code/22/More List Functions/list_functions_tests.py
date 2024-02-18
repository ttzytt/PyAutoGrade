

from list_functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)








def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    
    
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




item_moved_to_end_TEST()
move_item_to_end_TEST()
