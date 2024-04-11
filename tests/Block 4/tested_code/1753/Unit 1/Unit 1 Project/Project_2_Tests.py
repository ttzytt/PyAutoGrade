

from Project_2_Functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)







def four_in_row_TEST():
    print('Start four_in_row_TEST')
    TEST('four at beginning', 'x', four_in_row(['x', 'x', 'x', 'x', 'o', ' ']))
    TEST('None', None, four_in_row(['x', 'o', 'x', 'x', 'o', ' ']))
    TEST('four in middle', 'o', four_in_row(['x', 'o', 'o', 'o', 'o', ' ']))
    TEST('four at end', 'o', four_in_row(['x', 'x', 'o', 'o', 'o', 'o']))
    TEST('four spaces', None, four_in_row(['x', 'x', ' ', ' ', ' ', ' ']))
    TEST('three in beginning', None, four_in_row(['x', 'x', 'x', 'o', ' ', 'o']))
    TEST('three in middle', None, four_in_row(['x', 'x', 'o', 'o', 'o', 'x']))
    TEST('three at end', None, four_in_row(['x', 'x', 'o', 'x', 'x', 'x']))
    print('End four_in_row_TEST')
    print()

    
def find_winner_TEST():
    print('Start find_winner_TEST')

    
    board = [ ['x', 'o', 'o', ' ', ' ', ' '],
              ['o', 'x', 'o', ' ', ' ', ' '],
              ['o', 'x', 'x', ' ', ' ', ' '],
              ['x', 'o', 'x', 'o', ' ', ' '],
              ['o', 'o', 'o', 'x', ' ', ' '],
              ['x', 'x', 'x', 'x', ' ', ' '],
              ['x', 'o', 'o', ' ', ' ', ' ']]
    TEST('row win', 'x', find_winner(board))
    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'x', 'o', ' ', ' ', ' '],
              ['x', 'x', 'x', ' ', ' ', ' '],
              ['o', 'o', 'o', 'o', ' ', ' ']]
    TEST('row win', 'o', find_winner(board))

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              ['o', 'x', 'x', 'o', 'x', 'x'],
              [' ', 'x', ' ', ' ', 'o', 'x'],
              [' ', 'x', 'o', ' ', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'o', ' ', ' ', ' ']]
    TEST('column win', 'x', find_winner(board))
    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              ['x', ' ', ' ', ' ', ' ', ' '],
              ['x', ' ', ' ', ' ', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('column win', 'x', find_winner(board))
    

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              ['x', ' ', 'o', 'x', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', 'o', ' '],
              ['o', 'o', 'x', 'o', ' ', 'o']]
    TEST('diagonal win', 'o', find_winner(board))
    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', 'x', ' '],
              [' ', ' ', ' ', 'x', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'o', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('diagonal win', 'x', find_winner(board))

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('no winner', None, find_winner(board))
    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'x', ' ', ' '],
              [' ', 'x', 'o', 'o', ' ', ' '],
              ['o', 'x', 'x', 'o', ' ', ' '],
              ['o', 'x', 'x', 'o', ' ', ' ']]
    TEST('no winner', None, find_winner(board))

    print('End find_winner_TEST')
    print()


def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'x', 'x', ' ', ' ', ' '],
              ['x', 'o', 'x', ' ', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('x', '3B', board))
    expected_board = [ [' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', 'x', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', 'x', 'x', ' ', ' ', ' '],
                       ['x', 'o', 'x', ' ', ' ', ' '],
                       ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('o', '3A', board))
    expected_board = [ [' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' '],
                       ['o', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', 'x', 'x', 'o', ' ', ' '],
                       ['x', 'x', 'x', 'o', ' ', ' '],
                       ['o', 'o', 'x', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    expected_board = board
    TEST('reject move, wrong case', False, make_move('x', '2a', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('x', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('x', 'A3', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '1Aicky', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '10D', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '0A', board))
    TEST('dont change after rejected move', expected_board, board)

    
    board = [ [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'o', ' ', ' '],
              ['x', 'x', 'x', 'o', ' ', ' '],
              ['o', 'o', 'x', 'o', ' ', ' ']]
    expected_board = board
    TEST('reject move, space occupied', False, make_move('x', '7A', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, space occupied', False, make_move('o', '5C', board))
    TEST('dont change after rejected move', expected_board, board)
    
    print('End make_move_TEST')
    print()


def next_player_TEST():
    print('Start next_player_TEST')
    TEST('x to o', 'o', next_player('x'))
    TEST('o to x', 'x', next_player('o'))
    print('End next_player_TEST')
    print()




four_in_row_TEST()
find_winner_TEST()
make_move_TEST()
next_player_TEST()

