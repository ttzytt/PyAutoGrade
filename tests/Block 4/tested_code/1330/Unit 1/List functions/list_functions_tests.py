 



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
    TEST(average([]) == False)
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    TEST(all_equal([-1, -1, -5, -1]) == False)
    TEST(all_equal([66, 66, 66]) == True)
    TEST(all_equal([]) == False)
    TEST(all_equal([6]) == True)
    TEST(all_equal(['1', '1', '1']) == False)
    TEST(all_equal([-66, 66, 66]) == False)
    print('End all_equal_TEST')
    print()


def is_ordered_TEST():
    print('Start is_ordered')
    TEST(is_ordered([2, 4, 154, 32, 1], False))
    TEST(is_ordered([-23, -12, -5, -3, 2], True))
    TEST(is_ordered([-5, 3, -2, 52, 5], False))
    TEST(is_ordered([23, 466, 3572, 12544], True))
    TEST(is_ordered([1, 3, 3, 7], True))
    TEST(is_ordered([6], True))
    TEST(is_ordered(['1', '2', '3'], False))
    TEST(is_ordered([], False))
    print('End is_ordered')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum')
    TEST(alternate_sum([1, 2, 3, 4, 5]) == 3)
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([-23, -12, -5, -3, 2]) == -11)
    print('End alternate_sum')
    print()

def rotate_right_TEST():
    print('Start rotate_right')
    TEST(rotate_right([4, 2, 3]) == [3, 4, 2])
    TEST(rotate_right([33, 0, -5, 3]) == [3, 33, 0, -5])
    TEST(rotate_right([]) == [])
    print('End rotate_right')
    print()

def weird_double_TEST():
    print('Start weird_double')
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    TEST(weird_double([1, 3, -2]) == [2, 3, -2])
    TEST(weird_double([63, 5, 19, 22, 1, 3]) == [63, 5, 19, 22, 2, 3])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2])
    print('End weird_double')
    print()

def merge_ordered_lists_TEST():
    print('Start merge_ordered_lists')
    TEST(merge_ordered_lists([1, 3], [2, 2, 8]) == [1, 2, 2, 3, 8])
    TEST(merge_ordered_lists([], [22, 1, 7, 34, 21]) == [1, 7, 21, 22, 34])
    print('End merge_ordered_lists')
    print()
    


count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
is_ordered_TEST()
alternate_sum_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_lists_TEST()
    
