


from infection_function import *


def TEST(desc, actual_result, predicted_result):
    print(desc, ':')

    if actual_result == predicted_result:
        print('pass')
        print()
    else:
        print('FAIL')
        print('    Expected result:', predicted_result)
        print('    Actual result:', actual_result)
        print()


('''
def TEST_create_grid():
    print()
    print('START_create_grid_TEST')
    print()
    board = []
    TEST('test creating a grid', create_grid(3, 3, board, 0), None)
    TEST('test list change', board, [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])
    ''')


def check_infected_TEST():
    print('START_check_infected_TEST')
    print()

    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    TEST('test num ppl infected', check_infected(board, 2, 2), 2)

    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
    TEST('test num infected', check_infected(board, 1, 1), 1)


def count_infected_TEST():
    print('START_count_infected_TEST')
    print()

    board = [[1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    TEST('make sure outside is not checked', count_infected(board, 3, 3), 4)


def draw_board_TEST():
    print()
    print('START_count_infected_TEST')
    print()

    board = [[1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    TEST('test if draw_board counts infected', draw_board(board, 3, 3), 4)
    

def execute_round_TEST():
    print()
    print('START_execute_round_TEST')
    print()

    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    
    TEST('tests with non-random arguments', execute_round(3, 3, board, 1, 0), [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]])

    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    
    TEST('tests with non-random arguments', execute_round(3, 3, board, 0, 1), [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
         

print('START TESTS')
check_infected_TEST()
count_infected_TEST()
draw_board_TEST()
execute_round_TEST()
