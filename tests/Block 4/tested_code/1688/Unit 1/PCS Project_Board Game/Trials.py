import random
random.seed()

"""
def deal_2_hands():
    player_1_hands = []
    player_2_hands = []
    for i in range(0, 5):
        n = random.randint(0, 9)
        player_1_hands.append(n)
    for i in range(0, 5):
        n = random.randint(0, 9)
        player_2_hands.append(n)
    print(player_1_hands)
    print(player_2_hands)



def deal_2_hands():
    hands = [[], []]
    for j in range(0, 2):
        for i in range(0, 5):
            n = random.randint(0, 9)
            hands[j].append(n)

    print(hands)


deal_2_hands()


def get_move(player):
    choosen_number = input(player + ' player, choose a number in your hand: ')
    input(player + ' player, choose your move: ')



board = [ ['1', ' ', ' ', ' ', ' '],
          ['2', ' ', ' ', ' ', ' '],
          ['3', ' ', ' ', ' ', ' '],
          ['4', ' ', ' ', ' ', ' '],
          ['5', ' ', ' ', ' ', ' '] ]

def find_winner(board):
    for i in range(0, 4):
        for j in range(0, 4):
            if (int(board[j][i]) == int(board[j+1][i] + 1)) or \
               (int(board[j][i]) == int(board[j+1][i] - 1)):
                return True

find_winner(board)

def find_winner(board):
    for i in range(0, 4):
        for j in range(0, 4):
            while board[j][i] != ' ':
                if (int(board[j][i]) == int(board[j+1][i]) + 1) or \
                   (int(board[j][i]) == int(board[j+1][i]) - 1):
                    return True

            

def find_winner(board):
    for i in range(0, 4):
        for j in range(0, 4):
            if board[j][i] == ' ':
                continue
            else:
                if (int(board[j][i]) == int(board[j+1][i]) + 1) or \
                   (int(board[j][i]) == int(board[j+1][i]) - 1):
                    return True


def find_winner(board):
    for a in range(0, 5):
        for b in range(0, 5):
            if board[a][b] == ' ':
                board[a][b] == 0
            else:
                continue
    
    for i in range(0, 4):
        for j in range(0, 4):
                if (int(board[j][i]) == int(board[j+1][i]) + 1) or \
                   (int(board[j][i]) == int(board[j+1][i]) - 1):
                    return True


def find_winner(board):
    for i in range(0, 4):
        for j in range(0, 4):
                if (int(board[j][i]) == int(float(board[j+1][i])) + 1) or \
                   (int(board[j][i]) == int(float(board[j+1][i])) - 1):
                    return True

board = [ ['1', ' ', ' ', ' ', ' '],
          [' ', '2', ' ', ' ', ' '],
          [' ', ' ', '3', ' ', ' '],
          [' ', ' ', ' ', '4', ' '],
          [' ', ' ', ' ', ' ', '5'] ]



def find_winner(board):
    for a in range(0, 5):
        for b in range(0, 5):
            if board[a][b] == ' ':
                board[a][b] = 0
            else:
                continue
    
    for i in range(0, 4):
        for j in range(0, 4):
                if (int(board[j][i]) == int(board[j+1][i]) + 1) or \
                   (int(board[j][i]) == int(board[j+1][i]) - 1):
                    return True
                return False

def find_winner(board):
    for a in range(0, 5):
        for b in range(0, 5):
            if board[a][b] == ' ':
                board[a][b] = 0
            else:
                continue
    
    for i in range(0, 4):
        for j in range(0, 4):
                if (int(board[j][i]) == int(board[j+1][i]) + 1)
                    return True
                return False

def find_winner(board):
    for a in range(0, 5):
        for b in range(0, 5):
            if board[a][b] == ' ':
                board[a][b] = 0
            else:
                continue
    
    for i in range(0, 5):
        for j in range(0, 4):
            if int(board[i][j]) + 1 == int(board[i][j+1]):
                return True
            return False



    
find_winner(board)


def consecutive(a_list):
    for i in range(len(a_list)):
        if a_list[i+1] == a_list[i] + 1:
            return True
        return False




def find_winner(board):

    # Check rows
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
                break
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
                break
        if consecutive_row:
            return True

    # Check columns
    for i in range(len(board) - 1):
        consecutive_column = True
        for j in range(len(board)):
            if board[i][j] == ' ' or board[i + 1][j] == ' ':
                consecutive_column = False
                break
            elif abs(int(board[i][j]) - int(board[i + 1][j])) != 1:
                consecutive_column = False
                break
        if consecutive_column:
            return True

    for i in range(len(board)):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
            break
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
            break
        if consecutive_diagonal_1:
            return True
        
    for i in range(len(board)):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][(4 - i) + 1] == ' ':
            consecutive_diagonal_2 = False
            break
        elif abs(int(board[i][4 - i]) - int(board[i + 1][(4 - i) + 1])) != 1:
            consecutive_diagonal_2 = False
            break
        if consecutive_diagonal_2:
            return True

    return False





def find_winner(board):

    # Check rows
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
                break
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
                break


    # Check columns
    for i in range(len(board) - 1):
        consecutive_column = True
        for j in range(len(board)):
            if board[i][j] == ' ' or board[i + 1][j] == ' ':
                consecutive_column = False
                break
            elif abs(int(board[i][j]) - int(board[i + 1][j])) != 1:
                consecutive_column = False
                break


    for i in range(len(board)):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
            break
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
            break
        
        
    for i in range(len(board)):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][4 - (i + 1)] == ' ':
            consecutive_diagonal_2 = False
            break
        elif abs(int(board[i][4 - i]) - int(board[i + 1][(4 - i) + 1])) != 1:
            consecutive_diagonal_2 = False
            break
    if consecutive_row == True or \
       consecutive_column == True or \
       consecutive_diagonal_1 == True or \
       consecutive_diagonal_2 == True:
        return True

    else:
        return False



def find_winner(board):

    # Check rows
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
                break
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
                break
        if consecutive_row:
            return True

    # Check columns
    for i in range(len(board) - 1):
        consecutive_column = True
        for j in range(len(board)):
            if board[i][j] == ' ' or board[i + 1][j] == ' ':
                consecutive_column = False
                break
            elif abs(int(board[i][j]) - int(board[i + 1][j])) != 1:
                consecutive_column = False
                break
        if consecutive_column:
            return True

    for i in range(len(board)):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
            break
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
            break
        if consecutive_diagonal_1:
            return True
        
    for i in range(len(board)):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][4 - (i + 1)] == ' ':
            consecutive_diagonal_2 = False
            break
        elif abs(int(board[i][4 - i]) - int(board[i + 1][(4 - i) + 1])) != 1:
            consecutive_diagonal_2 = False
            break
        if consecutive_diagonal_2:
            return True

    return False




def find_winner(board):

    # Check rows
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
        if consecutive_row:
            return True

    # Check columns
    for i in range(len(board) - 1):
        consecutive_column = True
        for j in range(len(board)):
            if board[i][j] == ' ' or board[i + 1][j] == ' ':
                consecutive_column = False
            elif abs(int(board[i][j]) - int(board[i + 1][j])) != 1:
                consecutive_column = False
        if consecutive_column:
            return True

    for i in range(len(board) - 1):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
        if consecutive_diagonal_1:
            return True
        
    for i in range(len(board) - 1):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][4 - (i + 1)] == ' ':
            consecutive_diagonal_2 = False
        elif abs(int(board[i][4 - i]) - int(board[i + 1][(4 - i) + 1])) != 1:
            consecutive_diagonal_2 = False
        if consecutive_diagonal_2:
            return True

    return False


def find_winner(board):

    # Check rows
    for i in range(len(board)):
        consecutive_row = True
        for j in range(len(board[i]) - 1):
            if board[i][j] == ' ' or board[i][j + 1] == ' ':
                consecutive_row = False
                continue
            elif abs(int(board[i][j]) - int(board[i][j + 1])) != 1:
                consecutive_row = False
                continue
        if consecutive_row:
            return True

    # Check columns
    for i in range(len(board) - 1):
        consecutive_column = True
        for j in range(len(board)):
            if board[i][j] == ' ' or board[i + 1][j] == ' ':
                consecutive_column = False
                continue
            elif abs(int(board[i][j]) - int(board[i + 1][j])) != 1:
                consecutive_column = False
                continue
        if consecutive_column:
            return True

    for i in range(len(board) - 1):
        j = i
        consecutive_diagonal_1 = True
        if board[i][j] == ' ' or board[i + 1][j + 1] == ' ':
            consecutive_diagonal_1 = False
            continue
        elif abs(int(board[i][j]) - int(board[i + 1][j + 1])) != 1:
            consecutive_diagonal_1 = False
            continue
        if consecutive_diagonal_1:
            return True
        
    for i in range(len(board) - 1):
        consecutive_diagonal_2 = True
        if board[i][4 - i] == ' ' or board[i + 1][4 - (i + 1)] == ' ':
            consecutive_diagonal_2 = False
            continue
        elif abs(int(board[i][4 - i]) - int(board[i + 1][(4 - i) + 1])) != 1:
            consecutive_diagonal_2 = False
            continue
        if consecutive_diagonal_2:
            return True

    return False
"""


def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i + 1] != a_list[i] + 1:
            return False
    for i in range(len(a_list) - 1):
        if a_list[i + 1] != a_list[i] - 1:
            return False
    return True


print(is_consecutive([5, 4, 3, 2, 1]))



"""
            



def find_winner(board):

    # Rows
    for i in range(len(board)):
        if ' ' in board[i]:
            return False
        for j in range(len(board)):
            
            

"""






    



