



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
    TEST(approx_equal(average([-2,4,6,8]), 4))
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
    TEST(all_equal([3,3,3,3]) == True) 
    TEST(all_equal([2,2,3,2]) == False) 
    TEST(all_equal([4,4,4,7]) == False) 
    TEST(all_equal([1,2,2,2]) == False) 
    TEST(all_equal([]) == None) 
    print('End all_equal_TEST')
    print()


def alternate_sum_TEST(): 
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([3,4,7,2]) == 4) 
    TEST(alternate_sum([5,2,3]) == 6) 
    TEST(alternate_sum([1,3,2,7,8]) == 1)
    TEST(alternate_sum([2,4,3,5,4]) == 0)
    TEST(alternate_sum([]) == None)
    print('End alternate_sum_TEST')
    print()


def is_ordered_TEST(): 
    print('Start is_ordered_TEST')
    TEST(is_ordered([3,7,8,10],True) == True) 
    TEST(is_ordered([1,1,2,4],False) == True) 
    TEST(is_ordered([4,3,8,4],False) == False) 
    TEST(is_ordered([4,4,5,6],True) == False) 
    TEST(is_ordered([4,4,5,2],False) == False) 
    print('End is_ordered_TEST')
    print()


def rotate_right_TEST(): 
    print('Start rotate_right_TEST')
    TEST(rotate_right([3,7,8,9]) == [9,3,7,8])
    TEST(rotate_right([1,1,2,4]) == [4,1,1,2])
    TEST(rotate_right([4,3,8,4]) == [4,4,3,8])
    TEST(rotate_right([4,4,5,6]) == [6,4,4,5])
    
    TEST(rotate_right(['Alex','Brian','Lily','Harry']) == ['Harry','Alex','Brian','Lily'])
    print('End rotate_right_TEST')
    print()


def weird_double_TEST(): 
    print('Start weird_double_TEST')
    TEST(weird_double([1,4,3,6,5,4,7,8,5]) == [2,8,3,6,5,4,14,16,10])
    TEST(weird_double([2,3,4,5]) == [4,3,4,5])
    TEST(weird_double([4,5,3,4,2,6,11,7]) == [8,10,3,4,2,6,22,14])
    TEST(weird_double([3,2,3,4,2,3,1,8]) == [3,2,3,4,4,3,1,8])
    TEST(weird_double([2,4,6,5,2,2,4]) == [4,8,6,5,2,2,8])
    print('End weird_double_TEST')
    print()


def merge_ordered_lists_TEST(): 
    print('Start merge_ordered_lists_TEST')
    TEST(merge_ordered_lists([1,2,3],[5,6,7]) == [1,2,3,5,6,7])
    TEST(merge_ordered_lists([1,2,4],[3,5,6]) == [1,2,3,4,5,6])
    TEST(merge_ordered_lists([1,3,5],[2,4]) == [1,2,3,4,5])
    TEST(merge_ordered_lists([1,7],[3,6]) == [1,3,6,7])
    TEST(merge_ordered_lists([1,5],[2,6,7]) == [1,2,5,6,7])
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









