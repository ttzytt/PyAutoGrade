


from list_functions_ import *




def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('fail') 






def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    test_list = [1, 2, 3, 4]
    TEST(item_moved_to_end(test_list, 0) == [2, 3, 4, 1])
    TEST(test_list == [1, 2, 3, 4])

   
    test_list = [1, 2, 3, 4]
    TEST(item_moved_to_end(test_list, 1) == [1, 3, 4, 2])
    TEST(test_list == [1, 2, 3, 4])  

    test_list = [1, 2, 3, 4]
    TEST(item_moved_to_end(test_list, 3) == [1, 2, 3, 4])
    TEST(test_list == [1, 2, 3, 4]) 

    
    test_list = [1]
    TEST(item_moved_to_end(test_list, 0) == [1])
    TEST(test_list == [1])  
    
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    test_list = [1, 2, 3, 4]
    TEST(move_item_to_end(test_list, 1) is None)  
    TEST(test_list == [1, 3, 4, 2])  

    
    test_list = [1, 2, 3, 4]
    TEST(move_item_to_end(test_list, 0) is None) 
    TEST(test_list == [2, 3, 4, 1]) 

  
    test_list = [1, 2, 3, 4, 5]
    TEST(move_item_to_end(test_list, 3) is None)  
    TEST(test_list == [1, 2, 3, 5, 4]) 

    test_list = [1]
    TEST(move_item_to_end(test_list, 0) is None)  
    TEST(test_list == [1]) 
    print('End move_item_to_end_TEST')
    print()



item_moved_to_end_TEST()
move_item_to_end_TEST()

