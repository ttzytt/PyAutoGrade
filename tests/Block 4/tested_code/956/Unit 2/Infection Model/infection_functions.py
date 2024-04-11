




import random
random.seed()


def setup_board(board, board_length, infected_row, infected_column):
    
    if (infected_row>0 and infected_row < board_length
            and infected_column >0 and infected_column < board_length):
        board[infected_row][infected_column] = 1 
    else:
        print("Please re-enter")
    




def infecting_neighbor(board, board_length, infect, heal, board_copy):
    
    copy_board(board, board_copy, board_length) 
    row = 1
    column = 1 
    infected_neighbor_count = 0
    
    while (row< (board_length-1)):
        column = 1
        while (column< (board_length-1)):
            if board[row][column] == 0:
                
                if board_copy[row-1][column] == 1:  
                    infected_neighbor_count += 1
                if board_copy[row][column-1] == 1:
                    infected_neighbor_count += 1
                if board_copy[row][column+1] == 1:
                    infected_neighbor_count += 1
                if board_copy[row+1][column] == 1:
                    infected_neighbor_count += 1

            if (infected_neighbor_count >= 1 and board[row][column] == 0):
                
                if random.random() < (infect * infected_neighbor_count):
                    board[row][column] = 1
                    infected_neighbor_count = 0
                else:
                    infected_neighbor_count = 0
                
            column += 1
        row += 1
    
    copy_board(board, board_copy, board_length)
    


def heal_process(board_length, board, board_copy, heal):
    row = 1
    column = 1
    
    while (row< (board_length-1)):
        column = 1
        while (column< (board_length-1)):
            if board[row][column] == 1:
                if random.random() < heal:
                    board[row][column] = 0
            column += 1
        row += 1

    
    copy_board(board, board_copy, board_length)

    
    

def copy_board(board, board_copy, board_length):
    
    row = 1
    while (row< (board_length-1)):
        column = 1
        while (column< (board_length-1)):
            board_copy[row][column] = 0
            column += 1
        row+= 1

    row = 1
    
    
    while (row< (board_length-1)):
        column = 1
        while (column< (board_length-1)):
            if board[row][column] == 1:
                board_copy[row][column] = 1
            if board[row][column] == 0:
                board_copy[row][column] = 0 
            column += 1
        row+=1



def print_board(board, board_length):
    print()
    row = 1
    column = 1
    while (row< (board_length-1)):
        column = 1
        while (column< (board_length-1)):
            if board[row][column] == 1:
                print('X', end = ' ')
                
            if board[row][column] == 0:
                print('·', end = ' ')
        
            column += 1
        print()
        row += 1

