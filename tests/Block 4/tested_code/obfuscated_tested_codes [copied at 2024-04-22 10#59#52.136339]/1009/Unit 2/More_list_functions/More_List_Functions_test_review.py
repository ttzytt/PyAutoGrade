








from MoreListFunctions import *


def test_item_moved_to_end():
    
    original_list_1 = [1, 2, 3, 4, 5]
    index_1 = 2
    expected_result_1 = [1, 2, 4, 5, 3]
    actuall_result_1 = item_moved_to_end(original_list_1, index_1)
    
    
    if actuall_result_1 == expected_result_1:
        print("Test case 1: Pass")
    else:
        print("Test case 1: Fail")

    
    original_list_2 = ["apple", "banana", "peach", "grape", "pear"]
    index_2 = 4
    expected_result_2 = ["apple", "banana", "peach", "grape", "pear"]
    actuall_result_2 = item_moved_to_end(original_list_2, index_2)
    
    if actuall_result_2 == expected_result_2:
        print("Test case 2: Pass")
    else:
        print("Test case 2: Fail")

    
    original_list_3 = [1, 2, 3, 4, 5]
    index_3 = 5
    expected_result_3 = "INVALID INDEX"
    actuall_result_3 = item_moved_to_end(original_list_3, index_3)
    
    if actuall_result_3 == expected_result_3:
        print("Test case 3: Pass")
    else:
        print("Test case 3: Fail")


def test_move_item_to_end():
    
    original_list_1 = [1, 2, 3, 4, 5]
    index_1 = 3
    
    expected_result_1 = [1, 2, 3, 5, 4]
    actuall_result_1 = move_item_to_end(original_list_1, index_1)
    
    if original_list_1 == expected_result_1:
        print("Test case 1: Pass")
    else:
        print("Test case 1: Fail")

    
    original_list_2 = [1, 2, 3, 4, 5]
    index_2 = 6
    expected_result_2 = "INVALID INDEX"
    actuall_result_2 = move_item_to_end(original_list_2, index_2)
    if actuall_result_2 == expected_result_2:
        print("Test case 2: Pass")
    else:
        print("Test case 2: Fail")


test_item_moved_to_end()
test_move_item_to_end()

    
