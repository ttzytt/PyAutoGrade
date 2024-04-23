






from connect4_function import *



'''
def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' | '
          + row[4] + ' | '
          + row[5] + ' | '
          + row[6] + ' | ')

def draw_grid(grid):
    print('                           ')
    draw_row(grid[0], 1)
    print('                           ')
    draw_row(grid[1], 2)
    print('                           ')
    draw_row(grid[2], 3)
    print('                           ')
    print('A   B   C   D   E   F   G  ')
    
def get_move(player):
    return input(player + ' player, chose your move: ')

def next_player(player):
    if player == 'x':
        return 'o'
    else:  # player == 'o'
        return 'x'

def make_move(player, next_move, grid):
    # Check that next mover is a between g
    if ():
        return False
'''
    
    
    
    

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
