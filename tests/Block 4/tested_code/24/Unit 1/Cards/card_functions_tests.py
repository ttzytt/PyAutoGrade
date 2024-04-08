

from card_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')
        



def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([]) == [[], [], []])
    TEST(deal_3_hands([1, 2, 3]) == [[1], [2], [3]])
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    TEST(deal_3_hands(['a', 'b', 'c', 'd']) == [['a', 'd'], ['b'], ['c']])
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what([]) == [[], [], [], []])
    TEST(uno_who_played_what(['reverse', 'reverse', 'reverse', 'reverse']) == [['reverse', 'reverse'], [], [], ['reverse', 'reverse']])
    TEST(uno_who_played_what(['skip', 3, 'skip', 7, 'skip', 10]) == [['skip', 10], [7], [3, 'skip'], ['skip']])
    TEST(uno_who_played_what([1, 2, 3, 4, 5]) == [[1, 5], [2], [3], [4]])
    TEST(uno_who_played_what(['reverse', 1, 2, 3, 'reverse', 4, 5, 6]) == [['reverse', 'reverse'], [3, 4], [2, 5], [1, 6]])
    print('End uno_who_played_this_TEST')
    print()



    



deal_3_hands_TEST()
uno_who_played_what_TEST()
