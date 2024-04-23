




from Unit_1_project_functions import *








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

    
    board =  [[' ', ' ', 'X', ' ', ' '],
              [' ', 'X', 'o', ' ', ' '],
              ['x', 'x', 'O', 'o', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ']]
    TEST('diagonal win (big X)', 'x', find_winner(board))

    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', 'O', 'X', ' ', ' '],
              ['O', 'x', 'x', 'X', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ']]
    TEST('diagonal win (big X)', 'o', find_winner(board))

    board =  [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', 'o', ' ', ' '],
              [' ', ' ', 'O', 'o', 'x'],
              [' ', ' ', ' ', 'x', ' '],
              [' ', ' ', 'x', ' ', ' ']]
    TEST('diagonal win (small x)', 'x', find_winner(board))

    board =  [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', 'X', ' ', ' '],
              ['o', 'x', 'x', 'X', ' '],
              [' ', 'o', ' ', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('diagonal win (small o)', 'o', find_winner(board))

    
    board =  [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', 'x', ' ', ' '],
              ['O', 'o', 'O', 'o', 'o'],
              [' ', 'X', 'x', 'x', ' '],
              [' ', ' ', 'x', ' ', ' ']]
    TEST('row win (different sizes o)', 'o', find_winner(board))

    board =  [[' ', ' ', ' ', ' ', ' '],
              [' ', 'o', 'o', ' ', ' '],
              ['X', 'x', 'x', 'X', 'x'],
              [' ', 'o', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('diagonal win (different sizes x)', 'x', find_winner(board))

    
    board =  [[' ', ' ', 'X', ' ', ' '],
              [' ', ' ', 'x', ' ', ' '],
              ['O', 'o', 'x', 'o', 'o'],
              [' ', 'o', 'x', ' ', ' '],
              [' ', ' ', 'x', ' ', ' ']]
    TEST('column win (different sizes x)', 'x', find_winner(board))

    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', 'x', 'o', ' ', ' '],
              ['X', 'x', 'o', 'X', 'x'],
              [' ', 'x', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('column win (different sizes o)', 'o', find_winner(board))


    print('End find_winner_TEST')
    print()


def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'X', 'x'],
              [' ', 'x', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('o', '2B o', board))
    expected_board =  [[' ', ' ', 'O', ' ', ' '],
                       [' ', 'o', 'o', ' ', ' '],
                       [' ', 'x', 'x', 'X', 'x'],
                       [' ', 'x', 'o', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    
    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'X', 'x'],
              [' ', 'x', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('o', '4D o', board))
    expected_board =  [[' ', ' ', 'O', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' '],
                       [' ', 'x', 'x', 'X', 'x'],
                       [' ', 'x', 'o', 'o', ' '],
                       [' ', ' ', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)
    
    
    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'X', 'x'],
              [' ', 'x', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('o', '3B O', board))
    expected_board =  [[' ', ' ', 'O', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' '],
                       [' ', 'O', 'x', 'X', 'x'],
                       [' ', 'x', 'o', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    
    board =  [[' ', ' ', 'O', ' ', ' '],
              [' ', ' ', 'o', ' ', ' '],
              [' ', 'x', 'x', 'X', 'x'],
              [' ', 'x', 'o', ' ', ' '],
              [' ', ' ', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('o', '3E O', board))
    expected_board =  [[' ', ' ', 'O', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' '],
                       [' ', 'x', 'x', 'X', 'O'],
                       [' ', 'x', 'o', ' ', ' '],
                       [' ', ' ', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    
    board = [[' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ']]
    expected_board = board
    TEST('reject move, corner', False, make_move('x', '2a O', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, coner', False, make_move('x', '1A x', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '3A xx ', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '3Becky o', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off grid', False, make_move('o', '1F O', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off grid', False, make_move('o', '0A o', board))
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
