







import random
random.seed


def create_healthy_board():
    board = []
    for i in range(12):
        board.append([])
    for i in range(12):
        for ii in range(12):
            board[i].append('·')

    return board




def create_starting_board(num_infected):
    board = create_healthy_board()
    infected_people = 0
    while (infected_people < num_infected):
        row = random.randint(1,10)
        column = random.randint(1,10)
        if (board[row][column] != 'x'):
            infected_people += 1
            board[row][column] = 'x'

    return board




def create_board_of_infections(board):
    infected_near = []
    for i in range(10):
        infected_near.append([])
    for row in range(1,11):
        for column in range(1,11):
            if(board[row][column] == 'x'):
                infected_near[row-1].append(-1)
            else:
                count = 0
                if(board[row + 1][column] == 'x'):
                    count += 1
                if(board[row - 1][column] == 'x'):
                    count += 1
                if(board[row][column + 1] == 'x'):
                    count += 1
                if(board[row][column- 1] == 'x'):
                    count += 1
                infected_near[row - 1].append(count)
                
    return infected_near
                







def infect_the_healthy(infection_probability, board, infection_board):
    for row in range(0, 10):
        for column in range(0,10):
            if(infection_board[row][column] != -1):
                sick_or_not = random.randint(0, 100)
                if (sick_or_not < infection_probability * infection_board[row][column]):
                    board[row + 1][column + 1] = 'x'
            
            


def heal_the_infected(healing_probability, board, infection_board):
    for row in range(0,10):
        for column in range(0,10):
            if (infection_board[row][column] == -1):
                healed_or_no = random.randint(0,100)
                if (healed_or_no < healing_probability):
                    board[row + 1][column + 1] = '·'



def print_board(board):
    for row in range(1,11):
        for column in range(1,11):
            print(board[row][column], end = ' ')
        print()



    






