



from epic_tic_tac_toe_functions import *


board = [[[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ] ,


         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ] ,


         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ],

         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ] ]


board_2= [[ [' '], [' '], [' ']],
          [ [' '], [' '], [' ']],
          [ [' '], [' '], [' ']]]


player = 'x'
count_o = 3  
count_x = 3
changes_left = {'o': 3, 'x': 3}   
changes_left['o']
changes_left['x']


print_rules()

while True:
    
    draw_board_1(board_2)
    print()
    print()
    
    draw_board(board)
    print()
    next_move = get_move(player)
    success = make_move(player, next_move, board, changes_left)
    board_index = 0
    print()
    print()
    find_winner(board, board_index, board_2)


    
    if (find_master_winner(board_2)) == 'x':
        draw_board_1(board_2)
        print()
        print('The x player wins!')
        break
    if (find_master_winner(board_2)) == 'o':
        draw_board_1(board_2)
        print()
        print('The o player wins!')
        break
    if (find_master_winner(board_2)) == 'd':
        draw_board_1(board_2)
        print()
        print('No player wins!')
        break


    
    while not success:
        print()
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board, changes_left)
    player = next_player(player)
