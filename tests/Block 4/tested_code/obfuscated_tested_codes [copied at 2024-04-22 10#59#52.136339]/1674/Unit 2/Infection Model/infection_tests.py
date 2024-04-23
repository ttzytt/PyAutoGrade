
from infection_functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)



def count_infected(board):
    total_infected = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                total_infected += 1
    return total_infected

def test_create_infection():
    empty_board = [[' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    create_infection(empty_board, 5)
    infected_count = count_infected(empty_board)
    TEST('create_infection: Correct number of infected people', 5, infected_count)

def test_heal_probability():
    empty_board = [[' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    rows = len(empty_board)
    cols = len(empty_board[0])
    num_of_infected = 0

  
    while num_of_infected < num_infected:
        row = random.randint(0, rows - 2)
        col = random.randint(0, cols - 2)
        if empty_board[row][col] == ' ':
            empty_board[row][col] = 'X'
    before_healing = count_infected(empty_board)
    healed_board = heal_probability(empty_board)
    after_healing = count_infected(healed_board)
    TEST('heal_probability: Number of infected people decreased after healing', True, after_healing < before_healing)

def test_count_infected():
   empty_board = [[' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
   rows = len(empty_board)
   cols = len(empty_board[0])
   num_of_infected = 0

  
   while num_of_infected < num_infected:
        row = random.randint(0, rows - 2)
        col = random.randint(0, cols - 2)
        if empty_board[row][col] == ' ':
            empty_board[row][col] = 'X'
            infected_count = count_infected(board)
            actual_count = 0
   for row in board:
        for cell in row:
            if cell == 'X':
                actual_count += 1
   TEST('count_infected: Count matches actual infected count', actual_count, infected_count)

def test_infect_probability():
      empty_board = [[' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    rows = len(empty_board)
    cols = len(empty_board[0])
    num_of_infected = 0

  
    while num_of_infected < num_infected:
        row = random.randint(0, rows - 2)
        col = random.randint(0, cols - 2)
        if empty_board[row][col] == ' ':
            empty_board[row][col] = 'X'
    before_infecting = count_infected(board)
    infected_board = infect_probability(board, board)
    after_infecting = count_infected(infected_board)
    TEST('infect_probability: Number of infected people increased after infecting', True, after_infecting > before_infecting)

def test_is_board_full():
   board = [['X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],   
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],        
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],                    
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],        
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],        
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],        
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],       
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'],        
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    TEST('is_board_full: Full board detection', True, is_board_full(full_board))
    empty_board = [[' ' for _ in range(10)] for _ in range(10)]
    TEST('is_board_full: Empty board detection', False, is_board_full(empty_board))


test_create_infection()
test_heal_probability()
test_count_infected()
test_infect_probability()
test_is_board_full()
    

test_create_infection()
test_heal_probability()
test_count_infected()
test_infect_probability()
test_is_board_full()

