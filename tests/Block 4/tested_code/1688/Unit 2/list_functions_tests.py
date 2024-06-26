


from list_functions import *





def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    
    test_list = [1, 2, 3, 4, 5]
    TEST(item_moved_to_end(test_list, 0) == [2, 3, 4, 5, 1])
    TEST(item_moved_to_end(test_list, 4) == [1, 2, 3, 4, 5])
    TEST(item_moved_to_end(test_list, 2) == [1, 2, 4, 5, 3])
    TEST(test_list == [1, 2, 3, 4, 5])   
    
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    
    test_list = [1, 2, 3, 4, 5]
    TEST(move_item_to_end(test_list, 0) == None)
    TEST(test_list == [2, 3, 4, 5, 1])
    
    
    TEST(move_item_to_end(test_list, 2) == None)
    TEST(test_list == [2, 3, 5, 1, 4])

    
    TEST(move_item_to_end(test_list, 4) == None)
    TEST(test_list == [2, 3, 5, 1, 4])
    
    print('End move_item_to_end_TEST')
    print()




item_moved_to_end_TEST()
move_item_to_end_TEST()
