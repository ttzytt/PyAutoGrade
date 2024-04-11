




from list_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
        
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')

    test_list = [1,2,3,4,5,6]
    
    TEST(item_moved_to_end(test_list, 2) == [1,2,4,5,6,3])
    
    TEST(test_list == [1,2,3,4,5,6]) 

    test_list = [2,4,6,8,10]
    TEST(item_moved_to_end(test_list, 4) == [2,4,6,8,10])
    TEST(test_list == [2,4,6,8,10])

    test_list = [1,3,5,7,9]
    TEST(item_moved_to_end(test_list, 0) == [3,5,7,9,1])
    TEST(test_list == [1,3,5,7,9])
    
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')

    test_list = [1,2,3,4,5,6]
    
    TEST(move_item_to_end(test_list, 3) == None)
    
    TEST(test_list == [1,2,3,5,6,4]) 

    tl1 = [2,4,6,8]
    move_item_to_end(tl1, 0)
    TEST(tl1 == [4,6,8,2])

    tl2 = [1,3,5,7,9]
    move_item_to_end(tl2, 4)
    TEST(tl2 == [1,3,5,7,9])
    
    print('End move_item_to_end_TEST')
    print()





item_moved_to_end_TEST()
move_item_to_end_TEST()
