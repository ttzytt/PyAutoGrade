




from project_connect_four_functions import *

print('Welcome to 3D connect 4!')
print('There are 4 layers with 4 rows and columns each.')
print('Your move should be in the format of layer-column-row. ex. WA1')
print('The layers are W, X, Y, and Z.')
print('The columns are A, B, C, D.')
print('The rows are 1, 2, 3, 4.')
print('After every move, you will have a chance to rotate one of the layer clockwise 90 degrees.')
print('You will be asked if you want to rotate, which layer you want to rotate, and how many times.')
print('Always capitalize the layer.')
print('ex. yes, W, 2')
print('Make sure to use proper format!')
print('Have Fun!')

board = [ [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ], [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ] ]

W = board[0]
X = board[1]
Y = board[2]
Z = board[3]

count_moves = 0

player = 'x'


while find_winner(board) == None and count_moves < 64: 
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    draw_board(board)
    want_to_rotate = input('Do you want to rotate?')
    print()
    if want_to_rotate == 'yes' or want_to_rotate == 'Yes':
                                                            
        layer = input('Which layer do you want to rotate?')
        print()
        times = input('How many times do you want to rotate?')
        print()
        success_rotate = rotate_layer(layer, times, board)
        while not success_rotate:
            print('That is not a valid move.')
            print()
            layer = input('Which layer do you want to rotate?')
            print()
            times = input('How many times do you want to rotate?')
            print()
            success_rotate = rotate_layer(layer, times, board)
    player = next_player(player)




draw_board(board)
if count_moves == 64:
    print()
    print('Its a tie!')
else:
    print()
    print('The ' + find_winner(board) + ' player wins!')
