


from list_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')
        


def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    TEST(item_moved_to_end([4, 2, 66, 8, 9], 3) == [4, 2, 66, 9, 8])
    
    
    
    print('End item_moved_to_end_TEST')
    print()

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    
    
    
    print('End move_item_to_end_TEST')
    print()



item_moved_to_end_TEST()
move_item_to_end_TEST()
