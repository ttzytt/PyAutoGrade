





def draw_row(row):
    print('  │ ' + row[0] + ' │ '
          + row[1] + ' │ ' 
          + row[2] + ' │ ' 
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┐')
    draw_row(board[4])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[3])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[2])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[1])
    print('  ├───┼───┼───┼───┼───┼───┤')
    draw_row(board[0])
    print('  └───┴───┴───┴───┴───┴───┘')
    print('    1   2   3   4   5   6  ')


def check_winner(board, player):
    
    for col in range(3):
        
         for row in range(5):
             
             
             if (board[row][col] == player
                     and board[row][col + 1] == player
                     and board[row][col + 2] == player
                     and board[row][col + 3] == player):
                 
                  return True

    
    for col in range(6):
        
         for row in range(2):
             
             if (board[row][col] == player
            
                     and board[row + 1][col] == player
                     and board[row + 2][col] == player
                     and board[row + 3][col] == player):
                 
                 return True

    
    for row in range(2):
        
        for col in range(3):
            
            if (board[row][col] == player
            
                    and board[row + 1][col + 1] == player 
                    and board[row + 2][col + 2] == player 
                    and board[row + 3][col + 3] == player):
                
                return True

    
    for row in range(2):
        
        for col in range(3, 6):
            
            if (board[row][col] == player
                
                    and board[row + 1][col - 1] == player 
                    and board[row + 2][col - 2] == player
                    and board[row + 3][col - 3] == player):
                
                return True

    return False


def find_winner(board):
    if check_winner(board, 'x'): 
        return 'Player X wins!'
    elif check_winner(board, 'o'): 
        return 'Player O wins!'
     
   


def get_move(player):
    return input(player + ' player, chose your move: ')



def make_move(player, move, board):
    if len(move) > 2: 
        return False
    
    elif len(move) == 2: 
        if move[0] != 'R':
            return False
        
    elif move < '1' or move > '6': 
        return False
            
    elif not (player == 'x' or player == 'o'): 
        return False
        
    
    
    column = int(move) - 1 
    
    for row in range(0, 5): 
        if row == 5:
            if board[row][column] != ' ': 
                return False
        else:
            if board[row][column] == ' ':
               board[row][column] = player 
                                           
               return True
                
                


def remove_chip(player, move, board):
    if move[1] < '1' or move[1] > '6': 
        return False
    
    column = int(move[1]) - 1 
    
    if board[0][column] != player: 
        return False

        
    for row in range(5 - 1):  
                              
        board[row][column] = board[row + 1][column]

    board[4][column] = ' '
    return True

            
    
                
                    
            



def next_player(player):
    if player == 'x': 
        return 'o'
    
    else:  
        return 'x'
 


