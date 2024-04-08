

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
    TEST(largest_element([]) == None)
    print('End largest_element_TEST')
    print()


 
def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    
    TEST(alternate_sum([4]) == 4)
    
    TEST(alternate_sum([4, 5, 6, 8, 10, 13, 2]) == -4)
    
    TEST(alternate_sum([4, 5, 8, 10, 13, 2]) == 8)
    
    TEST(alternate_sum([4, -3, -5, 13, 2]) == -9)
    
    TEST(alternate_sum([4, -3, -5, 13, 2]) == -9)
    
    TEST(alternate_sum([]) == None)
    print('End alternate_sum_TEST')
    print()


def rotate_right_TEST():
    print('Start rotate_right_TEST')
    
    TEST(rotate_right([]) == [])
    
    TEST(rotate_right([4]) == [4])
    
    TEST(rotate_right([4, 5, 6, 10, 13, 26]) == [26, 4, 5, 6, 10, 13])
    
    TEST(rotate_right([4, 5, 5, 5, 6, 8, 9, 9]) == [9, 4, 5, 5, 5, 6, 8, 9])
    
    TEST(rotate_right([4, 4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4, 4])
    print('End rotate_right_TEST')
    print()

def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1, 2, 3]) == [[1], [2], [3]])
    
    TEST(deal_3_hands([]) == [[], [], []])
    
    TEST(deal_3_hands([1, 2, 3, 7, 16, 3, 2, 61, 32]) == [[1, 7, 2], [2, 16, 61], [3, 3, 32]])
    
    TEST(deal_3_hands([1, 3]) == [[1], [3], []])
    
    TEST(deal_3_hands(['apple', 'banana', 'orange', 'melon']) ==[['apple', 'melon'], ['banana'], ['orange']])
    print('End deal_3_hands_TEST')
    print()


largest_element_TEST()
alternate_sum_TEST()
rotate_right_TEST()
deal_3_hands_TEST()
