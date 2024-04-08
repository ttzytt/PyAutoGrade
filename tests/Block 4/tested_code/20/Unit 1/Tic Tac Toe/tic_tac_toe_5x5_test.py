

from tic_tac_toe_functions_rewrite import *
from unittest.mock import patch









def TEST(description, expected_result, actual_result):
    print(description, end=': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)





def mock_input(mock_values):
    return lambda prompt: mock_values.pop(0)








def TEST(description, expected_result, actual_result):
    print(description, end=': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)





def draw_row_TEST():
    print('Start draw_row_TEST')
    row = ['x', 'o', ' ', 'x', 'o']
    draw_row(row, 3)  
    print('End draw_row_TEST\n')


def draw_board_TEST():
    print('Start draw_board_TEST')
    board = [['x', 'o', ' ', 'x', ' '],
             ['x', ' ', 'x', 'o', ' '],
             ['x', 'o', ' ', 'x', 'o'],
             [' ', ' ', ' ', 'o', 'x'],
             ['o', 'x', ' ', ' ', 'x']]
    draw_board(board)
    print('End draw_board_TEST\n')


def next_player_TEST():
    print('Start next_player_TEST')
    TEST('Switch from x to o', 'o', next_player('x'))
    TEST('Switch from o to x', 'x', next_player('o'))
    print('End next_player_TEST\n')


def get_move_TEST():
    print('Start get_move_TEST')
    
    input_values = ['1A', '2B', 'invalid', '3C']
    expected_outputs = [(0, 0), (1, 1), None, (2, 2)]

    with patch('builtins.input', side_effect=input_values):
        for i in range(len(input_values)):
            result = get_move('x')
            TEST(f'get_move test {i+1}', expected_outputs[i], result)

    print('End get_move_TEST\n')


def make_move_TEST():
    print('Start make_move_TEST')
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    expected_boards = [
        [['x', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']],
        [['x', 'o', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']],
        [['x', 'o', ' '],
         [' ', ' ', ' '],
         [' ', 'x', ' ']],
        [['x', 'o', ' '],
         [' ', ' ', ' '],
         [' ', 'x', 'o']],
    ]
    with patch('builtins.input', side_effect=['1A', '2B', '3C', '4D']):
        for i in range(4):
            result = make_move('x', (i // 3, i % 3), board)
            TEST(f'make_move test {i+1}', True, result)
            TEST(f'make_move test {i+1}', expected_boards[i], board)

    print('End make_move_TEST\n')


def is_board_full_TEST():
    print('Start is_board_full_TEST')
    
    board_not_full = [['x', ' ', ' ', ' ', 'o'],
                      [' ', 'o', 'o', 'o', 'x'],
                      ['o', 'x', 'x', ' ', 'o'],
                      [' ', 'x', 'x', 'x', 'o'],
                      ['x', 'o', 'o', ' ', 'x']]
    result = is_board_full(board_not_full)
    TEST('board not full', False, result)

    
    board_full = [['x', 'o', 'x', 'o', 'x'],
                  ['o', 'x', 'o', 'o', 'x'],
                  ['x', 'x', 'o', 'o', 'o'],
                  ['o', 'x', 'x', 'o', 'o'],
                  ['x', 'o', 'o', 'x', 'x']]
    result = is_board_full(board_full)
    TEST('board full', True, result)

    print('End is_board_full_TEST\n')


def calculate_score_TEST():
    print('Start calculate_score_TEST')
    board = [['x', 'o', 'x', 'o', 'x'],
             [' ', 'o', 'o', 'o', 'x'],
             ['o', 'x', 'x', ' ', 'o'],
             [' ', 'x', 'x', 'o', 'o'],
             ['x', 'o', 'o', ' ', 'x']]
    board_points = [
        [3, 3, 3, 3, 3],
        [3, 2, 1, 2, 3],
        [3, 1, 1, 1, 3],
        [3, 2, 1, 2, 3],
        [3, 3, 3, 3, 3]
    ]
    result_x = calculate_score(board, board_points, 'x')
    result_o = calculate_score(board, board_points, 'o')
    TEST('calculate_score for player x', 12, result_x)
    TEST('calculate_score for player o', 13, result_o)
    print('End calculate_score_TEST\n')


draw_row_TEST()
draw_board_TEST()
next_player_TEST()
get_move_TEST()
make_move_TEST()
is_board_full_TEST()
calculate_score_TEST()
