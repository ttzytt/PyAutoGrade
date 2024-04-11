




import random

random.seed

from Poker_squares_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)







def make_move_TEST():
    print('Start make_move_TEST: ')

    
    board = [ ['3', ' ', '1', '7', '9'],
              ['2', '7', '2', '8', '4'],
              ['9', ' ', '8', '5', '2'],
              [' ', '5', '1', ' ', '4'],
              ['2', '3', '5', ' ', '2'] ]
    card = 5
    TEST('accept legal move', True, make_move('1B', card, board))
    expected_board = [ ['3', '5', '1', '7', '9'],
                       ['2', '7', '2', '8', '4'],
                       ['9', ' ', '8', '5', '2'],
                       [' ', '5', '1', ' ', '4'],
                       ['2', '3', '5', ' ', '2'] ]
    TEST('make legal move', expected_board, board)

    
    board = [ ['3', ' ', '1', '7', '9'],
              ['2', '7', '2', '8', '4'],
              ['9', ' ', '8', '5', '2'],
              [' ', '5', '1', ' ', '4'],
              ['2', '3', '5', ' ', '2'] ]
    card = 7
    TEST('accept legal move', True, make_move('4D', card, board))
    expected_board = [ ['3', ' ', '1', '7', '9'],
                       ['2', '7', '2', '8', '4'],
                       ['9', ' ', '8', '5', '2'],
                       [' ', '5', '1', '7', '4'],
                       ['2', '3', '5', ' ', '2'] ]
    TEST('make legal move', expected_board, board)

    
    board = [ [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '] ]
    card = 4
    expected_board = board
    TEST('reject move, wrong case', False, make_move('2a', card, board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, no location', False, make_move('', card, board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, wrong order', False, make_move('A3', card, board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, extra characters', False, make_move('5Aksi', card, board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('1F', card, board))
    TEST('dont change after rejected move', expected_board, board)
    TEST('reject move, off board', False, make_move('0A', card, board))
    TEST('dont change after rejected move', expected_board, board)

    print('End make_move_TEST. ')
    print()
    print()

def logic_of_row_score_TEST():
    print('Start logic_of_row_score_TEST: ')

    
    
    board = [ ['1', '1', '1', '1', '1'],
              ['2', '2', '3', '2', '2'],
              ['6', '4', '6', '6', '4'],
              ['9', '5', '9', '7', '9'],
              ['8', '8', '5', '2', '1'] ]
    TEST('count sum of row score', 63, logic_of_row_score(board))
    print()
    
    
    
    board = [ ['1', '4', '5', '2', '3'],
              ['6', '2', '3', '6', '3'],
              ['7', '4', '5', '6', '4'],
              ['2', '9', '9', '9', '6'],
              ['3', '1', '3', '3', '3'] ]
    TEST('count the sum of row score', 38, logic_of_row_score(board))
    print()
    
    print('End logic_of_row_score_TEST. ')
    print()
    print()
    
def logic_of_column_score_TEST():
    print('Start logic_of_column_score_TEST: ')

    
    
    board = [ ['1', '5', '3', '6', '7'],
              ['1', '2', '8', '9', '2'],
              ['1', '5', '8', '6', '4'],
              ['1', '5', '3', '6', '7'],
              ['1', '5', '8', '2', '1'] ]
    TEST('count the sum of column score', 63, logic_of_column_score(board))
    print()
    
    
    
    board = [ ['7', '5', '3', '9', '9'],
              ['9', '2', '4', '6', '1'],
              ['8', '7', '2', '9', '1'],
              ['5', '7', '3', '2', '1'],
              ['6', '5', '1', '9', '1'] ]
    TEST('count the sum of column score', 38, logic_of_column_score(board))
    print()

    print('End logic_of_column_score_TEST.')
    print()
    




make_move_TEST()
logic_of_row_score_TEST()
logic_of_column_score_TEST()


