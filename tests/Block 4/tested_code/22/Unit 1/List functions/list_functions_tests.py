

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
    TEST(all_equal([100, 100, 100]) == True)
    TEST(all_equal([-3, -3, -3]) == True)
    TEST(all_equal([1, 1, 1, 100]) == False)
    TEST(all_equal([100, 1, 1]) == False)
    TEST(all_equal([-3, -100, 1]) == False)
    TEST(all_equal(['x', 'x', 'x']) == True)
    TEST(all_equal(['x', 'x', 4]) == False)
    TEST(all_equal([]) == True)
    print('End all_equal_TEST')
    print()


def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([1, 2, 3, 4, 5]) == 3)
    TEST(alternate_sum([0, 0, -1, -10, 5, 8]) == 6)
    TEST(alternate_sum([-5, -2, -9, -4]) == -8)
    TEST(alternate_sum([1]) == 1)
    TEST(alternate_sum([]) == 0)
    print('End alternate_sum_TEST')
    print()


def is_ordered_TEST():
    print('Start is_ordered_TEST')
    TEST(is_ordered([1, 3, 5, 7, 9], True) == True)
    TEST(is_ordered([-9, -4, -2, 1, 8], True) == True)
    TEST(is_ordered([1, 3, 7, 5, 9], True) == False)
    TEST(is_ordered([1, 3, 5, 5, 9], True) == False)
    TEST(is_ordered([1, 3, 5, 5, 9], False) == True)
    TEST(is_ordered([], False) == True)
    print('End alternate_sum_TEST')
    print()


def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1, 7, 8, 2, 0, 2]) == [2, 1, 7, 8, 2, 0,])
    TEST(rotate_right([4, 2, 'u', 2, 9]) == [9, 4, 2, 'u', 2])
    TEST(rotate_right(['meh', 'uh?', 'buebuebue']) == ['buebuebue', 'meh', 'uh?'])
    print('End rotate_right_TEST')
    print()


def weird_double_TEST():
    print('Start rotate_right_TEST')
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    TEST(weird_double([1, 3, -2]) == [2, 3, -2])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2])
    TEST(weird_double([7, 6, 5, 4, 2, 3, 1]) == [14, 6, 5, 4, 2, 3, 1])
    print('End weird_double_TEST')
    print()


def merge_ordered_lists_TEST():
    print('Start merge_ordered_lists_TEST')
    TEST(merge_ordered_lists([1, 3], [2, 2, 8]) == [1, 2, 2, 3, 8])
    TEST(merge_ordered_lists([-3, 0, 7, 9, 15, 21], [-13, 1, 7, 9]) == [-13, -3, 0, 1, 7, 7, 9, 9, 15, 21])
    TEST(merge_ordered_lists([-7, -3, 1, 7], []) == [-7, -3, 1, 7])
    TEST(merge_ordered_lists([], []) == [])
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

