


from list_functions import *






def approx_equal(a, b):
    return abs(a - b) < 0.0001





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
    my_list = [3, 4, 6, 7]
    expected_my_list = my_list
    TEST('regular move index to end in new list', [3, 6, 7, 4], item_moved_to_end(my_list, 1))
    TEST("Don't change original list", expected_my_list, my_list)
    my_list = []
    expected_my_list = my_list
    TEST('move index to end in empty list', [], item_moved_to_end(my_list, 0))
    TEST("Don't change original list", expected_my_list, my_list)
    my_list = [4, 4, 4, 4]
    expected_my_list = my_list
    TEST('All the same values', [4, 4, 4, 4], item_moved_to_end(my_list, 2))
    TEST("Don't change original list", expected_my_list, my_list)
    my_list = [5, 7, 9, 0]
    expected_my_list = my_list
    TEST('move first index to end', [7, 9, 0, 5], item_moved_to_end(my_list, 0))
    TEST("Don't change original list", expected_my_list, my_list)
    my_list = [7, 7, 8, 9]
    expected_my_list = my_list
    TEST('move last index to end', [7, 7, 9, 8], item_moved_to_end(my_list, 3))
    TEST("Don't change original list", expected_my_list, my_list)

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')
    my_list = [3, 4, 6, 7]
    TEST('No return value', None, move_item_to_end(my_list, 1))
    TEST("Change original list", [3, 6, 7, 4], my_list)
    my_list = []
    TEST('No return value', None, move_item_to_end(my_list, 0))
    TEST("Empty list", [], my_list)
    my_list = [7]
    TEST('No return value', None, move_item_to_end(my_list, 0))
    TEST("Change original one index list", [7], my_list)
    my_list = [7, 8, 9, 10]
    TEST('No return value', None, move_item_to_end(my_list, 2))
    TEST("Change original list", [7, 8 ,10, 9], my_list)
    my_list = [3, 4, 55, 78]
    TEST('No return value', None, move_item_to_end(my_list, 3))
    TEST("Change original list last index", [3, 4, 55, 78], my_list)
    


item_moved_to_end_TEST()
print()
move_item_to_end_TEST()


