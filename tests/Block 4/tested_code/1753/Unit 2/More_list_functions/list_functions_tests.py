

from list_functions import *









def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5]
    expected_return = [1, 2, 3, 4, 5, 0]
    expected_L = [0, 1, 2, 3, 4, 5]
    TEST('Move first element to last', expected_return, item_moved_to_end(L, 0))
    TEST('State of list', expected_L, L)

    L = [0, 1, 2, 3, 4, 5]
    expected_return = [0, 2, 3, 4, 5, 1]
    expected_L = [0, 1, 2, 3, 4, 5]
    TEST('Move second element to last', expected_return, item_moved_to_end(L, 1))
    TEST('State of list', expected_L, L)

    
    L = [0, 1, 2, 3, 4, 5]
    expected_return = [0, 1, 3, 4, 5, 2]
    expected_L = [0, 1, 2, 3, 4, 5]
    TEST('Move third element to last', expected_return, item_moved_to_end(L, 2))
    TEST('State of list', expected_L, L)

    
    L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    expected_return = [10, 11, 13, 32, 56, 23 ,78, 69, 25, 45]
    expected_L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    TEST('Move fourth element to last', expected_return, item_moved_to_end(L, 3))
    TEST('State of list', expected_L, L)

    
    L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    expected_return = [10, 11, 13, 45, 56, 23 ,78, 69, 25, 32]
    expected_L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    TEST('Move fifth element to last', expected_return, item_moved_to_end(L, 4))
    TEST('State of list', expected_L, L)

    
    print('End item_to_end_TEST')
    print()

    

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5]
    expected_return = None
    expected_L = [1, 2, 3, 4, 5, 0]
    TEST('Move first element to last', None, move_item_to_end(L, 0))
    TEST('State of list', expected_L, L)

    print('Start move_item_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5]
    expected_return = None
    expected_L = [0, 2, 3, 4, 5, 1]
    TEST('Move second element to last', None, move_item_to_end(L, 1))
    TEST('State of list', expected_L, L)

    print('Start move_item_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5]
    expected_return = None
    expected_L = [0, 1, 3, 4, 5, 2]
    TEST('Move third element to last', None, move_item_to_end(L, 2))
    TEST('State of list', expected_L, L)

    print('Start move_item_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5]
    expected_return = None
    expected_L = [0, 1, 2, 4, 5, 3]
    TEST('Move fourth element to last', None, move_item_to_end(L, 3))
    TEST('State of list', expected_L, L)

    print('Start move_item_to_end_TEST')
    L = [0, 1, 2, 3, 4, 5, 6, 7]
    expected_return = None
    expected_L = [0, 1, 2, 3, 5, 6, 7, 4]
    TEST('Move fifth element to last', None, move_item_to_end(L, 4))
    TEST('State of list', expected_L, L)




    
item_moved_to_end_TEST()
move_item_to_end_TEST()
