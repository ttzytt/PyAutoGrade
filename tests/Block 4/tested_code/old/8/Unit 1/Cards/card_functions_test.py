

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
    
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    TEST(deal_3_hands([]) == [[], [], []])
    print('End deal_3_hands_TEST')
    print()

def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what(['skip', '2', '3', '4']) == [['skip', '4'], [], ['2'], ['3']])
    TEST(uno_who_played_what(['1', 'reverse', '3', '4']) == [['1', '3'], ['reverse'], [], ['4']])
    TEST(uno_who_played_what(['1', 'reverse', 'reverse', '4']) == [['1', 'reverse'], ['reverse', '4'], [], []])
    TEST(uno_who_played_what(['1', 'skip', 'skip', '4']) == [['1',], ['skip', '4'], [], ['skip']])
    TEST(uno_who_played_what([]) == [[], [], [], []])
    print('End uno_who_played_what_TEST')
    print()
    

deal_3_hands_TEST()
uno_who_played_what_TEST()
