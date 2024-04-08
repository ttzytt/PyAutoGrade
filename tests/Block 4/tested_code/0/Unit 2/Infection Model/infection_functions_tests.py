




from infection_functions import*

def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)

        

def make_board_TEST():
    rows = 3
    columns = 3
    expected_result = [ ['·', '·', '·'],
                        ['·', '·', '·'],
                        ['·', '·', '·'] ]
    TEST('make_board',expected_result, make_board(rows, columns))

def make_players_TEST():
    board = [ ['·', '·', '·'],
              ['·', '·', '·'],
              ['·', '·', '·'] ]
    expected_result = [ ['·', '·', '·'],
                        ['·', '·', '·'],
                        ['·', '·', '·'] ]
    TEST('Make player', expected_result, make_players(board))


def num_infected_neighbors_TEST():

    board = [ ['x', '·', '·'],
              ['·', '·', '·'],
              ['·', '·', '·'] ] 
    TEST('num_infected_neighbors',1, num_infected_neighbors(board, 1, 0))

    board = [ ['x', '·', '·'],
              ['·', 'x', 'x'],
              ['·', '·', '·'] ] 
    TEST('num_infected_neighbors',2, num_infected_neighbors(board, 0, 1))

    board = [ ['x', '·', '·'],
              ['·', 'x', 'x'],
              ['·', '·', '·'] ] 
    TEST('num_infected_neighbors',1, num_infected_neighbors(board, 0, 2))

    board = [ ['x', '·', '·','·','·'],
              ['·', 'x', 'x','·','·'],
              ['·', 'x', '·','x','·'],
              ['·', 'x', 'x','·','·'],
              ['·', '·', '·','·','·']] 
    TEST('num_infected_neighbors',4, num_infected_neighbors(board, 2, 2))



def heal_probability_TEST():
    board = [ ['x', '·', '·'],
              ['·', 'x', 'x'],
              ['·', '·', '·'] ] 
    expected_result = [ [0.2, 0, 0],
                         [0, 0.2, 0.2],
                         [0, 0, 0] ]
    board = [ ['·', '·', '·'],
              ['·', '·', '·'],
              ['·', '·', '·'] ] 
    expected_result = [ [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0] ]


    TEST('heal_probability',expected_result, heal_probability(board))

    board = [ ['x', '·', '·','·','·'],
              ['·', 'x', 'x','·','·'],
              ['·', 'x', '·','x','·'],
              ['·', 'x', 'x','·','·'],
              ['·', '·', '·','·','·']] 
    expected_result = [ [0.2, 0, 0,0,0],
                        [0,0.2 , 0.2,0,0],
                        [0, 0.2, 0,0.2,0],
                        [0, 0.2, 0.2,0,0],
                        [0,0, 0,0,0]] 

    TEST('heal_probability',expected_result, heal_probability(board))
    
def infection_probability_TEST():
    board = [ ['x', '·', '·'],
              ['·', 'x', 'x'],
              ['·', '·', '·'] ] 
    expected_result =[ [0, 0.3, 0.15],
                       [0.3, 0, 0],
                       [0, 0.15, 0.15] ] 
    
    TEST('infected_probability', expected_result, infection_probability(board))
    board = [ ['x', '·', '·','·','·'],
              ['·', 'x', 'x','·','·'],
              ['·', 'x', '·','x','·'],
              ['·', 'x', 'x','·','·'],
              ['·', '·', '·','·','·']] 
    expected_result = [ [0, 0.3,0.15,0,0],
                        [0.3,0 , 0,0.3,0],
                        [0.15, 0, 0.6,0,0.15],
                        [0.15, 0, 0,0.3,0],
                        [0,0.15, 0.15,0,0]]
    TEST('infected_probability', expected_result, infection_probability(board))





    
make_players_TEST()
make_board_TEST()
num_infected_neighbors_TEST()
infection_probability_TEST()    
heal_probability_TEST()
