


from unit_1_project_functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)






def make_piece_TEST():
    print('Start make_piece_TEST') 
    player = 'x'
    size = 2
    TEST('make_piece_TEST', 'X', make_piece(player,size))
    
    player = 'x'
    size = 1
    TEST('make_piece_TEST', 'x', make_piece(player,size))
    
    player = 'o'
    size = 2
    TEST('make_piece_TEST', 'O', make_piece(player,size))
    
    player = 'o'
    size = 1
    TEST('make_piece_TEST', 'o', make_piece(player,size))
    print('End make_piece_TEST')
    print()
    
def size_TEST():
    print('Start size_TEST')
    piece = 'x'
    TEST('size', 1, size_of(piece))
    
    piece = 'o'
    TEST('size', 1, size_of(piece))
    
    piece = 'X'
    TEST('size', 2, size_of(piece))
    
    piece = 'O'
    TEST('size', 2, size_of(piece))

    piece = ' '
    TEST('size', 0, size_of(piece))
    print('End size_TEST')
    print()


def find_winner_TEST():
    print('Start find_winner_TEST')

    
    board = [ [' ', ' ', ' '],
              ['X', 'x', 'X'],
              ['x', 'o', ' '] ]
    TEST('row win', 'x', find_winner(board))
    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'x'],
              ['x', 'o', ' '] ]
    TEST('row win', 'x', find_winner(board))
    
    board = [ [' ', ' ', ' '],
              ['x', ' ', 'x'],
              ['o', 'O', 'o'] ]
    TEST('row win', 'o', find_winner(board))

    
    board = [ ['x', ' ', ' '],
              ['x', ' ', 'o'],
              ['X', 'o', 'o'] ]
    TEST('column win', 'x', find_winner(board))
    
    board = [ ['X', 'x', 'o'],
              ['x', ' ', 'O'],
              ['o', 'x', 'o'] ]
    TEST('column win', 'o', find_winner(board))

    board = [ ['x', 'o', ' '],
              ['o', 'O', 'x'],
              ['x', 'o', 'x'] ]
    TEST('column win', 'o', find_winner(board))
    

    
    board = [ ['x', ' ', ' '],
              ['x', 'X', ' '],
              ['o', 'o', 'x'] ]
    TEST('diagonal win', 'x', find_winner(board))
    
    board = [ ['x', 'x', 'O'],
              ['x', 'O', 'x'],
              ['O', 'x', 'x'] ]
    TEST('diagonal win', 'o', find_winner(board))

    
    board = [ [' ', 'o', ' '],
              ['x', ' ', 'x'],
              ['x', 'O', ' '] ]
    TEST('no winner', None, find_winner(board))
    
    board = [ ['x', 'o', 'x'],
              ['X', 'O', 'x'],
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

    
    board = [ [' ', ' ', ' '],
              ['x', 'x', 'o'],
              [' ', ' ', 'o'] ]
    expected_board = board
    TEST('accept legal move size', True, make_move('X', '2C', board))
    TEST('dont change after rejected move', expected_board, board)

    
    TEST('reject move, space occupied', False, make_move('X','2C', board))
    TEST('dont change after rejected move', expected_board, board)
    
    
    board = [ [' ', ' ', ' '],
              ['X', 'X', 'o'],
              [' ', 'X', 'o'] ]
    expected_board = board
    TEST('reject move, space occupied', False, make_move('x', '2C', board))
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
make_piece_TEST()
size_TEST()


