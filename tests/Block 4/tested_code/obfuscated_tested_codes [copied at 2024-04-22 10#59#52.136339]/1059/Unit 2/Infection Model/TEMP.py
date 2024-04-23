import random
random.seed()

    
board = []
board_length = 5
heal = 0
infect = 0
board_copy = []
infected_row = 0
infected_column = 0
board_infected_count =[]

def make_board(board, board_length, board_copy, board_infected_count):
    for row in range (board_length):
        board.append([])
    for row in range (board_length):
        for column in range(board_length):
            board[row].append(0)
    
    for row in range (board_length):
        board_copy.append([])
    for row in range (board_length):
        for column in range(board_length):
            board_copy[row].append(0)

    for row in range (board_length):
        board_infected_count.append([])
    for row in range (board_length):
        for column in range(board_length):
            board_infected_count[row].append(0)


make_board(board, board_length, board_copy, board_infected_count)
print(board)


board_copy =   [[1, 1, 1, 1, 1], 
				[1, 1, 1, 1, 1], 
				[1, 1, 1, 1, 1], 
				[1, 1, 1, 1, 1], 
				[1, 1, 1, 1, 1]]
