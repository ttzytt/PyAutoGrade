





def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ ')
    

def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  └───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F ')


def prompt_move(prev_move, player_input):

    if prev_move == 'x':
        player_input = input("Play your move, 'x' player: ")


    elif prev_move == 'o':
        player_input = input("Play your move, 'o' player: ")
    
    return player_input
    

def is_move_legal(board, player_input):

    
    if player_input == 'rotate':
        return True
    
    
    elif len(player_input) != 2:
        print('WRONG LENGTH')
        return False
    
    
    elif not (ord(player_input[0]) >= 49 and ord(player_input[0]) <= 55):
        print('WRONG FIRST CHARACTER')
        return False
    elif not (ord(player_input[1]) >= 65 and ord(player_input[1]) <= 71):
        print('WRONG SECOND CHARACTER')
        return False
    
    
    elif board[int(player_input[0]) - 1][ord(player_input[1]) - 65] != ' ':
        print('FILLED UP SQUARE')
        return False
    
    
    elif player_input[0] != '6':
        if board[int(player_input[0])][ord(player_input[1]) - 65] == ' ':
            print('NOTHING BELOW')
            return False

    
    return True


def rotate(new_board, board):

    
    new_board[0] = [board[5][0], board[4][0], board[3][0], board[2][0], board[1][0], board[0][0]]
    new_board[1] = [board[5][1], board[4][1], board[3][1], board[2][1], board[1][1], board[0][1]]
    new_board[2] = [board[5][2], board[4][2], board[3][2], board[2][2], board[1][2], board[0][2]]
    new_board[3] = [board[5][3], board[4][3], board[3][3], board[2][3], board[1][3], board[0][3]]
    new_board[4] = [board[5][4], board[4][4], board[3][4], board[2][4], board[1][4], board[0][4]]
    new_board[5] = [board[5][5], board[4][5], board[3][5], board[2][5], board[1][5], board[0][5]]

    
    board = new_board
    new_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],

                 [' ', ' ', ' ', ' ', ' ', ' ']]
    


    return board


def any_blanks(my_list):
    for i in range(len(my_list)):
        if my_list[i] == ' ':
            return True

    return False


def fall_down(board):
    row_counter = 0
    
    for row in range(4, -1, -1):
        for column in range(6):
            
            if any_blanks([board[0][column], board[1][column], board[2][column], board[3][column], board[4][column], board[5][column]]) == True:

                
                if board[row][column] != ' ':
                    row_counter = 0

                    
                    while (row + row_counter) <= 4 and board[row + row_counter + 1][column] == ' ':
                        row_counter +=   1

                if board[row + 1][column] == ' ':
                    
                    board[row + row_counter][column] = board[row][column]
                    board[row][column] = ' '

    return board


def play_move(board, player_input, prev_move):
    if prev_move == 'x':
        board[int(player_input[0]) - 1][ord(player_input[1]) - 65] = 'x'
    elif prev_move == 'o':
        board[int(player_input[0]) - 1][ord(player_input[1]) - 65] = 'o'



def all_equal(my_list):

    if len(my_list) >= 2:

        for i in range(len(my_list) - 1):
            if my_list[i] != my_list[i + 1]:
                return False

        return True
            
    elif len(my_list) == 1:
        return True
    else:
        return False
    

def find_winner(board):

    
    for rows in range(3):
        for columns in range(6):

            if board[rows][columns] != ' ':

                
                my_list = [board[rows][columns], board[rows + 1][columns],\
                           board[rows + 2][columns], board[rows + 3][columns]]
                
                if all_equal(my_list) == True and my_list[0] == 'x':
                   return 'x'
                elif all_equal(my_list) == True and my_list[0] == 'o':
                   return 'o'
            
    
    for columns in range(3):
        for rows in range(6):
            
            if board[rows][columns] != ' ':

                
                my_list = [board[rows][columns], board[rows][columns + 1],\
                           board[rows][columns + 2], board[rows][columns + 3]]
                
                if all_equal(my_list) == True and my_list[0] == 'x':
                   return 'x'
                elif all_equal(my_list) == True and my_list[0] == 'o':
                   return 'o'



    
    for rows in range(3, 6):
        for columns in range(0, 3):
            
            if board[rows][columns] != ' ':

                
                my_list = [board[rows][columns], board[rows - 1][columns + 1], board[rows - 2][columns + 2], board[rows - 3][columns + 3]]
            
                if all_equal(my_list) == True and my_list[0] == 'x':
                   return 'x'
                elif all_equal(my_list) == True and my_list[0] == 'o':
                   return 'o'               
                
    
    for rows in range(0, 3):
        for columns in range(0, 3):
            
            if board[rows][columns] != ' ':

                
                my_list = [board[rows][columns], board[rows + 1][columns + 1], board[rows + 2][columns + 2], board[rows + 3][columns + 3]]
            
                if all_equal(my_list) == True and my_list[0] == 'x':
                   return 'x'
                elif all_equal(my_list) == True and my_list[0] == 'o':
                   return 'o'               
    
    return 'None'
