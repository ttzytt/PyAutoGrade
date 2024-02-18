




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
    
    TEST(item_moved_to_end([1,2,3,4,5,6],2) == [1,2,4,5,6,3])
    
    ml = [1,2,3,4,5,6]
    item_moved_to_end(ml,2)
    TEST(ml == [1,2,3,4,5,6]) 
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    
    TEST(move_item_to_end([1,2,3,4,5,6],2) == None)
    
    ml = [1,2,3,4,5,6]
    move_item_to_end(ml,2)
    TEST(ml == [1,2,4,5,6,3]) 
    print('End move_item_to_end_TEST')
    print()





item_moved_to_end_TEST()
move_item_to_end_TEST()
