

from list_functions import *



def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)

def item_moved_to_end_TEST(my_list, index):
    print('Start item_moved_to_end_TEST')
    TEST('wha description',[1,2,4,5,6,3],item_move_to_end([1,2,3,4,5,6],2))
    
def moved_to_end_TEST(my_list, index):
    print('Start moved_to_end_TEST')
