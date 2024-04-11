

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
    
    TEST(average([]) is None)
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    
    TEST(largest_element([]) is None)
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    
    TEST(all_equal([3,3,3]) == True)
    
    TEST(all_equal([2,3,3]) == False)
    
    TEST(all_equal([]) == True)
    
    TEST(all_equal([3]) == True)
    print('End all_equal_TEST')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    
    TEST(alternate_sum([1,2,3]) == 2)
    
    TEST(alternate_sum([-0.7,8,11.1,-6]) == 8.4)
    
    TEST(alternate_sum([]) == 0)
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    print('Start is_ordered_TEST')
    
    TEST(is_ordered([-1,1.3,2,3], True) == True)
    
    TEST(is_ordered([2.3,1,-3], True) == False)
    
    TEST(is_ordered([], True) == True)
    
    TEST(is_ordered([7], True) == True)
    
    TEST(is_ordered([1, 3, 3, 7], True) == False)
    
    TEST(is_ordered([1, 3, 3, 7], False) == True)
    print('End is_ordered_TEST')
    print()

def rotate_right_TEST():
    print('Start rotate_right_TEST')
    
    TEST(rotate_right([1,2,3]) == [3,1,2])
    
    
    TEST(rotate_right(['cat','dog',-7.7,'wolf','moon']) == ['moon','cat','dog',-7.7,'wolf'])
    
    TEST(rotate_right([]) == [])
    
    TEST(rotate_right(['elephant']) == ['elephant'])
    print('End is_ordered_TEST')
    print()

def weird_double_TEST():
    print('Start weird_double_TEST')
    
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    
    TEST(weird_double([1, 3, -2]) == [2, 3, -2])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2])
    TEST(weird_double([7, 6, 5, 4, 2, 3, 1]) == [14, 6, 5, 4, 2, 3, 1])
    
    TEST(weird_double([]) == [])
    
    TEST(weird_double([6]) == [6])
    print('End weird_double_TEST')
    print()

def merge_ordered_lists_TEST():
    print('merge_ordered_lists_TEST')
    
    TEST(merge_ordered_lists([1, 3, 7], [2, 4, 5])) == [1, 2, 3, 4, 5, 7]
    
    TEST(merge_ordered_lists([1, 3], [2, 2, 8])) == [1, 2, 2, 3, 8]
    
    TEST(merge_ordered_lists([], []) == [])
    
    TEST(merge_ordered_lists([6], []) == [6])
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
