



from form_a_square_functions import *

print("Welcome to the game 'form a square'.")
print("Winning condition: form a square or diamons anywhere on the board that looks like this:")
print("┌───┬───┬───┐")
print("│ x │   │ x │") 
print("├───┼───┼───┤")
print("│   │   │   │")
print("├───┼───┼───┤")
print("│ x │   │ x │") 
print("└───┴───┴───┘")
print("Or this:")
print("┌───┬───┬───┐")
print("│ o │   │ o │") 
print("├───┼───┼───┤")
print("│   │   │   │")
print("├───┼───┼───┤")
print("│ o │   │ o │") 
print("└───┴───┴───┘")
print("Or this:")
print("┌───┬───┬───┐")
print("│   │ x │   │") 
print("├───┼───┼───┤")
print("│ x │   │ x │")
print("├───┼───┼───┤")
print("│   │ x │   │") 
print("└───┴───┴───┘")
print("Or this:")
print("┌───┬───┬───┐")
print("│   │ o │   │") 
print("├───┼───┼───┤")
print("│ o │   │ o │")
print("├───┼───┼───┤")
print("│   │ o │   │") 
print("└───┴───┴───┘")
print("If you make a move in the center of the shape that you're forming, you lose immediately.")
print("Example:")
print("┌───┬───┬───┐")
print("│ x │   │ x │") 
print("├───┼───┼───┤")
print("│   │ x │   │")
print("├───┼───┼───┤")
print("│ x │   │ x │") 
print("└───┴───┴───┘")
print()
print("Let's start the game.")




board = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
player = 'x'

steps = 0


while not (find_winner(board) != None or steps > 15):
    
    draw_board(board)

    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    steps += 1



draw_board(board)
print()

if find_winner(board) == 'x':
    print('The x player wins!')
elif find_winner(board) == 'o':
    print('The o player wins!')
else:
    print('This is a tie.')
