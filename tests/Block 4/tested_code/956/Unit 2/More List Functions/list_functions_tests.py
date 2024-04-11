


            
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
    
    my_list = [13,4,6,14,7,93]
    
    TEST(item_moved_to_end(my_list, 1) == [13,6,14,7,93,4])
    TEST(my_list == [13,4,6,14,7,93])
    print('End item_moved_to_end_TEST: ')
    print()



def move_item_to_end_TEST():
    print('move_item_to_end_TEST: ')
    
    my_list = [13,4,5,14,7,93]
    TEST(move_item_to_end(my_list, 1) == None)
    
    TEST(my_list == [13,5,14,7,93,4])
    print('End imove_item_to_end_TEST: ')
    print()



item_moved_to_end_TEST()
move_item_to_end_TEST()
