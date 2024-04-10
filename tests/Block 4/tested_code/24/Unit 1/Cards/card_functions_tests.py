



from card_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6]) == [[1, 4], [2, 5], [3, 6]])
    
    TEST(deal_3_hands([1, 3, 5, 6, 7]) == [[1, 6], [3, 7], [5]])
    
    TEST(deal_3_hands([]) == [[], [], []])
    
    TEST(deal_3_hands([-2, -1, 4, 6, 7]) == [[-2, 6], [-1, 7], [4]])
    
    TEST(deal_3_hands(['Apple', 'Banana', 'Cherry', 'Orange'])
             == [['Apple', 'Orange'] , ['Banana'] , ['Cherry']])
    print('End merge_ordered_lists_TEST')
    print()

def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST()')
    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', 'reverse', '8'])
             == [['1', '5'], ['2', '6', '8'], ['3', 'reverse'], ['4']])
    
    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', 'skip', '8'])
             == [['1', '5', '8'], ['2', '6',], ['3', 'skip'], ['4']])

    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', 'reverse', '8'])
             == [['1', '5', 'reverse'], ['2', 'reverse', '8'], ['3'], ['4']])

    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', 'reverse', '8'])
             == [['1', '5'], ['2', 'skip'], ['3', '8'], ['4', 'reverse']])
    
    print('End uno_who_played_what_TEST()')
    print()
    

deal_3_hands_TEST()
uno_who_played_what_TEST()

