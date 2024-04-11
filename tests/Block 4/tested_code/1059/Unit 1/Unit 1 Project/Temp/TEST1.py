from tic_tac_toe_functions_1 import *

board = [[['x', 'o', 'x'],
          ['x', 'o', 'o'],
          [' ', 'x', 'o']],

         [['x', 'o', 'x'],
          ['o', 'x', 'x'],
          ['o', 'x', 'o']],

         [['x', 'o', 'x'],
          ['o', 'x', 'o'],
          ['o', 'x', 'x']],

         [['x', 'x', 'o'],
          ['o', 'o', 'x'],
          ['x', 'o', 'x']],

         [['x', 'x', 'o'],
          ['o', 'o', 'x'],
          ['x', 'x', 'o']],

         [['x', 'o', 'x'],
          ['o', 'x', 'x'],
          ['o', 'x', 'o']],

         [['x', 'o', 'o'],
          ['o', 'x', 'x'],
          ['o', 'x', 'o']],

         [['x', 'o', 'o'],
          ['o', 'x', 'x'],
          ['o', 'x', 'o']],

         [['x', 'o', 'o'],
          ['o', 'x', 'x'],
          ['o', ' ', 'o']]]

board_2 = [[[' '], [' '], [' ']],
           [[' '], [' '], [' ']],
           [[' '], [' '], [' ']]]

player = 'x'
count_o = 3
count_x = 3
changes_left = {'o': 3, 'x': 3}  
changes_left['o']
changes_left['x']

print("You are playing a highly intelligent game -- 9*9 tic tac toe.")
print("There is going to be a master board which is sized 3*3,")
print('To win the game, you have to win in the master board')
print("if you want to put anything on it, you would first win the corresponding game in the 3*3*3 secondary game.")
print("Each player have 3 times to change other player's move, if one player wins a secondary game")
print("no one can change the moves in that secondary game")
print("The program will first print the master board")
print()
print()
print('      ┌───┬───┬───┐ ')
print('    1 │   │   │   │ ')
print('      ├───┼───┼───┤ ')
print("    2 │   │   │   │ ")
print("      ├───┼───┼───┤")
print("    3 │   │   │   │ ")
print("      └───┴───┴───┘ ")
print('        A   B   C')
print()
print()
print("If you want to make a move in the secondary board, you first have to enter the board number, from 1 to 9")
print()

print('      ┌───┬───┬───┐ ')
print('    1 │ 1 │ 2 │ 3 │ ')
print('      ├───┼───┼───┤ ')
print("    2 │ 4 │ 5 │ 6 │ ")
print("      ├───┼───┼───┤")
print("    3 │ 7 │ 8 │ 9 │ ")
print("      └───┴───┴───┘ ")
print('        A   B   C')
print('After that, you should enter the row number and the column,')
print('The row number and the column number is on the left and bottom of the secondary main board')
print("You may enter something like this, to put something in the top left of the secondary main board, enter 11A")
print("The game will begin")
print()
print()
print()
print()
print()
print()
print()
print()

z = 0
while True:
    

    print()
    print()
    print()
    draw_board(board)
    draw_board_1(board_2)
    print()
    next_move = get_move(player)

    success = make_move(player, next_move, board, changes_left)
    z += 1
    i = 0
    print()
    print()
    find_winner(board, i, board_2)

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






