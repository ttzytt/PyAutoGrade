

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
    TEST(deal_3_hands([1,2,3,4,5,6,7]) == [[1,4,7], [2,5], [3,6]])
    TEST(deal_3_hands([]) == [[], [], []])
    TEST(deal_3_hands(['a', 'b', 'c', 'd', 'e', 'f']) == [['a', 'd'],['b', 'e'],['c', 'f']])
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what([]) == 0)
    TEST(uno_who_played_what(['1','2','3','4','5','skip','7']) == [['1','5'],['2','skip'],['3'],['4','7']])
    TEST(uno_who_played_what(['1', 'reverse', '3', '4', '5']) == [['1', '3'],['reverse'],['5'],['4']])
    print('End uno_who_played_what_TEST')
    print()


deal_3_hands_TEST()
uno_who_played_what_TEST()
