



'''
This program will run a simulation of infection and healing based off of a 10x10 board.  When healthy, the
infection probability is the set probability multiplied by the number of infected neighbors. While infected, the tile
has a chance to become healthy every round.  Even in the round that they turn healthy, the infected can still
infected a healthy individual that round.
'''


from infection_functions import *


board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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


num_trials = int(input('How many rounds do you want to run?'))
num_starting_infected = int(input('How many starting infected?'))
set_infected(num_starting_infected, board)

draw_board(board)


for _ in range(num_trials):
    
    change_state(board, changing_board, .15, .31)
    
    
    board, changing_board = changing_board, board
    draw_board(board)
    
    


draw_board(board)

'''
The corner and edge pieces have a lower chance of being infected.First, the corner and edge pieces have less of
them to be infected so the middle pieces often look as if they have more
infected more times.  This is also supported since corner pieces and edge pieces each have less neighbors then the
middle pieces with 2 and 3 as opposed to 4 normally. This means that intuitively, the maximum chance of infection
for a corner or edge piece is less because the number of neighbors directly impact the rate of being infected.
'''
