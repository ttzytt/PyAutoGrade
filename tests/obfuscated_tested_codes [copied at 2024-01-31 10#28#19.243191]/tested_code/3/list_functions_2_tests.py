

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
    TEST(largest_element([-10]) == -10)
    print('End largest_element_TEST')
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



def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1, 3, 5, 9, 7]) == [7, 1, 3, 5, 9])
    TEST(rotate_right([1, 8, 9, 18, 21]) == [21, 1, 8, 9, 18])
    TEST(rotate_right([1, 5, 3, 7, 9]) == [9, 1, 5, 3, 7])
    TEST(rotate_right(['a', 'b', 'c', 'd']) == ['d', 'a', 'b', 'c'])
    TEST(rotate_right([4, 2,]) == [2, 4])
    print('End rotate_right_TEST')
    print()

def deal_3_hands_TEST():
    print('Start deal_3_hands')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    TEST(deal_3_hands([8, 29]) == [[8], [29], []])  
    TEST(deal_3_hands([1, 4, 9]) == [[1], [4], [9]])  
    TEST(deal_3_hands([8]) == [[8], [], []])
    TEST(deal_3_hands(['skip']) == [['skip'], [], []])
    TEST(deal_3_hands([8, 9, 10, 11]) == [[8, 11], [9], [10]])
    print('End deal_3_hands')
    print()








largest_element_TEST()

alternate_sum_TEST()

rotate_right_TEST()

deal_3_hands_TEST()
