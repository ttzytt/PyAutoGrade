











def c4_get_display_row(row):
    return (row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3]
            + ' ' + row[4] + ' ' + row[5] + ' ' + row[6])































def draw_whole_board_row(board1, board2, board3):
    
    for i in range(7):



        print('│' + c4_get_display_row(board1[i]) +
              ' │' + c4_get_display_row(board2[i]) +
              ' │' + c4_get_display_row(board3[i]) + ' │')








def draw_whole_board(connect4_board):
    print('''┌──────────────┬──────────────┬──────────────┐''')
    draw_whole_board_row(connect4_board[0], connect4_board[1], connect4_board[2])
    print('├──────────────┼──────────────┼──────────────┤')
    draw_whole_board_row(connect4_board[3], connect4_board[4], connect4_board[5])
    print('├──────────────┼──────────────┼──────────────┤')
    draw_whole_board_row(connect4_board[6], connect4_board[7], connect4_board[8])
    print('└──────────────┴──────────────┴──────────────┘')









def c4_get_column(player):
    column = input('Player ' + player + ', please enter the ' +
                   'column you want your piece in: ')
    return column





def c4_get_valid_column(player, heights):
    column_move = c4_get_column(player)
    valid = c4_check_move(column_move, heights)

    while not valid:
        column_move = c4_get_column(player)
        valid = c4_check_move(column_move, heights)

    return column_move






def c4_check_move(move, column_height):
    if( not(len(move) == 1) or not('1' <= move <= '7')):
        return False
    
    if (column_height[int(move) - 1] == 7):
        return False

    return True





def c4_make_move(player, column_index, column_heights, board):
    
    row_index = 6 - column_heights[column_index]
    board[row_index][column_index] = player
    column_heights[column_index] += 1



def c4_find_winner(board):
    for column in range(7):
        for row in range(3,7):
            if((board[row][column] != ' ') and
               (board[row][column] == board[row - 1][column]) and
               (board[row][column] == board[row - 2][column]) and
               (board[row][column] == board[row - 3][column])):
                return board[row][column]
                
    for row in range(7):
        for column in range(4):
            if((board[row][column] != ' ') and
               (board[row][column] == board[row][column + 1]) and
               (board[row][column] == board[row][column + 2]) and
               (board[row][column] == board[row][column + 3])):
                return board[row][column]

    for row in range(4):
        for column in range(4):
            if((board[row][column] != ' ') and
               (board[row][column] == board[row + 1][column + 1]) and
               (board[row][column] == board[row + 2][column + 2]) and
               (board[row][column] == board[row + 3][column + 3])):
                print("First diagonal")
                return board[row][column]

    for row in range(3, 7):
        for column in range(4):
            if((board[row][column] != ' ') and
               (board[row][column] == board[row - 1][column + 1]) and
               (board[row][column] == board[row - 2][column + 2]) and
               (board[row][column] == board[row - 3][column + 3])):
                return board[row][column]
        
    
    return ' '




def c4_is_board_full(board_heights):
    for i in range(7):
        if (board_heights[i] != 7):
            return False
    return True








def next_player(player):
    if(player == 'x'):
        return 'o'
    else:
        return 'x'



def get_board(player):
    move = input('Player ' + player + ', please enter the ' + 'board you want your piece in: ')
    return move





def check_board_selection(move):
    if ((len(move) == 1) and ('1' <= move <= '9')):
        return True
    return False





def get_valid_board_selection(player, all_column_heights):
    board_selection = get_board(player)
    valid = check_board_selection(board_selection)
    while not valid:
        print('I\'m sorry, that\'s not a valid move. Please try again.')
        board_selection = get_board(player)
        valid = check_board_selection(board_selection)
    full = c4_is_board_full(all_column_heights[int(board_selection) - 1])
    while full:
        print('I\'m sorry, that board is full, please choose another one.')
        board_selection = get_board(player)
        valid = check_board_selection(board_selection)
        while not valid:
            print('I\'m sorry, that\'s not a valid move. Please try again.')
            board_selection = get_board(player)
            valid = check_board_selection(board_selection)
        full = c4_is_board_full(all_column_heights[int(board_selection) - 1])
    return board_selection


# Searches the board for a winner. Returns the winner, 'x' or 'o', if one
# is found. If there is no winner, returns None.
def find_winner(board):
    for i in range(3):
        if((board[i][0] != ' ') and
           (board[i][0] == board[i][1]) and
           (board[i][0] == board[i][2])):
            return board[i][0]
        elif((board[0][i] != ' ') and
             (board[0][i] == board[1][i]) and
             (board[0][i] == board[2][i])):
            return board[0][i]
    if(board[1][1] != ' '):
        if((board[0][0] == board[1][1]) and
           (board[2][2] == board[1][1])):
            return board[1][1]
        elif((board[0][2] == board[1][1]) and
           (board[2][0] == board[1][1])):
            return board[1][1]
    if((board[0][0] != ' ') and (board[0][1] != ' ') and
       (board[0][2] != ' ') and (board[1][0] != ' ') and
       (board[1][1] != ' ') and (board[1][2] != ' ') and
       (board[2][0] != ' ') and (board[2][1] != ' ') and
       (board[2][2] != ' ')):
        return 'tie'
            
    return None


# Switches the board from the 1 by 9 tic_tac_toe_board to the 3 by 3
# board_of_winners. It then finds if there is a winner on that board, and
# changes that entire board to the winner. 
def switch_between_styles(tic_tac_toe_board, index, board_of_winners, heights):
    if(index < 3):
        board_of_winners[0][index] = c4_find_winner(tic_tac_toe_board[index])
        maybe_change_board_to_winnner(tic_tac_toe_board[index],
                                      board_of_winners[0][index], heights[index])
    elif(index > 5):
        board_of_winners[2][index - 6] = c4_find_winner(tic_tac_toe_board[index])
        maybe_change_board_to_winnner(tic_tac_toe_board[index],
                                      board_of_winners[2][index - 6], heights[index])
    else:
        board_of_winners[1][index - 3] = c4_find_winner(tic_tac_toe_board[index])
        maybe_change_board_to_winnner(tic_tac_toe_board[index],
                                      board_of_winners[1][index - 3], heights[index])


# Fills an entire connect 4 board with the winner if there is a winner
def maybe_change_board_to_winnner(c4_board, winner, board_heights):
    if(winner != ' '):
        for row in range(7):
            for column in range(7):
                c4_board[row][column] = winner
            board_heights[row] = 7


# Checks if the entire game board is full.
def find_if_game_full(heights):
    for c4_board in range(9):
        for column in range(7):
            if (heights[c4_board][column] != 7):
                return None
    return 'tie'
                

    



