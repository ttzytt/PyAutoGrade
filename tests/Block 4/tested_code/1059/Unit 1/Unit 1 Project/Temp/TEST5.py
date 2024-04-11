





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
    mlist1 = board[0][0] + board[1][0] + board[2][0]
    mlist2 = board[0][1] + board[1][1] + board[2][1]
    mlist3 = board[0][2] + board[1][2] + board[2][2]
    mlist4 = board[3][0] + board[4][0] + board[5][0]
    mlist5 = board[3][1] + board[4][1] + board[5][1]
    mlist6 = board[3][2] + board[4][2] + board[5][2]
    mlist7 = board[6][0] + board[7][0] + board[8][0]
    mlist8 = board[6][1] + board[7][1] + board[8][1]
    mlist9 = board[6][2] + board[7][2] + board[8][2]
    







    
    
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(mlist1,1)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist2,2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist3,3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(mlist4,1)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist5,2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist6,3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('  ┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐ ')
    draw_row(mlist7,1)  
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist8,2)
    print('  ├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤ ')
    draw_row(mlist9,3)
    print('  └───┴───┴───┘└───┴───┴───┘└───┴───┴───┘ ')
    print('    A   B   C    A   B   C    A   B   C  ')


def find_winner(board, i, board_2):
    while i<9:

        if ((board[i][0][0] == board[i][1][0]== board[i][2][0]== 'x' )or (board [i][0][1] == board[i][1][1]== board[i][2][1]== 'x')
                or (board [i][0][2] == board[i][1][2]== board[i][2][2]== 'x')or (board [i][0][0] == board[i][0][1]== board[i][0][2]== 'x')
                or (board [i][1][0] == board[i][1][1]== board[i][1][2]== 'x') or (board [i][2][0] == board[i][2][1]== board[i][2][2]== 'x')
                or (board [i][0][0] == board[i][1][1]== board[i][2][2]== 'x') or (board [i][0][2] == board[i][1][1]== board[i][2][0]== 'x')):
            ret_1 = 20 + i
            if i == 0:
                board_2[0][0] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 1:
                board_2[0][1] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 2:
                board_2[0][2] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 3:
                board_2[1][0] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 4:
                board_2[1][1] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 5:
                board_2[1][2] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 6:
                board_2[2][0] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 7:
                board_2[2][1] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'
            if i == 8:
                board_2[2][2] = "['x']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'X'



        if (board[i][0][0] == board[i][1][0]== board[i][2][0]== 'o' or board [i][0][1] == board[i][1][1]== board[i][2][1]== 'o' or board [i][0][2] == board[i][1][2]== board[i][2][2]== 'o' or board [i][0][0] == board[i][0][1]== board[i][0][2]== 'o' or board [i][1][0] == board[i][1][1]== board[i][1][2]== 'o' or board [i][2][0] == board[i][2][1]== board[i][2][2]== 'o' or board [i][0][0] == board[i][1][1]== board[i][2][2]== 'o' or board [i][0][2] == board[i][1][1]== board[i][2][0]== 'o'):
            ret_1 = 30 + i
            if i == 0:
                board_2[0][0] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 1:
                board_2[0][1] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 2:
                board_2[0][2] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 3:
                board_2[1][0] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 4:
                board_2[1][1] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 5:
                board_2[1][2] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 6:
                board_2[2][0] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 7:
                board_2[2][1] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
            if i == 8:
                board_2[2][2] = "['o']"
                board[i][0][0] = board[i][0][1] = board[i][0][2] = board[i][1][0] = board[i][1][1] = board[i][1][2] = board[i][2][0] = board[i][2][1] = board[i][2][2] = 'O'
        if (board[i][0] == board[i][1] == board[i][2] == ['X', 'X', 'X']):
            if i == 0:
                board_2[0][0] = "['x']"
            if i == 1:
                board_2[0][1] = "['x']"
            if i == 2:
                board_2[0][2] = "['x']"
            if i == 3:
                board_2[1][0] = "['x']"
            if i == 4:
                
                
                board_2[1][1] = "['x']"
            if i == 5:
                board_2[1][2] = "['x']"
            if i == 6:
                board_2[2][0] = "['x']"
            if i == 7:
                board_2[2][1] = "['x']"
            if i == 8:
                board_2[2][2] = "['x']"
        if (board[i][0] == board[i][1] == board[i][2] == ['O', 'O', 'O']):
            if i == 0:
                board_2[0][0] = "['o']"
            if i == 1:
                board_2[0][1] = "['o']"
            if i == 2:
                board_2[0][2] = "['o']"
            if i == 3:
                board_2[1][0] = "['o']"
            if i == 4:
                board_2[1][1] = "['o']"
            if i == 5:
                board_2[1][2] = "['o']"
            if i == 6:
                board_2[2][0] = "['o']"
            if i == 7:
                board_2[2][1] = "['o']"
            if i == 8:
                board_2[2][2] = "['o']"

        elif((board[i][0][0] == ['o'] or board[i][0][0] == ['x']) and (board[i][1][0] == ['o'] or board[i][1][0] == ['x']) and (board[i][2][0] == ['o'] or board[i][2][0] == ['x']) and (board[i][0][1] == ['o'] or board[i][0][1] == ['x']) and (board[i][1][1] == ['o'] or board[i][1][1] == ['x']) and(board[i][2][1] == ['o'] or board[i][2][1] == ['x'])and (board[i][0][2] == ['o'] or board[i][0][2] == ['x']) and (board[i][1][2] == ['o'] or board[i][1][2] == ['x']) and (board[i][2][2] == ['o'] or board[i][2][2] == ['x']) ):
            ret_1 = 40 + i
            if i == 0:
                board_2[0][0] = "['d']"
            if i == 1:
                board_2[0][1] = "['d']"
            if i == 2:
                board_2[0][2] = "['d']"
            if i == 3:
                board_2[1][0] = "['d']"
            if i == 4:
                board_2[1][1] = "['d']"
            if i == 5:
                board_2[1][2] = "['d']"
            if i == 6:
                board_2[2][0] = "['d']"
            if i == 7:
                board_2[2][1] = "['d']"
            if i == 8:
                board_2[2][2] = "['d']"

        
        i += 1




