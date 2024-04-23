



from pente_functions import *


print('THESE ARE INSTRUCTIONS!! PLEASE READ EVERY LINE WITH PURPOSE!!')
print()
print('This is a Pente game.')
print('The goal of Pente is to connect 5 of your pieces in a row.')
print()
print('You can capture and delete opposing pieces in 2 patterns:')
print('1.')
print('O   #   #   O')
print('In this case, the 2 # pieces would be captured and instantly deleted.')
print()
print('For example, if an O piece is placed on the ·,'
      + ' this is what would happen:')
print('O   #   #   ·   --->   O           O')
print()
print('This can be diagonal, horizontal, or vertical.')
print('However, if you make a move that would cause your'
      + ' own pieces to be captured in this')
print('pattern, it does not count and a capture is not triggered.')
print()
print('It is possible to make more than 1 capture in 1 move with this pattern')
print()
print('2.')
print('O           #               #           O')
print()
print('        #                       #')
print('                   or')
print('    #                               #')
print()
print('#           O               O           #')
print('In this case, the 4 # pieces would be deleted.')
print('In order for a capture, this pattern must be completely unobstructed ' +
      '(no other pieces in between besides those in the pattern.)')
print('If, at any point, this pattern occurs on the board, a capture will' +
      ' be triggered. This means you can capture yourself with this pattern.')
print()
print('It is possible to make more than 1 capture in 1 move ' +
      'with this pattern unless the patterns are overlapping like this:')
print('O           #           O')
print()
print('        #       #')
print()
print('    #               #')
print()
print('#           O           #')
print()
print('An example of a valid move is 1 A.')
      


row = []
board = []
for j in range(19):
    row = ['·'] * 19
    board.append(row)

player = 'O'
winner = None
move_counter = 0 


while winner == None and move_counter < 361:
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board) 
    while not success: 
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    winner = find_winner_2(board, next_move)
    find_first_capture(board, next_move, player) 
    find_second_capture(board) 
    player = next_player(player)
    move_counter += 1
    

draw_board(board)
print()
if move_counter == 361: 
    print("It's a tie!")
else:
    print('The ' + winner + ' player wins!')

