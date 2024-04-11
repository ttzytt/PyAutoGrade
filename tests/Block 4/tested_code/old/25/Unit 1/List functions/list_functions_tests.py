

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
    TEST(all_equal([-10, -10, -10, -10]) == True) 
    TEST(all_equal([3, 4, 5]) == False) 
    TEST(all_equal([6, 6]) == True) 
    TEST(all_equal([8, 6, 7, 7, 8]) == False) 
    TEST(all_equal([8, 8, 8, 8, 8, 8]) == True) 
    TEST(all_equal([]) == None) 
    TEST(all_equal(['cat', 'cat', 'cat']) == True) 
    TEST(all_equal([8, '8']) == False) 
    TEST(all_equal([8, 8, 8, 7, 8, 8, 8]) == False) 
    TEST(all_equal([7, 8, 8, 8, 8, 8]) == False) 
    TEST(all_equal([8, 8, 8, 8, 8, 7]) == False) 
    print('End all_equal_TEST')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([1, 2, 3, 4]) == -2)
    TEST(alternate_sum([2, 1, 1, 2]) == 0)
    TEST(alternate_sum([10, 1, 3, 2]) == 10)
    TEST(alternate_sum([21, 100, 100, 3]) == 18)
    TEST(alternate_sum([3, 5, 2, 5, 3, 4, 5]) == -1) 
    TEST(alternate_sum([]) == 0)
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    print('Start is_ordered_TEST')
    TEST(is_ordered([1, 3, 3, 7], True) == False)
    TEST(is_ordered([1, 3, 3, 7], False) == True)
    TEST(is_ordered([1, 2, 3, 4, 5], False) == True)
    TEST(is_ordered([1, 3, 2, 7], True) == False)
    TEST(is_ordered([1, 2, 2, 3, 4, 4, 5, 7, 6], False) == False) 
    TEST(is_ordered([0, 3, 2, 2], False) == False) 
    TEST(is_ordered([-1, -1, -2, -3, -4], False) == False)
    TEST(is_ordered([-5, -3, -2, 1, 3], True) == True)
    TEST(is_ordered([-2, -1, -1, 0, 1, 2, 3, 3, 4], False) == True)
    TEST(is_ordered([1], True) == None) 
    TEST(is_ordered([1], False) == None)
    TEST(is_ordered([], True) == None)
    TEST(is_ordered([], False) == None)
    print('End is_ordered_TEST')
    print()

def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4])
    TEST(rotate_right([1, 2, 3, 4]) == [4, 1, 2, 3])
    TEST(rotate_right([1, 2, 222, 2, 3, 4, 4]) == [4, 1, 2, 222, 2, 3, 4])
    TEST(rotate_right([2, 5, 3, 4, 6, 9, 5, 6]) == [6, 2, 5, 3, 4, 6, 9, 5])
    TEST(rotate_right([1, 11, 111, 1111, 11111]) == [11111, 1, 11, 111, 1111])
    TEST(rotate_right([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2])
    TEST(rotate_right(['chicken', 'tenders', 'Crispy']) == ['Crispy', 'chicken', 'tenders'])
        
    TEST(rotate_right([]) == None)
        
    TEST(rotate_right([1]) == [1])
        
    print()

def weird_double_TEST():
    print('Start weird_double_TEST')
    TEST(weird_double([1, 4, 2]) == [2, 8, 4])
    TEST(weird_double([1, 3, 2, 5, 6, 7]) == [2, 3, 2, 5, 6, 14])
    print()

def merge_ordered_list_TEST():
    print('Start merge_ordered_list_TEST')
    TEST(merge_ordered_list([1, 2, 3], [3, 4, 5, 7]) == [1, 2, 3, 3, 4, 5, 7])
    TEST(merge_ordered_list([1, 3, 5], [2, 2, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 5, 6, 7])
    TEST(merge_ordered_list([3, 5, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10])
    print()


count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_list_TEST()

