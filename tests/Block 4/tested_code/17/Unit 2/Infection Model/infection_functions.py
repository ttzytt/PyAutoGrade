





import random



def board_initialize(board):
    for i in range(1, 11):
        for j in range(1, 11):
            a = random.randint(1, 100)
            if a <= 10:
                board[i][j] = 1 



def know_nearby(board, nearby_infections):
    for i in range(1, 11):
        for j in range(1, 11):
            
            nearby_infections[i][j] = board[i - 1][j] + board[i + 1][j] + board[i][j - 1] + board[i][j + 1]



def board_modify(board, nearby_infections, infection_possibility = 0.35, cure_possibility = 0.10):
    for i in range(1, 11):
        for j in range(1, 11):
            a = random.random()
            if board[i][j] == 1:
                if a < float(cure_possibility):
                    board[i][j] = 0
            else:
                if a < float(infection_possibility) * nearby_infections[i][j]:
                    board[i][j] = 1



def find_ending(board):
    ending = 0
    for i in range(1, 11):
        for j in range(1, 11):
            ending += board[i][j]
    if ending == 0:
        return 1 
    elif ending == 100:
        return 0 
    else:
        return None




def find_difference(board):
    ending = 0
    all_board = 0
    for i in range(2, 10):
        for j in range(2, 10):
            ending += board[i][j]
    for i in range(1, 11):
        for j in range(1, 11):
            all_board += board[i][j]
    return (ending*1.00/64)/((all_board-ending)*1.00/36)
