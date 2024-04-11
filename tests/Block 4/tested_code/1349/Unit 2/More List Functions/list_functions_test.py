





from list_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')






def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    TEST(item_moved_to_end([1, 2, 5, 6], 2) == [1, 2, 6, 5])
    TEST(item_moved_to_end([10, -3, 4, 5, -1], 2) == [10, -3, 5, -1, 4]) 
    TEST(item_moved_to_end([1, 2, 3, 4], 3) == [1, 2, 3, 4]) 
    my_list = [3, 4] 
    TEST(item_moved_to_end(my_list, 0) == [4, 3])
    
    TEST(my_list == [3, 4])
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    my_list = [1, 2, 1, 4, 5]
    TEST(move_item_to_end(my_list, 3) == None)
    TEST(my_list == [1, 2, 1, 5, 4])
    my_list = [1, 7, 4, 6, 5]
    TEST(move_item_to_end(my_list, 2) == None)
    
    TEST(my_list == [1, 7, 6, 5, 4])
    print('End average_TEST')
    print()



    



item_moved_to_end_TEST()
move_item_to_end_TEST()



