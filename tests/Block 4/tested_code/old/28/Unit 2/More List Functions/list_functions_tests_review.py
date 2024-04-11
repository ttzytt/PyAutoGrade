

from list_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')





def item_moved_to_end_TEST():
    print("Start item_moved_to_end_TEST")

    
    
    
    
    print("Move first item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(item_moved_to_end(my_list, 0) == [2, 3, 4, 5, 6, 7, 1])
    TEST(my_list == [1, 2, 3, 4, 5, 6, 7])
    print()

    
    print("Move last item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(item_moved_to_end(my_list, 6) == [1, 2, 3, 4, 5, 6, 7])
    TEST(my_list == [1, 2, 3, 4, 5, 6, 7])
    print()

    
    print("Move middle item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(item_moved_to_end(my_list, 3) == [1, 2, 3, 5, 6, 7, 4])
    TEST(my_list == [1, 2, 3, 4, 5, 6, 7])
    print()

    
    print("1 element list")
    my_list = [1]
    TEST(item_moved_to_end(my_list, 0) == [1])
    TEST(my_list == [1])
    print()

    
    print("2 element list")
    my_list = [1, 2]
    TEST(item_moved_to_end(my_list, 0) == [2, 1])
    TEST(my_list == [1, 2])


    print("End item_moved_to_end_TEST")
    print()


    
def move_item_to_end_TEST():
    print("Start move_item_to_end_TEST")

    
    
    
    
    print("Move first item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(move_item_to_end(my_list, 0) == None)
    TEST(my_list == [2, 3, 4, 5, 6, 7, 1])
    print()

    
    print("Move last item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(move_item_to_end(my_list, 6) == None)
    TEST(my_list == [1, 2, 3, 4, 5, 6, 7])
    print()

    
    print("Move middle item")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    TEST(move_item_to_end(my_list, 3) == None)
    TEST(my_list == [1, 2, 3, 5, 6, 7, 4])
    print()

    
    print("1 element list")
    my_list = [1]
    TEST(move_item_to_end(my_list, 0) == None)
    TEST(my_list == [1])
    print()

    
    print("2 element list")
    my_list = [1, 2]
    TEST(move_item_to_end(my_list, 0) == None)
    TEST(my_list == [2, 1])

    print("End move_item_to_end_TEST")
    print()


item_moved_to_end_TEST()
print()
print()
move_item_to_end_TEST()
