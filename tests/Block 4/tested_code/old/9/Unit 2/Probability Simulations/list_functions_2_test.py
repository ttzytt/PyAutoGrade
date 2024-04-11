




from list_functions_2 import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def largest_TEST():
    print('Start largest_TEST')
    TEST(largest([1, 3, 5]) == 5)
    TEST(largest([3, 0, -4]) == 3)
    TEST(largest([-10, -3, -5, -9]) == -3)
    TEST(largest([-10]) == -10)
    TEST(largest([1,3,2,7,4,5]) == 7)
    print('End largest_TEST')
    print()

def alternate_sum_TEST():
    print('Start alternate_sum_TEST')
    TEST(alternate_sum([3,4,7,2]) == 4) 
    TEST(alternate_sum([5,2,3]) == 6) 
    TEST(alternate_sum([1,3,2,7,8]) == 1)
    TEST(alternate_sum([2,4,3,5,4]) == 0)
    TEST(alternate_sum([1,2,3,4,5,6]) == -3)
    print('End alternate_sum_TEST')
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

def deal_3_hands_TEST(): 
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1,2,3,4,5,6]) == ([1,4],[2,5],[3,6]))
    TEST(deal_3_hands([1,3,4,2,3,8,3,1]) == ([1,2,3],[3,3,1],[4,8]))
    TEST(deal_3_hands([1,5,3,2,5,4,6]) == ([1,2,6],[5,5],[3,4]))
    
    (TEST(deal_3_hands(['I','LOVE','YOU','MY','DEAR','MOM'])
         == (['I','MY'],['LOVE','DEAR'],['YOU','MOM'])))
    (TEST(deal_3_hands(['A','B','C','D','E','F','G'])
          == (['A','D','G'],['B','E'],['C','F'])))
    print('End deal_3_hands_TEST')
    print()





largest_TEST()
alternate_sum_TEST()
rotate_right_TEST()
deal_3_hands_TEST()
