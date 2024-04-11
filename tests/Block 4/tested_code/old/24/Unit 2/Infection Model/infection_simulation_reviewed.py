

from infection_functions import*













infection_probability = 15
healing_probability = 20
board = create_starting_board(20)
print('---Initial Start---')
print_board(board)
times = 50



for i in range(5, times + 1, 5):
    print()
    print('-------Day ' + str(i) + '-------')
    infection_board = create_board_of_infections(board)
    infect_the_healthy(infection_probability, board, infection_board)
    heal_the_infected(healing_probability, board, infection_board)
    print_board(board)

