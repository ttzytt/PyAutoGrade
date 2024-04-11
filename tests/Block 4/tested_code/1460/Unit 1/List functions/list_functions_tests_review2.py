

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
    TEST(all_equal([1,1]) == True)
    TEST(all_equal([1,0]) == False)
    TEST(all_equal([-1,1]) == False)
    TEST(all_equal([197432198743213423943493249298747943987432879874,
                    197432198743213423943493249298747943987432879874]) == True)
    TEST(all_equal([197432198743213423943493249298747943987432879874,
                    197432198743213423943493249298747943987432879873]) == False)
    TEST(all_equal([3.1415,3.1415]) == True)
    TEST(all_equal([3.1415,3.1414]) == False)
    TEST(all_equal([1,1,1,1,1]) == True)
    TEST(all_equal([1,1,1,1,0]) == False)
    TEST(all_equal(['apple', 'apple', 'apple']) == True)
    TEST(all_equal(['apple', 'banana', 'carrot']) == False)
    TEST(all_equal(['1',1,1,1,1]) == False)
    
    
    
    
    TEST(all_equal([1, True]) == False)
    TEST(all_equal([0]) == True)
    TEST(all_equal([]) == None)
    print('End all_equal_TEST')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([1,2,3,4,5]) == 3)
    TEST(alternate_sum([1,1,1,1,1]) == 1)
    TEST(alternate_sum([1.12]) == 1.12)
    TEST(alternate_sum([1,2]) == -1)
    TEST(alternate_sum([]) == 0)
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    print('Start is_ordered_TEST')
    TEST(is_ordered([1,2,3,4,5], True) == True)
    TEST(is_ordered([1,2,3,4,-1], False) == False)
    TEST(is_ordered([1,2,3,4,0], True) == False)
    TEST(is_ordered([1,1,1,1,1], False) == True)
    TEST(is_ordered([1,1,1,1,1], True) == False)
    
    
    TEST(is_ordered([1,1.0000000000001], True) == True)
    TEST(is_ordered([1], True) == True)
    TEST(is_ordered([1], False) == True)
    TEST(is_ordered([], False) == True)
    print('End is_ordered_TEST')
    print()

def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1,2,3,4,5]) == [5,1,2,3,4])
    TEST(rotate_right([1,1,1,1,1]) == [1,1,1,1,1])
    TEST(rotate_right([1]) == [1])
    TEST(rotate_right([1,1,1,1,2]) == [2,1,1,1,1])
    TEST(rotate_right([1,234.123,'amongus','😱','0b11101']) == ['0b11101',1,234.123,'amongus','😱'])
    TEST(rotate_right([]) == [])
    print('End rotate_right_TEST')
    print()




count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()
rotate_right_TEST()

