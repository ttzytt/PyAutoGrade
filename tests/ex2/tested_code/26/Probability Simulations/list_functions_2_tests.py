

from list_functions_2 import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10) 
    TEST(largest_element([]) == "Empty list")
    print('End largest_element_TEST') 
    print()


def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([3, 2, 5, 6, 1, 4]) == -3)
    
    TEST(alternate_sum([2, 2, 2, 2]) == 0)
    
    TEST(alternate_sum([2, 2, 2, 2, 2]) == 2)
    TEST(alternate_sum([3, 2, 5, 6, 1,]) == 1)
    
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([2]) == 2)
    TEST(alternate_sum([0, 2]) == -2)
    print('End alternate_sum_TEST')
    print()


def rotate_right_TEST():
    print('Start rotate_right_TEST')
    
    TEST(rotate_right([1, 2, 3, 4, 5, 6]) == [6, 1, 2, 3, 4, 5])
    TEST(rotate_right([3, 2, 5, 7, 2, 7]) == [7, 3, 2, 5, 7, 2])
    
    TEST(rotate_right(['hi', 'bye', 'stop', 'go', 'daniel']) ==
         ['daniel', 'hi', 'bye', 'stop', 'go'])
    
    TEST(rotate_right([4.2, 6.7, 1.5, 2.7, 5.6]) == [5.6, 4.2, 6.7, 1.5, 2.7])
    
    TEST(rotate_right(['hi', 3, 'stop', 3.1, -1]) ==
         [-1, 'hi', 3, 'stop', 3.1])
    
    TEST(rotate_right([1, 2]) == [2, 1])
    TEST(rotate_right([1]) == [1])
    TEST(rotate_right([]) == [])
    print('End rotate_right_TEST')
    print()


def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    
    TEST(deal_3_hands(['J', 'A', 9, 3, 'Q', 4, 2, 'Joker']) == \
                      [['J', 3, 2], ['A', 'Q', 'Joker'], [9, 4]])
    
    TEST(deal_3_hands([]) == [[], [], []])
    TEST(deal_3_hands([2]) == [[2], [], []])
    TEST(deal_3_hands([2, 4]) == [[2], [4], []])
    TEST(deal_3_hands([2, 4, 'K']) == [[2], [4], ['K']])
    print('End deal_3_hands_TEST')
    print()


    


largest_element_TEST()

alternate_sum_TEST()

rotate_right_TEST()

deal_3_hands_TEST()
