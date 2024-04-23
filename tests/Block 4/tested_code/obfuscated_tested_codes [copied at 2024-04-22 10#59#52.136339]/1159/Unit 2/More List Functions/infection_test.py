'''
YOU MAN RUN THIS PROGRAM
'''

from infection_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
        
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def check_neighbors_TEST(board,row,column):
    board = [[' ', ' ', '+', ' ', ' ', ' ', ' ', '+', ' ', ' '],
          [' ', '+', ' ', ' ', ' ', ' ', '+', ' ', '+', ' '],
          [' ', '+', '+', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', '+', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', '+', ' ', ' ', ' ', '+'],
          [' ', ' ', ' ', ' ', ' ', ' ', '+', ' ', '+', ' ']]
    TEST(check_neighbors_TEST(board,4,3) == 4)
    TEST(check_neighbors_TEST(board,1,2) == 2)
    TEST(check_neighbors_TEST(board,3,2) == 3)
    TEST(check_neighbors_TEST(board,8,7) == 0)
    TEST(check_neighbors_TEST(board,3,1) == 1)
    TEST(check_neighbors_TEST(board,9,9) == 2)









check_neighbors_TEST()
