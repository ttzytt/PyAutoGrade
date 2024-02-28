

from card_functions import *





def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([-3, 3, 10, 4, 8]) == [[-3, 4], [3, 8], [10]])
    TEST(deal_3_hands([1]) == [[1], [], []])
    TEST(deal_3_hands([]) == [[], [], []])
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7' ])
         == [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    TEST(uno_who_played_what([1, 3, 9, 'reverse', 9, 2, 'reverse', 5, 'skip', 9])
         == [[1, 'reverse', 9], [3, 2, 5], [9, 9, 'skip'], ['reverse']])
    print('End uno_who_played_what_TEST')
    print()
    




deal_3_hands_TEST()
uno_who_played_what_TEST()
