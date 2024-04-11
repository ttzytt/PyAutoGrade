




from infection_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)



def num_neighbors_different_TEST():
    print('Start num_neighbors_different_TEST')
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
            [' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' '],
            ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
            [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ']]
    
    TEST('In the Middle Infect', 3, num_neighbors_different(board, 3, 2))
    TEST('In the Middle Heal', 2, num_neighbors_different(board, 3, 3))
    TEST('In the Middle None', 0, num_neighbors_different(board, 7, 1))
    TEST('On the Top Edge', 2, num_neighbors_different(board, 0, 6))
    TEST('On the Bottom Edge', 2, num_neighbors_different(board, 9, 3))
    TEST('On the Left Edge', 3, num_neighbors_different(board, 4, 0))
    TEST('On the Right Edge', 2, num_neighbors_different(board, 4, 9))
    TEST('Diagonal Not Count', 0, num_neighbors_different(board, 4, 5))
    print('End num_neighbors_different_TEST')
    print()


def change_state_TEST():
    print('Start change_state_TEST')
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
             [' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    changing_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
                      [' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x'],
                      [' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', ' '],
                      [' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    TEST('Propagating Properly', None, change_state(board, changing_board, 1, 1))
    
    TEST('Board is Correct', expected_board, changing_board)





num_neighbors_different_TEST()
change_state_TEST()
