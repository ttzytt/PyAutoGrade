


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
    my_list = [1, 2, 3] 
    TEST('Move item to end', [1, 3, 2], item_moved_to_end(my_list, 1))
         
    expected_my_list = [1, 2, 3]
    TEST('Keep my_list the same', expected_my_list, my_list)

    my_list = [1, 2, 3]
    TEST('Move item to end', [1, 2, 3], item_moved_to_end(my_list, None))
         
    expected_my_list = [1, 2, 3]
    TEST('Keep my_list the same', expected_my_list, my_list)

    my_list = [1]
    TEST('Move item to end', [1], item_moved_to_end(my_list, 0))
         
    expected_my_list = [1]
    TEST('Keep my_list the same', expected_my_list, my_list)
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    my_list = [1, 2, 3] 
    TEST('Move item to end', [1, 3, 2], move_item_to_end(my_list, 1))
         
    expected_my_list = [1, 3, 2]
    TEST('Edit my_list directly', expected_my_list, my_list)

    my_list = [1, 2, 3]
    TEST('Move item to end', [1, 2, 3], move_item_to_end(my_list, None))
         
    expected_my_list = [1, 2, 3]
    TEST('Edit my_list directly', expected_my_list, my_list)

    my_list = [1]
    TEST('Move item to end', [1], move_item_to_end(my_list, 0))
         
    expected_my_list = [1]
    TEST('Edit my_list directly', expected_my_list, my_list)
    print('End move_item_to_end_TEST')
    print()
    
    print('End move_item_to_end_TEST')
    print()

item_moved_to_end_TEST()
move_item_to_end_TEST()
