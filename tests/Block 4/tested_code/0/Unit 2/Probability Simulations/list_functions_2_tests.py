

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
    TEST(alternate_sum([1,2,3,4,5,6]) == -3)
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([-3,-4,-5,-6,-7,-8]) == 3)
    TEST(alternate_sum([10,20,21,23,30]) == 18)
    TEST(alternate_sum([1,1,1,1,1]) == 1)
    print()
    
         
def rotate_right_TEST():
    print('Start rotate_right_TEST')
    TEST(rotate_right([1,2,3,4]) == [4,1,2,3])
    TEST(rotate_right([2,2,2,2]) == [2,2,2,2])
    
    TEST(rotate_right(['hi','hi','no']) == ['no','hi','hi'])
    
    TEST(rotate_right([]) == [])
    TEST(rotate_right([2]) == [2])
    print('End rotate_right_TEST')
    print()
    
def deal_3_hands_TEST():
    print('deal_3_hands_TEST Start')
    TEST(deal_3_hands([1,2,3,4,5,6,7]) == ([[1,4,7],[2,5],[3,6]]))
    TEST(deal_3_hands([]) == [[],[],[]])
    TEST(deal_3_hands([1]) == [[1],[],[]])
    TEST(deal_3_hands(['Ace','queen','king','jake','joker']) == [['Ace','jake'],['queen','joker'],['king']])
    print('deal_3_hands_TEST End')
    print()








largest_element_TEST()
alternate_sum_TEST()
rotate_right_TEST()
deal_3_hands_TEST()



