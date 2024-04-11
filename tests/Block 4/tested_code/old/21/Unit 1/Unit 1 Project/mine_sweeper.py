from mine_sweeper_functions import *

print("This is minesweepers. If you've never played, here are the instructions.")
print("You will need to choose a square, number then letter ex: 1A")
print()
print("There will be four randomly placed mines, and when you choose a a square, ")
print("it will tell you how many mines are touching the square you're on or if you're on a mine.")
print("If you are not on a mine, you get +1 point. If you're not on a mine, you get no points for that turn.")
print("The game ends when you finish the board and it will display your points.")
print("Good luck!")





board = [ [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '] ]


num_mines = 4
mines = create_mines(num_mines)
player_1_score, player_2_score = 0, 0

player = 1
previous_moves = []




while not is_board_full(board):
    board = draw_board(board)
    next_move = get_move(player)
    
    success = make_move(player, next_move, board, mines, previous_moves)
    while success != True and success != 'mine':
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board, mines, previous_moves)

    if success != 'mine':
        if player == 2:
            player_2_score += 1
        if player == 1:
            player_1_score += 1
    
    player = next_player(player)
  

draw_board(board)


if is_board_full(board) is True:
    print("End of the game. Player 1 score:", player_1_score, "Player 2 score:", player_2_score
)
   



