def draw_row_layer_one(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')

def draw_row_layer_two(row, row_number):
    print('    ' + str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')

def draw_row_layer_three(row, row_number):
    print('        ' + str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')

def draw_row_layer_four(row, row_number):
    print('            ' + str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')

def draw_board(board):
    print(' Layer W')
    print('  ┌───┬───┬───┬───┐ ')
    draw_row_layer_one(layer_one[0], 1)
    print('  ├───┼───┼───┼───┤ ')
    draw_row_layer_one(layer_one[1], 2)
    print('  ├───┼───┼───┼───┤ ')
    draw_row_layer_one(layer_one[2], 3)
    print('  ├───┼───┼───┼───┤ ')
    draw_row_layer_one(layer_one[3], 4)
    print('  └───┴───┴───┴───┘ ')
    print('    A   B   C   D   ')
    print('     Layer X')
    print('      ┌───┬───┬───┬───┐ ')
    draw_row_layer_two(layer_two[0], 1)
    print('      ├───┼───┼───┼───┤ ')
    draw_row_layer_two(layer_two[1], 2)
    print('      ├───┼───┼───┼───┤ ')
    draw_row_layer_two(layer_two[2], 3)
    print('      ├───┼───┼───┼───┤ ')
    draw_row_layer_two(layer_two[3], 4)
    print('      └───┴───┴───┴───┘ ')
    print('        A   B   C   D   ')
    print('         Layer Y')
    print('          ┌───┬───┬───┬───┐ ')
    draw_row_layer_three(layer_three[0], 1)
    print('          ├───┼───┼───┼───┤ ')
    draw_row_layer_three(layer_three[1], 2)
    print('          ├───┼───┼───┼───┤ ')
    draw_row_layer_three(layer_three[2], 3)
    print('          ├───┼───┼───┼───┤ ')
    draw_row_layer_three(layer_three[3], 4)
    print('          └───┴───┴───┴───┘ ')
    print('            A   B   C   D   ')
    print('             Layer Z')
    print('              ┌───┬───┬───┬───┐ ')
    draw_row_layer_four(layer_four[0], 1)
    print('              ├───┼───┼───┼───┤ ')
    draw_row_layer_four(layer_four[1], 2)
    print('              ├───┼───┼───┼───┤ ')
    draw_row_layer_four(layer_four[2], 3)
    print('              ├───┼───┼───┼───┤ ')
    draw_row_layer_four(layer_four[3], 4)
    print('              └───┴───┴───┴───┘ ')
    print('                A   B   C   D   ')
layer_one = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
layer_two = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
layer_three = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
layer_four = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
board = [[layer_one], [layer_two], [layer_three], [layer_four]]

print(draw_board(board))
