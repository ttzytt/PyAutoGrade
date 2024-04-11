


'''
the relationship between
1. five_of_a_kind(board),
2. four_of_a_kind(board),
3. full_house(board),
4. straight(board),
5. Three_of_a_kind(board),
6. two_pair(board),
7. one_pair(board)
should be:

for an 'i',
if 1 > 0, then 2=3=5=6=7 == 0
elif 2 > 0, then 5=6=7 == 0
elif 3 > 0, then 5=7 == 0
elif 5 > 0, then 7 == 0
elif 6 > 0, then 7 == 0

It will be easy to count the score in row and column

'''

def logic_of_row_score(board):
    row_score = 0
    for i in range(5):
        row = [board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]]
        row.sort()
        
        if (board[i][0] == board[i][1] == board[i][2] == board[i][3]
            == board[i][4]):
            row_score += 30
        
        elif ((row[1] == row[2] == row[3] == row[4])
            or (row[0] == row[1] == row[2] == row[3])):
            row_score += 16
        
        elif ((row[0] == row[1] == row[2] and row[3] == row[4])
            or (row[0] == row[1] and row[2] == row[3] == row[4])):
            row_score += 10
        
        elif (row[0] == row[1] == row[2] or row[2] == row[3] == row[4]):
            row_score += 6
        
        elif ((row[0] == row[1] and row[2] == row[3])
            or (row[0] == row[1] and row[3] == row[4])
            or (row[1] == row[2] and row[3] == row[4])):
            row_score += 3
        
        elif (row[0] == row[1] or row[2] == row[3] or row[3] == row[4]
             or row[1] == row[2]):
            row_score += 1
        
        elif int(row[4]) - int(row[1]) == 4:
            row_score += 12
    return row_score

def logic_of_column_score(board):
    col_score = 0
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        col.sort()
        
        if (board[0][i] == board[1][i] == board[2][i] == board[3][i]
            == board[4][i]):
            col_score += 30
        
        elif ((col[1] == col[2] == col[3] == col[4])
            or (col[0] == col[1] == col[2] == col[3])):
            col_score += 16
        
        elif ((col[0] == col[1] == col[2] and col[3] == col[4])
            or (col[0] == col[1] and col[2] == col[3] == col[4])):
            col_score += 10
        
        elif (col[0] == col[1] == col[2] or col[2] == col[3] == col[4]):
            col_score += 6
        
        elif ((col[0] == col[1] and col[2] == col[3])
            or (col[0] == col[1] and col[3] == col[4])
            or (col[1] == col[2] and col[3] == col[4])):
            col_score += 3
        
        elif (col[0] == col[1] or col[2] == col[3]
            or col[3] == col[4] or col[1] == col[2]):
            col_score += 1
        
        elif int(col[4]) - int(col[1]) == 4:
            col_score += 12
    return col_score

def sum_score(row_score, col_score):
    Sum = sum(row_score, col_score)
    return Sum
