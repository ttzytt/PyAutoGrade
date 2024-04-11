




from card_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001






def deal_3_hands_TEST():
    print ('Start deal_3_hands')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    TEST(deal_3_hands([5, 23]) == [[5], [23], []])
    TEST(deal_3_hands([]) == [[], [], []])
    TEST(deal_3_hands([7]) == [[7], [], []])
    TEST(deal_3_hands(['skip']) == [['skip'], [], []])
    print ('End deal_3_hands')
    print()

def uno_who_played_what_TEST():
    print('Start uno_who_played_what')
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7' ]) == [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    TEST(uno_who_played_what(['skip', 'skip', '7' ]) == [['skip', '7'], [], ['skip'], []])
    TEST(uno_who_played_what([]) == [[], [], [], []])
    print('End uno_who_played_what')
    print()

'''
def uno_who_played_what_Bonus_TEST():
    print('Start uno_who_played_what_Bonus_TEST')
    (TEST(uno_who_played_what_Bonus(['1', '2', '3', '4', '5', 'skip', '7' ], 6, 3)
         == [['5'], ['skip'], ['1'], ['2', '7'], ['3'], ['4']]))
    print()
'''


deal_3_hands_TEST()
uno_who_played_what_TEST()

