

from infection_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('not pass')



def create_list_TEST():
    print('Start create_list_TEST')
    TEST(create_list(0,0) == [[0, 0], [0, 0]])
    TEST(create_list(1,1) ==[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    TEST(create_list(2,2)==[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    print('End create_list_TEST')
    print()
def process_TEST():
    print('Start process_TEST')
    TEST(process(1,1,3,3,[[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]) == [[0,0,0,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    TEST(process(0,1,3,3,[[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]) == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])                                                     
    print('End process_TEST')




create_list_TEST()
process_TEST()
