



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
    
    
    my_list = [1, -3, 5, 8, -7]
    expected_list = my_list
    TEST('Regular item_moved_to_end', [1, -3, 8, -7, 5], item_moved_to_end(my_list, 2))
    TEST("Don't change my_list", expected_list, my_list)
    
    
    my_list = [8, -6, 1, 8, -9]
    expected_list = my_list
    TEST('Max index item_moved_to_end', [8, -6, 1, 8, -9], item_moved_to_end(my_list, 4))
    TEST("Don't change my_list", expected_list, my_list)
    
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')

    
    my_list = [1, -3, 5, 8, -7]
    TEST('No return value', None, move_item_to_end(my_list, 2))
    TEST('Change original list', [1, -3, 8, -7, 5], my_list)

    
    my_list = [0, -9, 2, -4, 11]
    TEST('No return value', None, move_item_to_end(my_list, 4))
    TEST('Change original list', [0, -9, 2, -4, 11], my_list)
    
    print('End move_item_to_end_TEST')
    print()



item_moved_to_end_TEST()
move_item_to_end_TEST()
