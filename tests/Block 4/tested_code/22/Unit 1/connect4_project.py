






from connect4_function import *




    
    
    
    

grid = [ [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '█', ' ', '█', ' ', '█', ' '] ] 

player = 'x'


while True:
    draw_grid(grid)
    next_move = get_move(player)
    success = make_move(player, next_move, grid)
    while not success:
        print('That aint a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, grid)
    player = next_player(player)





def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)