def draw_row_1(row_1, row_number_1):
    print(str(row_number_1) + ' │ '
          + str(row_1[0]) + ' │ '
          + str(row_1[1]) + ' │ '
          + str(row_1[2]) + ' │ ')

def draw_board_1(board_2):
    print('  ┌───┬───┬───┐ ')
    draw_row_1(board_2[0][0] + board_2[0][1]+ board_2[0][2], 1)
    print('  ├───┼───┼───┤ ')
    draw_row_1(board_2[1][0] + board_2[1][1]+ board_2[1][2], 2)
    print('  ├───┼───┼───┤ ')
    draw_row_1(board_2[2][0] + board_2[2][1]+ board_2[2][2], 3)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')
    print()





def find_master_winner(board_2):
    if (board_2 [0][0] == board_2[1][0]==board_2[2][0]== "['x']" or board_2 [0][1] == board_2[1][1]== board_2[2][1]== "['x']"
            or board_2 [0][2] == board_2[1][2]== board_2[2][2]== "['x']" or board_2 [0][0] == board_2[0][1]== board_2[0][2]== "['x']"
            or board_2 [1][0] == board_2[1][1]== board_2[1][2]== "['x']" or board_2 [2][0] == board_2[2][1]== board_2[2][2]== "['x']"
            or board_2 [0][0] == board_2[1][1]== board_2[2][2]== "['x']" or board_2 [0][2] == board_2[1][1]== board_2[2][0]== "['x']"):
        return 'x'
    if (board_2[0][0] == board_2[1][0] == board_2[2][0] == "['o']" or board_2[0][1] == board_2[1][1] == board_2[2][1] == "['o']"
            or board_2[0][2] == board_2[1][2] == board_2[2][2] == "['o']" or board_2[0][0] == board_2[0][1] == board_2[0][2] == "['o']"
            or board_2[1][0] == board_2[1][1] == board_2[1][2] == "['o']" or board_2[2][0] == board_2[2][1] == board_2[2][2] == "['o']"
            or board_2[0][0] == board_2[1][1] == board_2[2][2] == "['o']" or board_2[0][2] == board_2[1][1] == board_2[2][0] == "['o']"):
        return 'o'
    elif (board_2[0][0] != ' ' and board_2[1][0] != ' ' and board_2[2][0] != ' ' and board_2[0][1] != ' ' and board_2[1][1] != ' '
          and board_2[2][1] != ' ' and board_2[0][2] != ' ' and board_2[1][2] != ' ' and board_2[2][2] != ' '):
        return 'd'

    


def get_move(player):
    return input(player + ' player, chose your move: ')





def make_move(player, move, board, changes_left):
    if len(move) != 3:
        ret = 1
        return False
    if move[0] != '1' and move[0] != '2' and move[0] != '3' and move[0] != '4' and move[0] != '5' and move[0] != '6' and move[0] != '7' and move[0] != '8' and move[0] != '9':
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





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

