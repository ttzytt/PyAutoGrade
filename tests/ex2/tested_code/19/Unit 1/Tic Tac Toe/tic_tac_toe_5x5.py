

from tic_tac_toe_functions_rewrite import *


board = [[' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]


board_points = [[3, 3, 3, 3, 3],
                [3, 2, 1, 2, 3],
                [3, 1, 1, 1, 3],
                [3, 2, 1, 2, 3],
                [3, 3, 3, 3, 3]]


current_player = 'x'


player_scores = {'x': 0, 'o': 0}


while True:
    
    draw_board(board)

    
    next_move = get_move(current_player)
    
    
    while not make_move(current_player, next_move, board):
        next_move = get_move(current_player)
    
    
    current_score = calculate_score(board, board_points, current_player)
    earned_score_with_this_move = current_score - player_scores[current_player]
    player_scores[current_player] = current_score
    
    
    print(f'Player {current_player} earns {earned_score_with_this_move} point(s) with this move, current score is {current_score}.')

    
    if is_board_full(board):
        draw_board(board)
        print('The game ends!')
        break

    
    current_player =  next_player(current_player)



print('Final Scores:')
print(f'Player x: {player_scores["x"]} points')
print(f'Player o: {player_scores["o"]} points')
if player_scores["x"]>player_scores["o"]:
    print('Final Result: Player x wins!')
else:
    print('Final Result: Player y wins!')
