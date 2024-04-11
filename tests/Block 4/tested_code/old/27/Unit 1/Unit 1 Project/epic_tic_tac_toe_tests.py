



from epic_tic_tac_toe_functions import *









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

    
    board = [[['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'o', 'o']],

         [['x', 'o', 'x'],
          ['x', 'o', 'o'],
          ['x', 'x', 'o']],

         [['x', 'o', 'x'],
          ['o', 'o', 'x'],
          ['o', 'x', 'x']],

         [['x', 'x', 'x'],
          ['o', 'o', 'x'],
          ['x', 'o', 'x']],

         [['x', 'x', 'o'],
          ['o', 'o', 'x'],
          ['x', 'x', 'x']],

         [['x', 'x', 'o'],
          ['o', 'x', 'x'],
          ['o', 'o', 'o']],

         [['x', 'x', 'o'],
          ['o', 'o', 'x'],
          ['o', 'x', 'o']],

         [['x', 'o', 'x'],
          ['o', 'x', 'o'],
          ['x', 'x', 'x']],

         [['x', 'o', 'x'],
          ['o', 'o', 'x'],
          ['x', 'x', 'o']]]
    board_2 = [[[' '], [' '], [' ']],
                [[' '], [' '], [' ']],
                [[' '], [' '], [' ']]]
    board_index = 0
    find_winner(board, board_index, board_2)
    
    TEST('win', 'x', find_master_winner(board_2))

    
    board = [[['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'o', 'o']],

             [['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['x', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['o', 'x', 'x']],

             [['x', 'x', 'x'],
              ['o', 'o', 'x'],
              ['x', 'o', 'x']],

             [['x', 'x', 'o'],
              ['o', 'o', 'o'],
              ['x', 'o', 'x']],

             [['x', 'x', 'o'],
              ['o', 'x', 'x'],
              ['o', 'o', 'o']],

             [['x', 'x', 'o'],
              ['o', 'o', 'x'],
              ['o', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'x', 'o'],
              ['x', 'x', 'x']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['x', 'x', 'o']]]
    board_2 = [[[' '], [' '], [' ']],
               [[' '], [' '], [' ']],
               [[' '], [' '], [' ']]]
    board_index = 0
    find_winner(board, board_index, board_2)
    
    TEST('tie', 'd', find_master_winner(board_2))
    board = [[['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'x', 'o']],

             [['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['o', 'x', 'o']],

             [['x', 'x', 'o'],
              ['o', 'o', 'x'],
              ['x', 'o', 'o']],

             [['o', 'x', 'o'],
              ['o', 'x', 'o'],
              ['x', 'o', 'x']],

             [['x', 'x', 'o'],
              ['o', 'x', 'x'],
              ['x', 'o', 'o']],

             [['x', 'x', 'o'],
              ['o', 'o', 'x'],
              ['x', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'x', 'o'],
              ['x', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['x', 'x', 'o']]]
    board_2 = [[[' '], [' '], [' ']],
               [[' '], [' '], [' ']],
               [[' '], [' '], [' ']]]
    board_index = 0
    find_winner(board, board_index, board_2)
    
    TEST('all tie', 'd', find_master_winner(board_2))

    board = [[['o', 'x', 'o'],
              ['o', 'x', 'x'],
              ['x', 'o', 'x']],

             [['o', 'x', 'o'],
              ['o', 'x', 'x'],
              ['x', 'o', 'x']],

             [['o', 'x', 'o'],
              ['x', 'x', 'o'],
              ['x', 'o', 'x']],

             [['o', 'o', 'x'],
              ['x', 'x', 'o'],
              ['o', 'x', 'x']],

             [['x', 'o', 'x'],
              ['x', 'o', 'x'],
              ['o', 'x', 'o']],

             [['o', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'x', 'x']],

             [['o', 'o', 'x'],
              ['x', 'x', 'o'],
              ['o', 'o', 'x']],

             [['x', 'o', 'x'],
              ['o', 'x', 'o'],
              ['x', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['x', 'x', 'o']]]
    board_2 = [[[' '], [' '], [' ']],
               [[' '], [' '], [' ']],
               [[' '], [' '], [' ']]]
    board_index = 0
    find_winner(board, board_index, board_2)
    
    TEST('all tie', 'd', find_master_winner(board_2))


    
    board = [[['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['o', 'o', 'o']],

             [['x', 'o', 'x'],
              ['x', 'o', 'o'],
              ['x', 'x', 'o']],

             [['x', 'o', 'o'],
              ['o', 'o', 'x'],
              ['o', 'o', 'x']],

             [['x', 'o', 'x'],
              ['o', 'x', 'x'],
              ['x', 'o', 'x']],

             [['x', 'x', 'o'],
              ['o', 'o', 'o'],
              ['x', 'o', 'x']],

             [['x', 'x', 'o'],
              ['o', 'x', 'x'],
              ['o', 'o', 'o']],

             [['x', 'x', 'o'],
              ['o', 'o', 'x'],
              ['o', 'x', 'o']],

             [['x', 'o', 'x'],
              ['o', 'x', 'o'],
              ['x', 'x', 'x']],

             [['x', 'o', 'x'],
              ['o', 'o', 'x'],
              ['x', 'x', 'o']]]
    board_2 = [[[' '], [' '], [' ']],
               [[' '], [' '], [' ']],
               [[' '], [' '], [' ']]]
    board_index = 0
    find_winner(board, board_index, board_2)
    
    TEST('win', 'o', find_master_winner(board_2))


    print('End find_winner_TEST')
    print()

def make_move_TEST():
    print('Start make_move_TEST')
    
    
    changes_left = {'o': 3, 'x': 3}
    board = [[[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]]

    TEST('accept legal move', True, make_move('o', '63A', board, changes_left))
    expected_board = [[[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              ['o', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]]

    TEST('make legal move', expected_board, board)

    
    changes_left = {'o': 3, 'x': 3}
    board = [[[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', 'x', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]]

    TEST('accept legal move', True, make_move('o', '32B', board, changes_left))
    expected_board = [[[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', 'o', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]]

    TEST('make legal move', expected_board, board)

    
    changes_left = {'o': 0, 'x': 3}
    board = [[[' ', 'x', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']],

             [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', 'O', ' ']]]
    expected_board = board
    TEST('reject move, wrong format', False, make_move('o', '2a', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong format', False, make_move('o', '111A', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('o', 'A3', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong format', False, make_move('x', 'python', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no more chance', False, make_move('o', '11B', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no take back', False, make_move('x', '11B', board, changes_left))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no change after the game is done', False, make_move('x', '93B', board, changes_left))
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
