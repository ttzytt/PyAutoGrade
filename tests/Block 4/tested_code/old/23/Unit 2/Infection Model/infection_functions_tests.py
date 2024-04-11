


from infection_functions import *

def TEST(expected_result, actual_result):
    if actual_result == expected_result:
        print('pass')
    else: 
        print('FAIL')
        print('Expected result: ', expected_result)
        print('Actual result: ', actual_result)

def infected_neighbors_TEST():
    board = [ [1, 0, 0, 1],
              [0, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 1, 0]]
    
    TEST(1, infected_neighbors(1, 1, board))
    TEST(4, infected_neighbors(2, 1, board))
    TEST(2, infected_neighbors(2, 2, board))

def infection_simulation_TEST():

    
    board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    expected_board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    actual_board = infection_simulation(1, 1, board, 1)
    TEST(expected_board, actual_board)

    
    board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    expected_board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],   
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    actual_board = infection_simulation(1, 1, board, 1)
    TEST(expected_board, actual_board)

    
    

infected_neighbors_TEST()
infection_simulation_TEST()


              
    