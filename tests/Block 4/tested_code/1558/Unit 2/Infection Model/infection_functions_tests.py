



from infection_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)



def count_infected_neighbors_TEST():
    
    board = [['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', 'x', '·', '·', '·', '·', '·', '·', '·'],
    ['·', 'x', 'x', '·', '·', '·', 'x', '·', '·', '·'],
    ['·', 'x', 'x', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', 'x', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', 'x', '·'],
    ['·', '·', 'x', 'x', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', 'x', '·', '·', '·', 'x', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·']]

    
    TEST('count infected neighbors', 2, count_infected_neighbors(board, 3, 1))




def update_board_infect_TEST():
    size = 10
    infection_probability = 1.0  
    heal_probability = 1.0  
    board = [['·' for _ in range(size)] for _ in range(size)] 
    updated_board = update_board(board, infection_probability, heal_probability)

    
    expected_result = [['x' for _ in range(size)] for _ in range(size)]
    TEST('Update board, infected probability', expected_result, updated_board)


def update_board_heal_TEST():
    size = 10
    infection_probability = 1.0  
    heal_probability = 1.0  
    board = [['x' for _ in range(size)] for _ in range(size)] 
    updated_board = update_board(board, infection_probability, heal_probability)

    
    expected_result = [['·' for _ in range(size)] for _ in range(size)]
    TEST('Update board, heal probability', expected_result, updated_board)


count_infected_neighbors_TEST()
update_board_infect_TEST()
update_board_heal_TEST()





















