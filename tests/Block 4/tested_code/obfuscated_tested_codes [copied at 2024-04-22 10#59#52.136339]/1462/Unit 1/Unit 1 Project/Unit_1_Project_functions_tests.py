


from Unit_1_Project_functions import *









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

    
    board=[ [ 1, 1, 1, 1, 1, -1],
            [ 0, -1, 1, -1, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ -1, 0, -1, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0] ]
    TEST('row win', 'o', find_winner(board))
    
    board=[ [ 1, 1, 1, 1, 0, 1],
            [ 1, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ 0, -1, -1, -1, -1, -1],
            [ 0, 0, 0, 0, 0, 0] ]
    TEST('row win', 'x', find_winner(board))

    
    board=[ [ 0, 0, 1, 0, 0, -1],
            [ 0, 0, 1, 0, 0, 0],
            [ 0, 0, 1, 0, -1, 0],
            [ -1, 0, 1, 0, 0, 0],
            [ 0, 0, 1, 0, -1, 0],
            [ 0, 0, 1, 0, 0, 0] ]
    TEST('column win', 'o', find_winner(board))
    
    board=[ [ 1, 0, 0, 1, -1, 0],
            [ 0, 0, 0, 0, -1, 0],
            [ 0, 1, 0, 0, -1, 0],
            [ 0, 0, 0, 0, -1, 0],
            [ 0, 0, 1, 0, -1, 0],
            [ 1, 0, 1, 0, 0, 0] ]
    TEST('column win', 'x', find_winner(board))

    
    board=[ [ 0, 1, 0, 0, 0, -1],
            [ 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0 ],
            [ -1, 0, 0, 0, 1, 0],
            [ 0, -1, 0, 0, 0, 1],
            [ -1, 0, 0, 0, 0, 0] ]
    TEST('diagonal win', 'o', find_winner(board))

    
    board=[ [ 1, 0, 0, 1, 0, 1],
            [ 0, 0, 0, 0, 0, -1],
            [ 0, 1, 0, 0, -1, 0],
            [ 0, 0, 0, -1, 0, 0],
            [ 1, 0, -1, 0, 0, 0],
            [ 0, -1, 0, 0, 0, 1] ]
    TEST('diagonal win', 'x', find_winner(board))

    board=[ [ -1, 0, 0, 0, 0, -1],
            [ 0, 1, 0, 0, -1, 0],
            [ 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0],
            [ 0, 0, 0, 0, 1, 0],
            [ 0, -1, 0, 0, 0, 1] ]
    TEST('diagonal win', 'o', find_winner(board))
    board=[ [ 0, 0, 0, 0, 0, -1],
            [ 1, 1, 0, 0, -1, 1],
            [ 1, 0, 1, -1, 0, 0],
            [ 1, 0, -1, 1, 0, 0],
            [ 0, -1, 0, 0, 1, 0],
            [ -1, 0, 0, 0, 0, -1] ]
    TEST('diagonal win', 'x', find_winner(board))

    
    board=[ [ 1, 0, 0, 0, 0, -1],
            [ 0, 1, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0],
            [ 1, 1, 1, 1, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ -1, -1, -1, 0, -1, -1] ]
    TEST('no winner', None, find_winner(board))
    
    board=[ [ 1, 0, 0, -1, 0, 0],
            [ 1, 0, 0, 0, -1, 0],
            [ 1, 0, 0, 0, 0, 0],
            [ 0, 0, 0, -1, 0, -1],
            [ 1, 0, 0, 0, 0, 0],
            [ 1, 0, 0, 0, 0, 0] ]
    TEST('no winner', None, find_winner(board))

    print('End find_winner_TEST')
    print()


def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board = [ [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0] ]
    TEST('accept legal move', True, make_move('x', '3C', board))
    expected_board = [ [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, -1, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0]  ]
    TEST('accept legal move', True, make_move('o', '6F', board))
    expected_board = [ [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 1] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0] ]
    expected_board = board
    TEST('reject move, wrong case', False, make_move('x', '2a', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('x', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('x', 'A3', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '1Aicky', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '7D', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '0A', board))
    TEST('dont change after rejected move', expected_board, board)

    
    board = [ [ 1, 0, 0, -1, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 0, 0, 1, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ -1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0] ]
    expected_board = board
    TEST('reject move, space occupied', False, make_move('x', '1A', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, space occupied', False, make_move('o', '3C', board))
    TEST('dont change after rejected move', expected_board, board)
    
    print('End make_move_TEST')
    print()


def make_spin_TEST():
    print('Start make_spin_TEST')
    
    
    board = [ [ 1, 0, 0, 0, 0, 0],
              [ 1, 1, 0, 1, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0] ]
    TEST('accept legal spin', True, make_spin('o', '3C', board))
    expected_board = [ [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 1, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 1, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 1, 0, -1],
              [ -1, 0, 0, 0, 0, 0],
              [ -1, 0, 0, -1, 1, 0]  ]
    TEST('accept legal spin', True, make_spin('x', '5E', board))
    expected_board = [ [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 1, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, -1, 0, 1],
                       [ -1, 0, 0, 1, 0, 0],
                       [ -1, 0, 0, 0, 0, -1] ]
    TEST('make legal spin', expected_board, board)

    
    
    TEST('reject move, off board', False, make_spin('o', '6F', board))

    print('End make_spin_TEST')
    print()

    
def next_player_TEST():
    print('Start next_player_TEST')
    TEST('x to o', 'o', next_player('x'))
    TEST('o to x', 'x', next_player('o'))
    print('End next_player_TEST')
    print()




find_winner_TEST()
make_move_TEST()
make_spin_TEST()
next_player_TEST() 
