


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
    TEST(average([])==None)
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    TEST(largest_element([0]) == 0)
    TEST(largest_element([]) == None)
    print('End largest_element_TEST')
    print()


def all_equal_TEST():
    print('Start all_equal_TEST')
    TEST(all_equal(['hi','hi','hi','hi']) == True) 

    TEST(all_equal([-15,-15,-15]) == True) 
    TEST(all_equal([-15, -15, -6, -15, -15]) == False)
    
    TEST(all_equal([1,1,1]) == True) 
    TEST(all_equal([1,2,2,2]) == False) 
                                        
    TEST(all_equal([3,3,3,4]) == False)
                                       
    TEST(all_equal([]) == None) 
    
    
    print('End all_equal_TEST')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([0,1,2]) == 1)
    TEST(alternate_sum([15,15,15]) == 15)
    TEST(alternate_sum([9,8,4]) == 5) 
    TEST(alternate_sum([0,0,0]) == 0)
    TEST(alternate_sum([1,2,2,2]) == -1)
    TEST(alternate_sum([5,3,3,4]) == 1)
    TEST(alternate_sum([]) == None) 
    
    
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    print('Start is_ordered_TEST')
    TEST(is_ordered([0,1,2], True) == True)
    TEST(is_ordered([0,1,1], True) == False) 
    TEST(is_ordered([0,1,1], False) == True)
    TEST(is_ordered([0,1,2,3,4], True) == True) 
    TEST(is_ordered([3,3,4,5], True) == False) 
                                                
    TEST(is_ordered([-5,-3,-2,-1,0], True) == True)
    TEST(is_ordered([-5,-3,-2,-1,0,0], True) == False) 
                                                       
    TEST(is_ordered([-5,-3,-2,-1,0,0], False) == True)
    TEST(is_ordered([], True) == None) 
    
    
    print('End is_ordered_TEST')
    print()
    
def rotate_right_TEST():
    print("Start rotate_right_TEST")
    TEST(rotate_right([0,1,2]) == [2,0,1])
    TEST(rotate_right([0,1,2,3]) == [3,0,1,2])
    TEST(rotate_right([0,1]) == [1,0])
    TEST(rotate_right(["hello","python","world"]) == ["world","hello","python"])
    
    TEST(rotate_right([0,0]) == [0,0])
    TEST(rotate_right([]) == [])
    print('End rotate_right_TEST')
    print()

def weird_double_TEST():
    print("Start weird_double_TEST")
    TEST(weird_double([1, 3, -2]) == [2, 3, -2]) 
    
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2]) 
    
    TEST(weird_double([7, 6, 5, 4, 2, 3, 1]) == [14, 6, 5, 4, 2, 3, 1])
    TEST(weird_double([]) == [])
    print('End weird_double_TEST')
    print()
  
def merge_ordered_lists_TEST():
    print("Start merge_ordered_lists_TEST")
    TEST(merge_ordered_lists([1, 3, 5],[2, 2, 8]) == [1, 2, 2, 3, 5, 8]) 
    
    TEST(merge_ordered_lists([1],[2, 2, 8]) == [1, 2, 2, 8])
    TEST(merge_ordered_lists([-1, 0, 1],[2, 2, 8]) == [-1, 0, 1, 2, 2, 8])
    TEST(merge_ordered_lists([0, 10, 18],[5, 12, 18]) == [0, 5, 10, 12, 18, 18])
    TEST(merge_ordered_lists([0, 0, 10],[2, 3, 5]) == [0, 0, 2, 3, 5, 10])
    TEST(merge_ordered_lists([0, 0, 10],[2, 3, 5, 20]) == [0, 0, 2, 3, 5, 10, 20])
    print("End merge_ordered_lists_TEST")


count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_lists_TEST()

