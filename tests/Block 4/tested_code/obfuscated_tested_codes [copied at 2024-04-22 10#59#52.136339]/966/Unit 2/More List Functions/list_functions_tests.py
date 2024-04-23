


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
    print('start move_item_to_end_TEST')
    
    my_list = [-2, 4, 7, 0, -1]
    expected_list = my_list
    TEST('normal test', [-2, 4, 7, -1, 0], item_moved_to_end(my_list, 3))
    TEST('doesnt change list', expected_list, my_list)
    
    print('end move_item_to_end_TEST')
    print()


def item_moved_to_end_TEST():
    print('start move_item_to_end_TEST')
    
    my_list = [5, -4, 2, 5, -8]
    expected_list = my_list
    TEST('doest change, max index', [5, -4, 2, 5, -8], item_moved_to_end(my_list, 4))
    TEST('desnt change list', expected_list, my_list)
    
    print('end move_item_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('start move_item_to_end_TEST')

    my_list = [-2, 4, 7, 0, -1]
    TEST('no returned value', None, move_item_to_end(my_list, 3))
    TEST('changes list', [-2, 4, 7, -1, 0], my_list)

def move_item_to_end_TEST():
    my_list = [-2, 4, 7, -1, 0]
    TEST('no returned value', None, move_item_to_end(my_list, 4))
    TEST('changes list', [-2, 4, 7, -1, 0], my_list)

item_moved_to_end_TEST() 
move_item_to_end_TEST()
