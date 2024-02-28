from card_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1, 'apple', 23]) == ([[1], ['apple'], [23]]))
    TEST(deal_3_hands([1, 10, 12, 14, 20, 19, 21, 13]) == ([[1, 14, 21], [10, 20, 13], [12, 19]]))

    
    TEST(deal_3_hands([1, 2]) == ([[1], [2], []]))
    TEST(deal_3_hands([1]) == ([[1], [], []]))
    TEST(deal_3_hands([]) == ([[], [], []]))
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_v2_TEST():
    print('Start uno_who_played_what_v2_TEST')
    
    TEST(uno_who_played_what_v2(['reverse', '1', 'skip', '2', '3', '10']) == (
        [['reverse', '2'], [], ['skip', '10'], ['1', '3']]))
    TEST(uno_who_played_what_v2(['reverse', '1', 'reverse', 'skip', '2', '3']) == (
        [['reverse'], ['2'], ['reverse', '3'], ['1', 'skip']]))

    
    TEST(uno_who_played_what_v2(['reverse', 'reverse', 'reverse', 'reverse', 'reverse']) == (
        [['reverse', 'reverse', 'reverse'], [], [], ['reverse', 'reverse']]))
    TEST(uno_who_played_what_v2(['skip', 'skip', 'skip', 'skip']) == (
        [['skip', 'skip'], [], ['skip', 'skip'], []]))

    
    TEST(uno_who_played_what_v2(['1', 'skip', '3', 'reverse', '4', 'skip', 'reverse', '5']) == (
        [['1', 'reverse', 'reverse'], ['skip', '5'], ['skip'], ['3', '4']]))

    
    TEST(uno_who_played_what_v2(['reverse', 'reverse']) == ([['reverse'], [], [], ['reverse']]))
    TEST(uno_who_played_what_v2(['skip', 'reverse']) == ([['skip'], [], ['reverse'], []]))
    TEST(uno_who_played_what_v2(['skip', 'skip', '1']) == ([['skip', '1'], [], ['skip'], []]))
    print('End uno_who_played_what_v2_TEST')
    print()


def catch_cheater_TEST():
    print('Start catch_cheater_TEST')
    TEST(catch_cheater([['red', '1'], ['blue', '1'], ['green', '2'], ['red', '5'], ['yellow', '5']], ['red', '2'])
         == [2, 3])
    TEST(catch_cheater([['red', '1'], ['blue', '2']], ['green', '1']) == [1])
    TEST(catch_cheater([['green', '1']], ['red', '2']) == [0])
    TEST(catch_cheater([], []) is None)
    print('End catch_cheater_TEST')




deal_3_hands_TEST()

uno_who_played_what_v2_TEST()

catch_cheater_TEST()
