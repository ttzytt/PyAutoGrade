



from list_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST: ')
    my_list = [0,1,2,3]
    TEST(item_moved_to_end(my_list, 1) == [0,2,3,1])
    TEST(my_list == [0,1,2,3])
    my_list = [11, 4, 5, 14, 6, 66]
    TEST(item_moved_to_end(my_list, 1) == [11, 5, 14, 6, 66, 4])
    TEST(my_list == [11, 4, 5, 14, 6, 66])
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST: ')
    my_list = [11,4,5,14,6,66]
    TEST(move_item_to_end(my_list, 1) == None)
    TEST(my_list == [11, 5, 14, 6, 66, 4])
    my_list = [1,2,3,55]
    TEST(move_item_to_end(my_list, 3) == None)
    TEST(my_list == [1,2,3,55])
    print('End move_item_to_end_TEST')
    print()





item_moved_to_end_TEST()
move_item_to_end_TEST()

