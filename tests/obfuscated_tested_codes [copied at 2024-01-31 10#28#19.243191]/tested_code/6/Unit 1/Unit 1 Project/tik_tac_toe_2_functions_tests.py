



from tik_tac_toe_2_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001





def creat_list_TEST():
    print('Start creat_list_TEST')
    TEST(creat_list(1)==[[0]])
    TEST(creat_list(2)==[[0, 0], [0, 0]])
    TEST(creat_list(3)==[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    TEST(creat_list(4)==[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    TEST(creat_list(5)==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    print('End creat_list_TEST')
    print()


def sums_TEST():
    print('Start average_TEST')
    TEST(approx_equal(average([1.0, 3.0, 5.0]), 3))
    TEST(approx_equal(average([1, 2, 4]), 2.333333))
    TEST(approx_equal(average([-2]), -2))
    TEST(average([])==0)
    print('FAIL: Need to test e)mpty list.')
    print('End average_TEST')
    print()


def sums_TEST():
    print('Start sums_TEST')
    TEST(sums([[1,2,3],[4,5,6],[7,8,9]], 1)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 4, 7, 2, 5, 8, 3, 6, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 4, 5, 6, 1, 2, 3])
    TEST(sums([[1,2,3],[4,5,6],[7,8,9]], 2)==[3, 5, 9, 11, 15, 17, 5, 11, 7, 13, 9, 15, 6, 8, 12, 14, 12, 14, 6, 8])
    TEST(sums([[1,2,3],[4,5,6],[7,8,9]], 3)==[6, 15, 24, 12, 15, 18, 15, 15])
    TEST(sums([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 4) == [10, 26, 42, 58, 28, 32, 36, 40, 34, 34])
    TEST(sums([[1]],1)==[1, 1, 1, 1])
    print('End sums_TEST')
    print()


def judgement_TEST():
    print('Start judgement_TEST')
    TEST(judgement([1,2,3],3)== True)
    TEST(judgement([1,2,2,2,2],2) == True)
    TEST(judgement([2,2,2,2,1],3) == False)
    TEST(judgement([2,4,5,6,7,3,3,2,2],1) == False)
    print('End judgement_TEST')
    print()
    
def move_check_human_TEST():
    print('Start move_check_human_TEST')
    TEST(move_check_human([[1,0,1],[-1,0,-1],[0,0,0]],3,3,3)==[[1, 1]])
    TEST(move_check_human([[1,0,1],[-1,0,-1],[0,0,0]],3,3,2)==[[0, 1], [2, 0], [2, 1], [2, 2]])
    TEST(move_check_human([[1,0,1],[-1,0,-1],[0,0,0]],3,3,1)==[[0, 1], [1, 1], [2, 0], [2, 1], [2, 2]])
    TEST(move_check_human([[1,0,1],[-1,0,-1],[0,1,0]],3,3,3)==[[1, 1]])
    TEST(move_check_human([[1,0,1],[-1,0,-1],[0,1,0]],3,3,2)==[[0, 1], [2, 0], [2, 2]])
    print('End move_check_human_TEST')
    print()
def move_check_computer_TEST():
    print('Start move_check_computer_TEST')
    TEST(move_check_computer([[1,0,1],[-1,0,-1],[0,0,0]],3,3,3)==[[0, 1]])
    TEST(move_check_computer([[1,0,1],[-1,0,-1],[0,0,0]],3,3,2)==[[1, 1], [2, 0], [2, 1], [2, 2]])
    TEST(move_check_computer([[1,0,1],[-1,0,-1],[0,0,0]],3,3,1)==[[0, 1], [1, 1], [2, 0], [2, 1], [2, 2]])
    TEST(move_check_computer([[1,0,1],[-1,0,-1],[0,1,0]],3,3,1)==[[0, 1], [1, 1], [2, 0], [2, 2]])
    TEST(move_check_computer([[1,0,1],[-1,0,-1],[0,0,0]],3,2,1)==[[0, 1], [1, 1], [2, 0], [2, 1], [2, 2]])
    print('End move_check_computer_TEST')
    print()





creat_list_TEST()
sums_TEST()
judgement_TEST()
move_check_human_TEST()
move_check_computer_TEST()
