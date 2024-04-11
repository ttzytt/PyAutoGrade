

from list_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('not pass')






def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    TEST(item_moved_to_end([1,2,5,6],2) == [1,2,6,5])
    TEST(item_moved_to_end([10, -3, 4, 5, -1],3) == [10,-3,4,-1,5])
    TEST(item_moved_to_end([1],0) == [1])
    TEST(item_moved_to_end([10, -3, 4, 5, -1],4) ==[10, -3, 4, 5, -1] )
    TEST(item_moved_to_end([10, -3, 4, 5, -1],0) == [-3, 4, 5, -1, 10])
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    A = [1,2,5,6]
    move_item_to_end(A,2)
    B = [10, -3, 4, 5, -1]
    move_item_to_end(B,3)
    C = [1]
    move_item_to_end(C,0)
    D = [10, -3, 4, 5, -1]
    move_item_to_end(D,4)
    E = [10, -3, 4, 5, -1]
    move_item_to_end(E,0)
    print('Start move_item_to_end_TEST')
    TEST(A == [1,2,6,5]and move_item_to_end(A,2) == None)
    TEST(B ==[10,-3,4,-1,5] and move_item_to_end(B,3)==None)
    TEST(C == [1] and move_item_to_end(C,0)==None)
    TEST(D == [10, -3, 4, 5, -1] and move_item_to_end(D,4)==None)
    TEST(E ==  [-3, 4, 5, -1, 10] and move_item_to_end(E,0)==None)
    print('End move_item_to_end_TEST')
    print()





item_moved_to_end_TEST()
move_item_to_end_TEST()
