



import random

random.seed


"""
Print the given row to the screen.
Input:
    row            a list representing one row of the board
    row_number     int to be printed before the row
"""

def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  └───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E  ')


def give_cards(card):
    print('You get a ' + card)



def make_move(move, card, board):
    if len(move) != 2:
        return False
    if (move[0] != '1' and move[0] != '2' and move[0] != '3'
        and move[0] != '4' and move[0] != '5'):
        return False
    if (move[1] != 'A' and move[1] != 'B' and move[1] != 'C'
        and move[1] != 'D' and move[1] != 'E'):
        return False
    row = int(move[0]) - 1
    column = ord(move[1]) - ord('A')
    if board[row][column] != ' ':
        return False

    board[row][column] = str(card)
    return True




'''

# different cases to get score
def five_of_a_kind(board):
    five_of_a_kind_score = 0
    for i in range(5):
        if (board[i][0] == board[i][1] == board[i][2] == board[i][3]
            == board[i][4]):
            five_of_a_kind_score += 30
            print('*There is a five of a kind in row' + str(i))
        else:
            print('There is no five of a kind in row' + str(i))
            
    for i in range(5):
        if (board[0][i] == board[1][i] == board[2][i] == board[3][i]
            == board[4][i]):
            five_of_a_kind_score += 30
            print('*There is a five of a kind in column' + str(i))
        else:
            print('There is no five of a kind in column' + str(i))
    return five_of_a_kind_score

def four_of_a_kind(board):
    four_of_a_kind_score = 0
    for i in range(5):
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if ((row[1] == row[2] == row[3] == row[4])
            or (row[0] == row[1] == row[2] == row[3])):
            four_of_a_kind_score += 16

    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if ((col[1] == col[2] == col[3] == col[4])
            or (col[0] == col[1] == col[2] == col[3])):
            four_of_a_kind_score += 16
    return four_of_a_kind_score
        

def full_house(board):
    full_house_score = 0
    for i in range(5):
        #let row be sorted out 
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if ((row[0] == row[1] == row[2] and row[3] == row[4])
            or (row[0] == row[1] and row[2] == row[3] == row[4])):
            full_house_score += 10
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if ((col[0] == col[1] == col[2] and col[3] == col[4])
            or (col[0] == col[1] and col[2] == col[3] == col[4])):
            full_house_score += 10

    return full_house_score

def straight(board):
    straight_score = 0
    for i in range(5):
        #let row be sorted out 
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if int(row[4]) - int(row[0]) == 4:
            straight_score += 12
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if int(col[4]) - int(col[0]) == 4:
            straight_score += 12

    return straight_score

def Three_of_a_kind(board):
    Three_of_a_kind_score = 0
    for i in range(5):
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if (row[0] == row[1] == row[2] or row[2] == row[3] == row[4]):
            Three_of_a_kind_score += 6
            print('There is a three of a kind in row' + str(i))
        else:
            print('There is no three of a kind in row' + str(i))

    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if (col[0] == col[1] == col[2] or col[2] == col[3] == col[4]):
            Three_of_a_kind_score += 6
            print('There is a three of a kind in column' + str(i))
        else:
            print('There is no three of a kind in column' + str(i))

    return Three_of_a_kind_score
        
def two_pair(board):
    two_pair_score = 0
    for i in range(5):
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if ((row[0] == row[1] and row[2] == row[3])
            or (row[0] == row[1] and row[3] == row[4])
            or (row[1] == row[2] and row[3] == row[4])):
            two_pair_score += 3
            print('There is a two pair in row' + str(i))
        else:
            print('There is no two pair in row' + str(i))

    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if ((col[0] == col[1] and col[2] == col[3])
            or (col[0] == col[1] and col[3] == col[4])
            or (col[1] == col[2] and col[3] == col[4])):
            two_pair_score += 3
            print('There is a two pair in column' + str(i))
        else:
            print('There is no two pair in column' + str(i))
    return two_pair_score

def one_pair(board):
    one_pair_score = 0
    for i in range(5):
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        if (row[0] == row[1] or row[2] == row[3] or row[3] == row[4]
             or row[1] == row[2]):
            one_pair_score += 1
            print('There is a one pair in row' + str(i))
        else:
            print('There is no one pair in row' + str(i))

    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        if (col[0] == col[1] or col[2] == col[3]
            or col[3] == col[4] or col[1] == col[2]):
            one_pair_score += 1
            print('There is a one pair in column' + str(i))
        else:
            print('There is no one pair in column' + str(i))
    return one_pair_score
    
def final_score(score_list):
    score = sum(score_list)
    return score

'''

