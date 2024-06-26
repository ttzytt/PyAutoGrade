

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
    TEST(approx_equal(average([1, 2, 4]), 2.33333))
    TEST(approx_equal(average([-2]), -2))
    TEST(approx_equal(average([0]), 0))
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    TEST(largest_element([-10]) == -10)
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    
    TEST(all_equal([]) == True)
    
    TEST(all_equal([5]) == True)
    
    TEST(all_equal([9, 4]) == False)
    
    TEST(all_equal([1, 1, 1]) == True)
    
    TEST(all_equal([5, 8, 8, 8]) == False)
    
    TEST(all_equal([6, 6, 9, 6, 6]) == False)
    
    TEST(all_equal(['a', 'a', 'a']) == True)
    TEST(all_equal([-10, -3, -5, -9]) == False)
    
    TEST(all_equal([-9, -9, -9]) == True)
    print('End all_equal_TEST')
    print()


def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([1, 3, 5]) == 3)
    TEST(alternate_sum([3, 18, 4]) == -11)
    TEST(alternate_sum([-10, -3, -5, -9]) == -3)
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([2, 4, 6]) == 4)
    TEST(alternate_sum([3, 7, -18, 9, 3]) == -28)
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    print('Start is_ordered_TEST')
    TEST(is_ordered([1, 3, 5, 9, 7], False) == False)
    TEST(is_ordered([1, 8, 9, 18, 21], False) == True)
    TEST(is_ordered([1, 5, 3, 7, 9], False) == False)
    TEST(is_ordered([-9, -7, -3, 6], False) == True)
    TEST(is_ordered([5, 5, 5], False) == True)
    TEST(is_ordered([1, 3, 5, 9, 7], True) == False)
    TEST(is_ordered([1, 8, 9, 18, 21], True) == True)
    TEST(is_ordered([1, 5, 3, 7, 9], True) == False)
    TEST(is_ordered([-9, -7, -3, 6], True) == True)
    TEST(is_ordered([5, 5, 5], True) == False)
    print('End is_ordered_TEST')
    print()

def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1, 3, 5, 9, 7]) == [7, 1, 3, 5, 9])
    TEST(rotate_right([1, 8, 9, 18, 21]) == [21, 1, 8, 9, 18])
    TEST(rotate_right([1, 5, 3, 7, 9]) == [9, 1, 5, 3, 7])
    TEST(rotate_right(['a', 'b', 'c', 'd']) == ['d', 'a', 'b', 'c'])
    TEST(rotate_right([4, 2,]) == [2, 4])
    print('End rotate_right_TEST')
    print()



def weird_double_TEST():
    print('Start weird_double_TEST')
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    TEST(weird_double([1, 3, -2]) == [2, 3, -2])
    TEST(weird_double([1, 4, 8]) == [2, 8, 16])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2])
    TEST(weird_double([7, 6, 5, 4, 2, 3, 1]) == [14, 6, 5, 4, 2, 3, 1])
    print('End weird_double_TEST')
    print()

def merge_ordered_lists_TEST():
    print('Start merge_ordered_lists_TEST')
    TEST(merge_ordered_lists([1, 2, 5], [3, 6, 9]) == [1, 2, 3, 5, 6, 9])
    TEST(merge_ordered_lists([2, 3, 5], [3, 4, 5]) == [2, 3, 3, 4, 5, 5])
    TEST(merge_ordered_lists([8, 13, 30, 45, 58], [3, 6, 60]) == [3, 6, 8, 13, 30, 45, 58, 60])
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
