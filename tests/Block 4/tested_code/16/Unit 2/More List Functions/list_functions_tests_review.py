






from list_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass :)')
    else:
        print('FAIL >:(')
        


def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    list = [1, 2, 3, 4]
    
    new_list = item_moved_to_end(list, 0)
    TEST(new_list == [2, 3, 4, 1])
    TEST(list == [1, 2, 3, 4])
    
    new_list = item_moved_to_end(list, 1)
    TEST(new_list == [1, 3, 4, 2])
    TEST(list == [1, 2, 3, 4])
    
    new_list = item_moved_to_end(list, 2)
    TEST(new_list == [1, 2, 4, 3])
    TEST(list == [1, 2, 3, 4])
    
    TEST(item_moved_to_end(list, 3) == [1, 2, 3, 4])
    TEST(list == [1, 2, 3, 4])
    
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    
    list = [1, 2, 3, 4]
    TEST(move_item_to_end(list, 0) is None)
    TEST(list == [2, 3, 4, 1])
    
    list = [1, 2, 3, 4]
    TEST(move_item_to_end(list, 1) is None)
    TEST(list == [1, 3, 4, 2])
    
    list = [1, 2, 3, 4]
    TEST(move_item_to_end(list, 2) is None)
    TEST(list == [1, 2, 4, 3])
    
    list = [1, 2, 3, 4]
    TEST(move_item_to_end(list, 3) is None)
    TEST(list == [1, 2, 3, 4])
    
    print('End move_item_to_end_TEST')
    print()
    
    





item_moved_to_end_TEST()
move_item_to_end_TEST()


