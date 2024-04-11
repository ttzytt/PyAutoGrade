





from list_functions import *



def TEST(expected_result, actual_result):
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)
        



def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')

    my_list = [1, 2, 3, 4]
    index = 2
    TEST([1, 2, 4, 3], item_moved_to_end(my_list, index))

    my_list = [1, 2, 3, 4, 5, 6]
    index = 0
    TEST([2, 3, 4, 5, 6, 1], item_moved_to_end(my_list, index))
    
    my_list = ['a', 'b', 'c'] 
    index = 1
    TEST(['a', 'c', 'b'], item_moved_to_end(my_list, index))

    
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')

    my_list = [1, 2, 3, 4]
    index = 2
    move_item_to_end(my_list, index)
    TEST([1, 2, 4, 3], my_list)

    my_list = [1, 2, 3, 4, 5, 6]
    index = 0
    move_item_to_end(my_list, index)
    TEST([2, 3, 4, 5, 6, 1], my_list)
    
    my_list = ['a', 'b', 'c'] 
    index = 1
    move_item_to_end(my_list, index)
    TEST(['a', 'c', 'b'], my_list)

    print('End move_item_to_end_TEST')



item_moved_to_end_TEST()
move_item_to_end_TEST()


    
    

    
    

        


