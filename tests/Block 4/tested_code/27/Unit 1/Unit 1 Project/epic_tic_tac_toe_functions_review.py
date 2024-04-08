






def print_rules():
    print("You are playing a highly intelligent game -- 9*9 tic tac toe.")
    print("There is going to be a master board which is sized 3*3,")
    print('To win the game, you have to win in the master board')
    print("if you want to put anything on it, you would first win the corresponding game in the 3*3*3 secondary game.")
    print(
        "Each player have 3 times to change other player's move, if one player wins a secondary game or if it's a tie")
    print("no one can change the moves in that secondary game")
    print('It is not possible to take back moves')
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




def draw_row(row,row_number):
    print(str(row_number) + ' │ '
          + str(row[0]) + ' │ '
          + str(row[1]) + ' │ '
          + str(row[2]) + ' │'
          + '│ ' + str(row[3]) + ' │ '
          + str(row[4]) + ' │ '
          + str(row[5]) + ' │'
          + '│ ' + str(row[6]) + ' │ '
          + str(row[7]) + ' │ '
          + str(row[8]) + ' │ ')




def draw_board(board):
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(board[0][0] + board[1][0] + board[2][0],1)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[0][1] + board[1][1] + board[2][1],2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[0][2] + board[1][2] + board[2][2],3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(board[3][0] + board[4][0] + board[5][0],1)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[3][1] + board[4][1] + board[5][1],2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[3][2] + board[4][2] + board[5][2],3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(board[6][0] + board[7][0] + board[8][0],1)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[6][1] + board[7][1] + board[8][1],2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(board[6][2] + board[7][2] + board[8][2],3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('    A   B   C    A   B   C    A   B   C  ')




def draw_row_1(row_1, row_number_1):
    print(str(row_number_1) + ' │ '
          + str(row_1[0]) + ' │ '
          + str(row_1[1]) + ' │ '
          + str(row_1[2]) + ' │ ')



def draw_board_1(board_2):
    print('  ┌───┬───┬───┐ ')
    draw_row_1(board_2[0][0] + board_2[0][1] + board_2[0][2], 1)
    print('  ├───┼───┼───┤ ')
    draw_row_1(board_2[1][0] + board_2[1][1] + board_2[1][2], 2)
    print('  ├───┼───┼───┤ ')
    draw_row_1(board_2[2][0] + board_2[2][1] + board_2[2][2], 3)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')
    print()





def find_winner(board, board_index, board_2):
    
    m = 0
    n = 'a'
    
    
    while board_index<9:
        m = 0
        n = 'a'
        while m<3:
            
            if m == 0:
                n = 'x'
            if m == 1:
                n = 'o'
            if m == 2:
                n = 'a'
                if((board[board_index][0][0] == 'o' or board[board_index][0][0] == 'x') 
						and (board[board_index][1][0] == 'o' or board[board_index][1][0] == 'x') 
						and (board[board_index][2][0] == 'o' or board[board_index][2][0] == 'x')
						and (board[board_index][0][1] == 'o' or board[board_index][0][1] == 'x') 
						and (board[board_index][1][1] == 'o' or board[board_index][1][1] == 'x') 
						and(board[board_index][2][1] == 'o' or board[board_index][2][1] == 'x')
						and (board[board_index][0][2] == 'o' or board[board_index][0][2] == 'x') 
						and (board[board_index][1][2] == 'o' or board[board_index][1][2] == 'x') 
						and (board[board_index][2][2] == 'o' or board[board_index][2][2] == 'x') ):
                    for j in range(9):
                
                
                        board[board_index][(j // 3)][(j % 3)] = ("D")
                    board_2[(board_index // 3)][(board_index % 3)] = ['d']

            if ((board[board_index][0][0] == board[board_index][1][0]== board[board_index][2][0]== n )
                    or (board [board_index][0][1] == board[board_index][1][1]== board[board_index][2][1]== n)
                    or (board [board_index][0][2] == board[board_index][1][2]== board[board_index][2][2]== n)
                    or (board [board_index][0][0] == board[board_index][0][1]== board[board_index][0][2]== n)
                    or (board [board_index][1][0] == board[board_index][1][1]== board[board_index][1][2]== n)
                    or (board [board_index][2][0] == board[board_index][2][1]== board[board_index][2][2]== n)
                    or (board [board_index][0][0] == board[board_index][1][1]== board[board_index][2][2]== n)
                    or (board [board_index][0][2] == board[board_index][1][1]== board[board_index][2][0]== n)):

                for j in range(9):
                
                
                    board[board_index][(j // 3)][(j % 3)] = (n.capitalize())
                board_2[(board_index // 3)][(board_index % 3)] = [n]
            m += 1
        board_index += 1



def find_master_winner(board_2):
    
    
    
    
    m = 0
    n = 'a'
    while m < 3:
        if m == 0:
            n = 'x'
        if m == 1:
            n = 'o'
        if m == 2:
            if((board_2[0][0] != [' '])
                    and (board_2[1][0] != [' '])
                    and (board_2[2][0] != [' '])
                    and (board_2[0][1] != [' '])
                    and (board_2[1][1] != [' '])
                    and (board_2[2][1] != [' '])
                    and (board_2[0][2] != [' '])
                    and (board_2[1][2] != [' '])
                    and (board_2[2][2] != [' '])):
                return 'd'

        if ((board_2 [0][0] == board_2[1][0]==board_2[2][0]== [n])
                or (board_2 [0][1] == board_2[1][1]== board_2[2][1]== [n])
                or (board_2 [0][2] == board_2[1][2]== board_2[2][2]== [n])
                or (board_2 [0][0] == board_2[0][1]== board_2[0][2]== [n])
                or (board_2 [1][0] == board_2[1][1]== board_2[1][2]== [n])
                or (board_2 [2][0] == board_2[2][1]== board_2[2][2]== [n])
                or (board_2 [0][0] == board_2[1][1]== board_2[2][2]== [n])
                or (board_2 [0][2] == board_2[1][1]== board_2[2][0]== [n])):
            return n
        m += 1



def get_move(player):
    return input(player + ' player, chose your move: ')







def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'


def make_move(player, move, board, changes_left):
    
    if len(move) != 3:
        ret = 1
        return False
    if (move[0] != '1' and move[0] != '2' and move[0] != '3' 
			and move[0] != '4' and move[0] != '5' and move[0] != '6' 
			and move[0] != '7' and move[0] != '8' and move[0] != '9'):
        ret = 1
        return False
    if move[1] != '1' and move[1] != '2' and move[1] != '3':
        ret = 1
        return False

    if move[2] != 'A' and move[2] != 'B' and move[2] != 'C':
        ret = 1
        return False


    boards = int(move[0]) - 1
    row = int(move[1]) - 1

    column = ord(move[2]) - ord('A')

    
    
    if board[boards][row][column] != ' ':

        
        if ((board[boards][row][column] ==  'X') or (board[boards][row][column] ==  'X')):
            print()
            print("You can't change these")
            return False
        if ((board[boards][row][column] ==  'O') or (board[boards][row][column] ==  'O')):
            print()
            print("You can't change these")
            return False


        
        if ((board[boards][row][column] ==  'x') and (player == 'o') and (changes_left['o'] > 0)):
            board[boards][row][column] = player
            changes_left['o'] -= 1
            print()
            print("Your chance to change player_x's move is:", changes_left['o'])
            
            return True
        if ((board[boards][row][column] ==  'o') and (player == 'x') and (changes_left['x'] > 0)):
            board[boards][row][column] = player
            changes_left['x'] -= 1
            print()
            print("Your chance to change player_o's move is:", changes_left['x'])
            return True


        
        
        
        if ((board[boards][row][column] ==  'o') and (player == 'x') and (changes_left['o'] <= 0)):
            print()
            print("You have no chance to change moves")
            return False
        if ((board[boards][row][column] ==  'x') and (player == 'o') and (changes_left['x'] <= 0)):
            print()
            print("You have no chance to change moves")
            return False

        
        else:
            return False


    
    
    else:
        board[boards][row][column] = player
        return True




