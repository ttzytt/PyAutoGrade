



from tic_tac_toe_functions import *


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
player = 'x'


while True:  
    draw_board(board)  
    next_move = get_move(player)  
    success = make_move(player, next_move, board)  

    
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)

    winner = find_winner(board)  
    if winner:
        draw_board(board)  
        print()
        print(f'The {winner} player wins!')
        break  

    if is_board_full(board):
        draw_board(board)  
        print("\nThe game ends in a tie!")
        break  

    player = next_player(player)  




draw_board(board)
