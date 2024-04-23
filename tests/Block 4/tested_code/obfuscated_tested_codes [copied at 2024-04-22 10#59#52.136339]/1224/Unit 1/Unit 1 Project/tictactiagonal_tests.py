


from tictactiagonal_functions import *
board =  [['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#']]









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)





def check_winner_TEST():
    print('Start check_winner_TEST')
    
    board = [['#', 'x', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', 'x', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', 'x', '#', 'o', '#', ' ', '#'],
          [' ', '#', 'o', '#', 'x', '#', ' ', '#', ' '],
          ['#', ' ', '#', 'o', '#', ' ', '#', ' ', '#'],
          [' ', '#', 'o', '#', 'o', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', 'o', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#']]
    TEST('left to right win', 'x', check_winner(board))

    
    board =  [['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', 'o', '#', ' ', '#', ' '],
          ['#', ' ', '#', 'o', '#', ' ', '#', ' ', '#'],
          [' ', '#', 'o', '#', ' ', '#', ' ', '#', ' '],
          ['#', 'o', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#']]
    TEST('right to left win', 'o', check_winner(board))
    
    board =  [['#', 'x', '#', 'x', '#', ' ', '#', ' ', '#'],
          ['x', '#', 'o', '#', 'o', '#', ' ', '#', ' '],
          ['#', 'o', '#', 'x', '#', ' ', '#', ' ', '#'],
          [' ', '#', 'x', '#', 'o', '#', 'x', '#', ' '],
          ['#', 'o', '#', 'o', '#', 'o', '#', ' ', '#'],
          ['o', '#', 'o', '#', 'o', '#', 'o', '#', ' '],
          ['#', 'x', '#', 'x', '#', 'x', '#', 'x', '#'],
          ['o', '#', 'o', '#', ' x', '#', 'x', '#', ' '],
          ['#', 'x', '#', 'o', '#', 'o', '#', ' ', '#']]
    TEST('no winner', None, check_winner(board))
    print()
    
def make_move_TEST():
    print('Start make_move_TEST')
    player = 'x'
    
    
    player_input = '1B'
    TEST('legal move', True, make_move(player, player_input, board))
    
    
    player_input = '1A'
    TEST('legal move', False, make_move(player, player_input, board))
    
    
    player_input = 'A1'
    TEST('illegal move', False, make_move(player, player_input, board))
    
    
    player_input = ''
    TEST('illegal move', False, make_move(player, player_input, board))

    
    


check_winner_TEST()
make_move_TEST()
