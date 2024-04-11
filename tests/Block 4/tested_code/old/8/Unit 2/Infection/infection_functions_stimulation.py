


from infection_functions import *

board = [['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '·'],
         ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·']]
sick_probability = int(input("What do you want the probability of contracting the disease to be? "))
heal_probability = int(input("What do you want the probability of healing to be? "))


make_sick(sick_probability, board)
count = 0
draw_board(board)
        
while existing_regular(board) and existing_sick(board):
    prob_board = probability_board(sick_probability, heal_probability, board)
    switch_board(prob_board, board)
    count += 1

draw_board(board)
if not existing_regular(board):
    print("Everyone is sick after " + str(count) + " rounds")
else:
    print("Everyone is healed after " + str(count) + " rounds")
