


from Unit_1_Project_functions import *


print(" This is a 6 by 6 tic tac toe game. The first player that has 5 connected would win.")
print(" After each move, each player must choose a 3 by 3 square to spin 90 degrees clockwise"
      " by inputing the spinning center. Wish you players good luck.")


board = [ [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0] ]
player = 'o'
count = 1
winner = None


while count < 37 and winner == None:
    draw_board(board)
    
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    draw_board(board)

    
    next_spin = get_spin(player)
    success = make_spin(player, next_spin, board)
    while not success:
        print('That is not a valid move.')
        next_spin = get_spin(player)
        success = make_spin(player, next_spin, board)

    player = next_player(player)
    winner = find_winner(board)
    count = count + 1
    


draw_board(board)
print()
if winner == None:
    print("You tied.")
else:
    print('The winner is player ' + str(winner) + '!')


