

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
    
    print('FAIL: Need to test empty list.')
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    
    print('FAIL: Need to test empty list.')
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    TEST(all_equal([1, 1, 1, 1]) == True)
    TEST(all_equal([5, 5, 5, 5]) == True)
    TEST(all_equal([10, 9, 8, 7]) == False)
    TEST(all_equal([]) == None)
    print('End all_equal_TEST') 
    print()


def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([0, 2, 2, 3]) == -3)
    TEST(alternate_sum([5, 3, 6, 9]) == -1)
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([8, 8, 5, 6, 1]) == 0)
    print('End alternate_sum_TEST')

def is_ordered_TEST():
    print('Start is_ordered')
    TEST(is_ordered([0, 1, 2, 3], True) == True)
    TEST(is_ordered([4, 5, 6, 6], True) == False)
    TEST(is_ordered([7, 8, 7, 3], False) == False)
    TEST(is_ordered([], False) == None)

count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()

