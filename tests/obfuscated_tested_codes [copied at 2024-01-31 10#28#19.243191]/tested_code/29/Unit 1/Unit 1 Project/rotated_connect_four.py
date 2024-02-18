





from rotated_connect_four_functions import *



board = [[' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ']]
new_board = [[' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ']]

row_counter = 0
prev_move = 'x'
moves_played = 0
player_input = ' '



while moves_played < 36 and find_winner(board) == 'None':
    
    draw_board(board)

    
    player_input = prompt_move(prev_move, player_input)
    
    while is_move_legal(board, player_input) == False:
        player_input = input('Try again: ')

        

    if is_move_legal(board, player_input) == True:

        
        if player_input == 'rotate':

            n_times_rotate = input("How many 90 degree rotations (up to 3): ")

            
            while not (49 <= ord(n_times_rotate[0]) <= 51 and len(n_times_rotate) == 1):
                n_times_rotate = input('Please enter a positive integer between 1 and 3: ')

            
            for i in range(int(n_times_rotate)):
                
                board = rotate(new_board, board)
                new_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ']]
                draw_board(board)
            board = fall_down(board)

        
        else:
            play_move(board, player_input, prev_move)

    
        if prev_move == 'x':
            prev_move = 'o'
        else:
            prev_move = 'x'

    moves_played += 1


draw_board(board)


if moves_played == 36 and find_winner(board) == 'None':
    print('Tie')
    

else:
    print(find_winner(board) + ' player wins.')
    
