




from card_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001






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


def uno_who_played_what_TEST():
    print('Start uno_who_played_what')
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7' ]) == [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    TEST(uno_who_played_what(['skip', '6', '7' ]) == [['skip'], [], ['6'], ['7']])
    TEST(uno_who_played_what(['2', '4', '6', '8']) == [['2'], ['4'], ['6'], ['8']])
    print('End uno_who_played_what')
    print()



deal_3_hands_TEST()
uno_who_played_what_TEST()

