


from list_functions import *







def TEST(actual_result , expected_result):
	if actual_result == expected_result:
		print('pass')
	else:
		print('FAIL')
        





def approx_equal(a, b):
    return abs(a - b) < 0.0001




def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    TEST(item_moved_to_end([1,2,3,4,5,6,7,8,9],3) , [1,2,3,5,6,7,8,9,4]) 
    TEST(item_moved_to_end([1,2,3,4,5,6,7,8,9],0) , [2,3,4,5,6,7,8,9,1]) 
    TEST(item_moved_to_end([1,2,3,4,5,6,7,8,9],8) , [1,2,3,4,5,6,7,8,9]) 
    print('Start item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start_move_item_to_end_TEST')
    my_list = [1,2,3,4,5,6,7,8,9] 
    TEST(None , (move_item_to_end(my_list,3))) 
    expected = [1,2,3,5,6,7,8,9,4] 
    TEST(expected , my_list)
    
    my_list = [1,2,3,4,5,6,7,8,9] 
    TEST(None , (move_item_to_end(my_list,0)))
    expected = [2,3,4,5,6,7,8,9,1]
    TEST(expected , my_list)
    
    my_list = [1,2,3,4,5,6,7,8,9] 
    TEST(None , (move_item_to_end(my_list,8)))
    expected = [1,2,3,4,5,6,7,8,9]
    TEST(expected , my_list)
    print('End move_item_to_end_TEST')
    print()





item_moved_to_end_TEST()
move_item_to_end_TEST()
