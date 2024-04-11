



from list_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)


def item_moved_to_end_TEST():
    print('Start item_moved_to_end_TEST')
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('First Element', [3, 4, 2, 15, 2, 16, 1], item_moved_to_end(my_list, 0))
    expected_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Original list stays the same', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Last Element', [1, 3, 4, 2, 15, 2, 16], item_moved_to_end(my_list, 6))
    expected_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Original list stays the same', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Middle Element', [1, 3, 4, 15, 2, 16, 2], item_moved_to_end(my_list, 3))
    expected_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Original list stays the same', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16, 14, 87, 2, 321, 1, 14, 23, 9]
    TEST('Large List', [1, 3, 4, 2, 15, 2, 16, 87, 2, 321, 1, 14, 23, 9, 14], item_moved_to_end(my_list, 7))
    expected_list = [1, 3, 4, 2, 15, 2, 16, 14, 87, 2, 321, 1, 14, 23, 9]
    TEST('Original list stays the same', expected_list, my_list)
    my_list = [3, 3, 3, 3]
    TEST('All Same', [3, 3, 3, 3], item_moved_to_end(my_list, 2))
    expected_list = [3, 3, 3, 3]
    TEST('Original list stays the same', expected_list, my_list)
    my_list = []
    TEST('Empty List', None, move_item_to_end(my_list, 2))
    expected_list = []
    TEST('Original list stays the same', expected_list, my_list)
    print('End item_moved_to_end_TEST')
    print()


def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('First Element', None, move_item_to_end(my_list, 0))
    expected_list = [3, 4, 2, 15, 2, 16, 1]
    TEST('First Element Succeed', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Last Element', None, move_item_to_end(my_list, 6))
    expected_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('Last Element Succeed', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16]
    TEST('In the Middle', None, move_item_to_end(my_list, 3))
    expected_list = [1, 3, 4, 15, 2, 16, 2]
    TEST('In the Middle Succeed', expected_list, my_list)
    my_list = [1, 3, 4, 2, 15, 2, 16, 14, 87, 2, 321, 1, 14, 23, 9]
    TEST('Large List', None, move_item_to_end(my_list, 7))
    expected_list = [1, 3, 4, 2, 15, 2, 16, 87, 2, 321, 1, 14, 23, 9, 14]
    TEST('Large List Succeed', expected_list, my_list)
    my_list = [3, 3, 3, 3]
    TEST('All Same', None, move_item_to_end(my_list, 2))
    expected_list = [3, 3, 3, 3]
    TEST('All Same Succeed', expected_list, my_list)
    my_list = []
    TEST('Empty List', None, move_item_to_end(my_list, 2))
    expected_list = []
    TEST('Original list stays the same', expected_list, my_list)








item_moved_to_end_TEST()
move_item_to_end_TEST()

