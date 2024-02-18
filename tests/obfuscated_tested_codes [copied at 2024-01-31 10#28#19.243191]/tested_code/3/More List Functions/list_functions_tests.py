

from list_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')
def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)






def approx_equal(a, b):
    return abs(a - b) < 0.0001




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    my_list = [1, 3, 5]
    index = 1
    TEST('item moved to the end', [1, 5, 3], item_moved_to_end(my_list, index))
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    my_list = [1, 3, 5]
    index = 1
    TEST('item moved to the end', [1, 5, 3], move_item_to_end(my_list, index))
    print('End move_item_to_end_TEST')
    print()

 

item_moved_to_end_TEST()
move_item_to_end_TEST()
