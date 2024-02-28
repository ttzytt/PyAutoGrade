

from list_functions import *








def TEST(condition, test_name="Test Case"):
    if condition:
        print(f"{test_name} Passed")
    else:
        print(f"{test_name} Failed")




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def count_number_larger_than_TEST():
    print('Start count_number_larger_than_TEST')
    TEST(count_number_larger_than(3, [1, 2, 5, 6]) == 2, "Test Case 1")
    TEST(count_number_larger_than(0, [10, -3, 4, 5, -1]) == 3, "Test Case 2")
    TEST(count_number_larger_than(3, []) == 0, "Test Case 3")
    TEST(count_number_larger_than(3, [3.1]) == 1, "Test Case 4")
    TEST(count_number_larger_than(3, [4, 3, 3, 1]) == 1, "Test Case 5")
    print('End count_number_larger_than_TEST')
    print()

def average_TEST():
    print('Start average_TEST')
    TEST(approx_equal(average([1.0, 3.0, 5.0]), 3), "Test Case 1")
    TEST(approx_equal(average([1, 2, 4]), 2.333333), "Test Case 2")
    TEST(approx_equal(average([-2]), -2), "Test Case 3")
    
    print('FAIL: Need to test empty list.')
    print('End average_TEST')
    print()

def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5, "Test Case 1")
    
    TEST(largest_element([3, 0, -4]) == 3, "Test Case 2")
    
    TEST(largest_element([-10, -3, -5, -9]) == -3, "Test Case 3")
    TEST(largest_element([-10]) == -10, "Test Case 4")
    
    print('FAIL: Need to test empty list.')
    print('End largest_element_TEST')
    print()

def all_equal_TEST():
    
    result = all_equal([1, 1, 1, 1])
    TEST(result, "Test Case 1")

    
    result = not all_equal([1, 2, 3, 4])
    TEST(result, "Test Case 2")

    
    result = all_equal([])
    TEST(result, "Test Case 3")

    
    result = all_equal([42])
    TEST(result, "Test Case 4")

    print("all_equal_TEST: All test cases passed!")

def test_alternate_sum():
    
    assert alternate_sum([]) == 0  

    
    assert alternate_sum([1, 2, 3, 4]) == 2  

    
    assert alternate_sum([1, 2, 3, 4, 5]) == 3  

    
    assert alternate_sum([1]) == 1  

    
    assert alternate_sum([0, 1]) == -1  

def is_ordered_TEST():
    
    TEST(is_ordered([1, 2, 3, 4], is_strict=True), "Test Case 1")
    
    TEST(is_ordered([1, 2, 3, 3, 4], is_strict=False), "Test Case 2")
    
    TEST(is_ordered([42], is_strict=True), "Test Case 3")
    
    TEST(is_ordered([], is_strict=False), "Test Case 4")
    
    TEST(not is_ordered([4, 3, 2, 1], is_strict=False), "Test Case 5")
    
    TEST(not is_ordered([1, 3, 3, 7], is_strict=True), "Test Case 6")
    
    TEST(is_ordered([1, 3, 3, 7], is_strict=False), "Test Case 7")

    print("is_ordered_TEST: All test cases passed!")

def rotate_right_TEST():
    
    original_list = [1, 2, 3, 4, 5]
    rotated_list = rotate_right(original_list)
    TEST(rotated_list == [5, 1, 2, 3, 4], "Test Case 1")
    
    empty_list = []
    rotated_empty_list = rotate_right(empty_list)
    TEST(rotated_empty_list == [], "Test Case 2")
    
    single_element_list = [42]
    rotated_single_element_list = rotate_right(single_element_list)
    TEST(rotated_single_element_list == [42], "Test Case 3")

    print("rotate_right_TEST: All test cases passed!")

def weird_double_TEST():
    
    TEST(weird_double([1, 1, 1]) == [2, 2, 2], "Test Case 1")
    
    TEST(weird_double([1, 3, -2]) == [2, 3, -2], "Test Case 2")
    print("weird_double_TEST: All test cases passed!")

def merge_ordered_lists_TEST():
    
    ordered_numbers_1 = [1, 3, 5, 7, 9]
    ordered_numbers_2 = [2, 4, 6, 8, 10]
    result = merge_ordered_lists(ordered_numbers_1, ordered_numbers_2)
    TEST(result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test Case 1")
    
    ordered_numbers_1 = [1, 3, 5, 7, 9]
    ordered_numbers_2 = [3, 4, 6, 8, 10]
    result = merge_ordered_lists(ordered_numbers_1, ordered_numbers_2)
    TEST(result == [1, 3, 4, 5, 6, 7, 8, 9, 10], "Test Case 2")

    print("merge_ordered_lists_TEST: All test cases passed!")



count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
test_alternate_sum()
is_ordered_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_lists_TEST()
