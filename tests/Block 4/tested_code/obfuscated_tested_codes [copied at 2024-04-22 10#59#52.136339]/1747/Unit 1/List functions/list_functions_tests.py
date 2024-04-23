

from list_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def count_number_larger_than_TEST():
    print('Start count_number_larger_than_TEST')
    TEST(count_number_larger_than(3, [1, 2, 5, 6]) == 2)
    TEST(count_number_larger_than(0, [10, -3, 4, 5, -1]) == 3)
    TEST(count_number_larger_than(3, []) == 0)
    TEST(count_number_larger_than(3, [3.1]) == 1)
    TEST(count_number_larger_than(3, [4, 3, 3, 1]) == 1)
    print('End count_number_larger_than_TEST')
    print()


def average_TEST():
    print('Start average_TEST')
    TEST(approx_equal(average([1.0, 3.0, 5.0]), 3))
    TEST(approx_equal(average([1, 2, 4]), 2.333333))
    TEST(approx_equal(average([-2]), -2))
    TEST(average([]) == None)
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    TEST(largest_element([]) == None)
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    
    TEST(all_equal([3, 3, 3, 3, 3]) == True)
    
    TEST(all_equal([3, 3, 3, 3, 4]) == False)
    
    TEST(all_equal([2, 3, 3, 3, 3]) == False)
    
    TEST(all_equal([3, 3, 10, 3, 3]) == False)
    
    TEST(all_equal([]) == True)
    print('End all_equal_TEST')
    print()


def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    
    TEST(alternate_sum([1, 2, 3, 4, 5, 6]) == 3)
    
    TEST(alternate_sum([1, 2, 3, 4, 5]) == -3)
    
    TEST(alternate_sum([6, 5, 4, 3, 2, 1]) == -3)
    
    TEST(alternate_sum([1, 10, 2, 9, 3]) == 13)
    
    TEST(alternate_sum([1]) == -1)
    
    TEST(alternate_sum([]) == None)
    print('End alternate_sum_TEST')
    print()


def is_ordered_TEST():
    print('Start is_ordered_TEST')
    
    TEST(is_ordered([1, 2, 3, 4, 5], True) == True)
    
    TEST(is_ordered([1, 2, 2, 3, 4], True) == False)
    
    TEST(is_ordered([1, 2, 1, 2, 3], True) == False)
    
    TEST(is_ordered([1], False) == True)
    
    TEST(is_ordered([], False) == True)
    
    TEST(is_ordered([1, 2, 3, 4, 5], False) == True)
    
    TEST(is_ordered([1, 2, 2, 3, 4], False) == True)
    
    TEST(is_ordered([1, 2, 1, 2, 3], False) == False)
    
    TEST(is_ordered([1], False) == True)
    
    TEST(is_ordered([], False) == True)
    print('End is_ordered_TEST')
    print()


def rotate_right_TEST():
    print('Start rotate_right_TEST')
    
    TEST(rotate_right([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4])
    
    TEST(rotate_right([1, 1, 4, 5]) == [5, 1, 1, 4])
    
    TEST(rotate_right([1]) == [1])
    
    TEST(rotate_right([]) == 'N/A')
    
    TEST(rotate_right(['a', 'b', 'c', 'd']) == ['d', 'a', 'b', 'c'])
    print('End rotate_right_TEST')
    print()

def weird_double_TEST():
    print('Start weird_double_TEST')
    
    TEST(weird_double([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 3, 4, 5, 6, 14, 16])
    
    TEST(weird_double([1, 2, 3, 4, 5]) == [2, 4, 3, 4, 5])
    
    TEST(weird_double([1, 2, 3, 4, 5, 6]) == [2, 4, 3, 4, 5, 6])
    
    TEST(weird_double([1, 2, 4, 5, 7]) == [2, 4, 8, 10, 14])
    print('End weird_double_TEST')
    print()

def merge_ordered_lists_TEST():
    print('Start merge_ordered_lists_TEST')
    
    TEST(merge_ordered_lists([1, 2, 5, 6, 8], [3, 4, 6, 8]))
    
    TEST(merge_ordered_lists([1, 2, 5, 6, 9], [3, 4, 6, 8]))
    
    TEST(merge_ordered_lists([3, 4, 6, 8], [1, 2, 5, 6, 9]))
    
    TEST(merge_ordered_lists([1, 2, 5, 6, 9, 11, 13], [3, 4, 6, 8]))
    
    TEST(merge_ordered_lists([3, 4, 6, 8], [1, 2, 5, 6, 9, 11, 13]))
    print('End merge_ordered_lists_TEST')
    print()



count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_lists_TEST()
