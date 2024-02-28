



from connect_four_remove_functions import *









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

    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', 'o', ' ', ' '],
             [' ', ' ', ' ', 'o', 'o', ' '],
             ['x', 'x', 'x', 'x', 'o', ' ']]
    TEST('row win', 'Player X wins!', find_winner(board))
    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             ['x', ' ', ' ', ' ', ' ', ' '],
             ['o', 'o', 'o', 'o', ' ', ' '],
             ['x', 'o', 'x', 'x', ' ', ' ']]
    TEST('row win', 'Player O wins!', find_winner(board))

    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             ['x', ' ', ' ', ' ', ' ', ' '],
             ['x', 'o', ' ', ' ', ' ', ' '],
             ['x', 'o', ' ', ' ', ' ', ' '],
             ['x', 'o', 'o', ' ', ' ', ' ']]
    TEST('column win', 'Player X wins!', find_winner(board))
    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'o', ' ', ' ', ' ', ' '],
             [' ', 'o', ' ', ' ', ' ', ' '],
             [' ', 'o', 'x', ' ', ' ', ' '],
             ['x', 'o', 'x', 'x', ' ', ' ']]
    TEST('column win', 'Player O wins!', find_winner(board))
    

    
    board = [[' ', ' ', ' ', ' ', 'x', ' '],
             [' ', ' ', ' ', 'x', 'x', ' '],
             [' ', ' ', 'x', 'o', 'o', ' '],
             [' ', 'x', 'o', 'x', 'o', ' '],
             [' ', 'o', 'o', 'o', 'x', ' ']]
    TEST('diagonal win', 'Player X wins!', find_winner(board))
    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             ['o', ' ', ' ', ' ', ' ', ' '],
             ['o', 'o', ' ', ' ', ' ', ' '],
             ['x', 'x', 'o', ' ', ' ', ' '],
             ['x', 'x', 'x', 'o', ' ', ' ']]
    TEST('diagonal win', 'Player O wins!', find_winner(board))

    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'x', ' ', ' ', ' ', ' '],
             ['x', 'o', 'o', ' ', ' ', ' ']]
    TEST('no winner', None, find_winner(board))
    
    board = [['o', ' ', ' ', ' ', ' ', ' '],
             ['x', ' ', ' ', ' ', ' ', ' '],
             ['o', ' ', ' ', ' ', ' ', ' '],
             ['x', ' ', ' ', ' ', ' ', ' '],
             ['o', ' ', ' ', ' ', ' ', ' ']]
    TEST('no winner', None, find_winner(board))

    print('End find_winner_TEST')
    print()



def make_move_TEST():
    print('Start make_move_TEST')
    
    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'x', ' ', ' ', ' ', ' '],
             ['x', 'o', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', ' ', ' ', ' '],
             ['o', 'x', 'x', 'o', ' ', ' ']]
    TEST('accept legal move', True, make_move('x', '2', board))
    expected_board = [[' ', 'x', ' ', ' ', ' ', ' '],
             [' ', 'x', ' ', ' ', ' ', ' '],
             ['x', 'o', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', ' ', ' ', ' '],
             ['o', 'x', 'x', 'o', ' ', ' ']]
    TEST('make legal move', expected_board, board)

    expected_board = board

    print('End make_move_TEST')
    print()

def remove_chip_TEST(): 
    print('Start remove_chip_TEST')

    
    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             ['o', 'x', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', 'o', ' ', ' '],
             ['x', 'x', 'x', 'o', ' ', ' ']]
    board.reverse()  
    TEST('accept remove chip', True, remove_chip('x', 'R1', board))
    expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'x', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', 'o', ' ', ' '],
             ['o', 'x', 'x', 'o', ' ', ' ']]
    expected_board.reverse()
    TEST('remove chip', expected_board, board)
    
    expected_board = board

    board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             ['o', 'x', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', 'o', ' ', ' '],
             ['x', 'x', 'x', 'o', ' ', ' ']]
    board.reverse()  
    TEST('reject remove chip', False, remove_chip('o', 'R1', board))
    expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             ['o', 'x', ' ', ' ', ' ', ' '],
             ['o', 'o', 'x', 'o', ' ', ' '],
             ['x', 'x', 'x', 'o', ' ', ' ']]
    expected_board.reverse()
    TEST('dont change  after reject remove chip', expected_board, board)
    
    expected_board = board

    print('End remove_chip_TEST')
    print()
    TEST('reject move, no location', False, make_move('x', '', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('x', '1Aicky', board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('o', '0', board))
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
remove_chip_TEST()
next_player_TEST()
