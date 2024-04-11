




import random
random.seed()

from infection_functions import *

board = [] 
board_length = (int(input("Input the board size: ")))+2

heal = 0 
infect = 0 
board_copy =[] 
infected_row = 0 
infected_column = 0
board_infected_count = []

run = 1
make_board(board,board_length,board_copy, board_infected_count)


while (run == 1):
    if ((type(infected_row) == int) and (type (infected_column) == int)):
        infected_row = int(input("Input the row: "))
        infected_column = int(input("Input the column: "))
        setup_board(board,board_length,infected_row,infected_column)
      
        print_board(board,board_length)
        print("Enter 1 to continue, enter anything else to quit setup")
        run = int(input("Do you want to continue: "))
    else:
        print("Enter Valid value")

infect = float(input("Input the infection probability: "))
heal = float(input("Input the heal probability: "))




for runtime in range(10000):
	infecting_neighbor(board, board_length, infect, heal, board_copy)
	count_infected_time(board_length, board, board_infected_count)
	heal_process(board_length, board, board_copy,heal)
	runtime += 1


print_board(board, board_length)
print_infected_board(board_infected_count,board_length)