def logic_of_row_score(board):
    row_score = 0
    i = 0
    while i < 5:
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        
        if row[0] == row[1] == row[2] == row[3] == row[4]:
            row_score += 30
            print('there is a five_of_a_kind in row ' + str(i + 1)) 
        
        elif ((row[1] == row[2] == row[3] == row[4])
            or (row[0] == row[1] == row[2] == row[3])):
            row_score += 16
            print('there is a four_of_a_kind in row ' + str(i + 1))
        
        elif ((row[0] == row[1] == row[2] and row[3] == row[4])
            or (row[0] == row[1] and row[2] == row[3] == row[4])):
            row_score += 10
            print('there is a full_house in row ' + str(i + 1))
        
        elif (row[0] == row[1] == row[2] or row[1] == row[2] == row[3] or row[2] == row[3] == row[4]):
            row_score += 6
            print('there is a three_of_a_kind in row ' + str(i + 1))
        
        elif ((row[0] == row[1] and row[2] == row[3])
            or (row[0] == row[1] and row[3] == row[4])
            or (row[1] == row[2] and row[3] == row[4])):
            row_score += 3
            print('there is a two_pair in row ' + str(i + 1))
        
        elif (row[0] == row[1] or row[2] == row[3] or row[3] == row[4]
             or row[1] == row[2]):
            row_score += 1
            print('there is a one_pair in row ' + str(i + 1))
        
        elif int(row[4]) - int(row[0]) == 4:
            row_score += 12
            print('there is a straight in row ' + str(i + 1))
        i += 1
    print('your row score is: ' + str(row_score))
    print()
    return row_score


def logic_of_column_score(board):
    col_score = 0
    
    col_name_list = ['A', 'B', 'C', 'D', 'E']
    i = 0
    while i < 5:
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        
        if col[0] == col[1] == col[2] == col[3] == col[4]:
            col_score += 30
            print('there is a five_of_a_kind in column' + col_name_list[i])
        
        elif ((col[1] == col[2] == col[3] == col[4])
            or (col[0] == col[1] == col[2] == col[3])):
            col_score += 16
            print('there is a four_of_a_kind in column' + col_name_list[i])
        
        elif ((col[0] == col[1] == col[2] and col[3] == col[4])
            or (col[0] == col[1] and col[2] == col[3] == col[4])):
            col_score += 10
            print('there is a full_house in column' + col_name_list[i])
        
        elif (col[0] == col[1] == col[2] or col[1] == col[2] == col[3]
            or col[2] == col[3] == col[4]):
            col_score += 6
            print('there is a three_of_a_kind in column' + col_name_list[i])
        
        elif ((col[0] == col[1] and col[2] == col[3])
            or (col[0] == col[1] and col[3] == col[4])
            or (col[1] == col[2] and col[3] == col[4])):
            col_score += 3
            print('there is a two_pair in column' + col_name_list[i])
        
        elif (col[0] == col[1] or col[2] == col[3]
            or col[3] == col[4] or col[1] == col[2]):
            col_score += 1
            print('there is a one_pair in column' + col_name_list[i])
        
        elif int(col[4]) - int(col[0]) == 4:
            col_score += 12
            print('there is a straight in column' + col_name_list[i])
        i += 1
    print('your column score is: ' + str(col_score))
    print()
    return col_score


def score(board):
    Sum = logic_of_row_score(board) + logic_of_column_score(board)
    return Sum
    


def get_move(name):
    return input(name + ', chose your move: ')

