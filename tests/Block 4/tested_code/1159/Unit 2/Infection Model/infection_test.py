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




def check_neighbors_TEST():
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
    print('Start check_neighbors_TEST')
    TEST(check_neighbors(board,4,3) == 4)
    TEST(check_neighbors(board,2,3) == 2)
    TEST(check_neighbors(board,1,2) == 3)
    TEST(check_neighbors(board,3,2) == 3)
    TEST(check_neighbors(board,8,7) == 0)
    TEST(check_neighbors(board,3,1) == 1)
    TEST(check_neighbors(board,9,9) == 2)
    print('End check_neighbors_TEST')
    print()

def count_patients_TEST():
    board = [[' ', ' ', '+', ' ', ' ', ' ', ' ', '+', ' ', ' '],
          [' ', '+', ' ', ' ', ' ', ' ', '+', ' ', '+', ' '],
          [' ', '+', '+', ' ', '+', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', '+', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', '+', ' ', ' ', '+', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', ' ', ' ', '+', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', '+', ' ', ' ', ' ', '+'],
          [' ', ' ', ' ', ' ', ' ', ' ', '+', ' ', '+', ' ']]
    print('Start count_patients_TEST')
    TEST(count_patients(board) == 19)
    board = [[' ', ' ', '+', ' ', ' ', ' ', ' ', '+', ' ', ' '],
          [' ', '+', ' ', ' ', ' ', ' ', '+', ' ', '+', ' '],
          [' ', '+', '+', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', '+', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', '+', ' ', ' ', ' ', '+'],
          [' ', ' ', ' ', ' ', ' ', ' ', '+', ' ', '+', ' ']]
    TEST(count_patients(board) == 14)
    print('End count_patients_TEST')
    print()

def draw_patients_cured_TEST():
    board = [ [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']]
    patients = [[3,4],[2,4],[4,1],[8,2]]
    cured = [[2,5],[8,2]]
    print('Start draw_patients_cured_TEST')
    TEST(draw_patients_cured(board,patients,cured) == ([ [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ','+',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ','+',' ',' ',' ',' ',' '],
          [' ', '+', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']]))
    patients = [[3,4],[2,4],[4,1],[8,2]]
    cured = [[3,4],[4,7]]
    TEST(draw_patients_cured(board,patients,cured) == ([ [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ','+',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', '+', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', '+',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']]))
    print('End draw_patients_cured_TEST')
    print()







check_neighbors_TEST()
count_patients_TEST()
draw_patients_cured_TEST()
