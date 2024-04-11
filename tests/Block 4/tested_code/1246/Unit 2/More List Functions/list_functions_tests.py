







from list_functions import *

def TEST(desc, actual_result, predicted_result):
    print(desc, ':')

    if actual_result == predicted_result:
        print('pass')
        print()
    else:
        print('FAIL')
        print('    Expected result:', predicted_result)
        print('    Actual result:', actual_result)
        print()


def TEST_move_item_to_end():
    print('start TEST_move_item_to_end')

    test_list = [1]
    TEST('test only 1 thing', move_item_to_end(test_list, 0), None)
    TEST('test list change', [1], test_list)

    test_list = [1,2]
    TEST('test 2 things, index as 0', move_item_to_end(test_list,0), None)
    TEST('test list change', [2,1], test_list)

    test_list = [1,2,3,4,5]
    TEST('test 5, index 2', move_item_to_end(test_list,2), None)
    TEST('test list change', [1,2,4,5,3], test_list)

    test_list = [1,2,3,4,5]
    TEST('test 5, last index', move_item_to_end(test_list,4), None)
    TEST('test list change', [1,2,3,4,5], test_list)

    print('end TEST_move_item_to_end')



def TEST_item_moved_to_end():
    print('start TEST_item_moved_to_end')

    TEST('test only 1 thing', item_moved_to_end([1], 0), [1])

    TEST('test only 2 things, index set as 0', item_moved_to_end([1, 2], 0), [2,1])

    TEST('5 element list, index as 2', item_moved_to_end([1, 2, 3, 4, 5], 2), [1,2,4,5,3])

    TEST('test last element to be moved', item_moved_to_end([1, 2, 3, 4, 5], 4), [1,2,3,4,5])

    TEST('index > lenght of list', item_moved_to_end([1,2,3], 3), None)

    print('end TEST_item_moved_to_end')







TEST_item_moved_to_end()
TEST_move_item_to_end()
