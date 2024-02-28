

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
    expected_L = [1, 2, 3, 4, 5, 0]
    TEST('Move first element to last', expected_L, item_moved_to_end(L, 0))
    
    L = [0, 1, 2, 3, 4, 5]
    expected_L = [0, 2, 3, 4, 5, 1]
    TEST('Move second element to last', expected_L, item_moved_to_end(L, 1))
    
    L = [0, 1, 2, 3, 4, 5]
    expected_L = [0, 1, 3, 4, 5, 2]
    TEST('Move third element to last', expected_L, item_moved_to_end(L, 2))
    
    L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    expected_L = [10, 11, 13, 32, 56, 23 ,78, 69, 25, 45]
    TEST('Move fourth element to last', expected_L, item_moved_to_end(L, 3))
    
    L = [10, 11, 13, 45, 32, 56, 23 ,78, 69, 25]
    expected_L = [10, 11, 13, 45, 56, 23 ,78, 69, 25, 32]
    TEST('Move fifth element to last', expected_L, item_moved_to_end(L, 4))
    
    print('End item_to_end_TEST')
    print()


    
item_moved_to_end_TEST()
