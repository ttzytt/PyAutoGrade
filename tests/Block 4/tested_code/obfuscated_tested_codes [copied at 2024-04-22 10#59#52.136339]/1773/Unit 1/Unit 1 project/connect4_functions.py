







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
    
    for i_r in range(7):
        draw_row(grid[i_r], i_r)
        print('  ', end='')
        for i_c in range(6):
            print(' ___', end='')
        print(' ___')
            
    print('    A   B   C   D   E   F   G  ')






def get_move(player):
    return input(player + ' player, chose your move: ')

def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

def make_move(player, next_move, grid):
    
    if ():
        return False

    column = ord(move[1]) - ord('A')
    
    
    








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)
