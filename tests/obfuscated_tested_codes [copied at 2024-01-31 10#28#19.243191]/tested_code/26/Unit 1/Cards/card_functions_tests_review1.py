

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
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    
    TEST(deal_3_hands(['J', 'A', 9, 3, 'Q', 4, 2, 'Joker']) == \
                      [['J', 3, 2], ['A', 'Q', 'Joker'], [9, 4]])
    
    TEST(deal_3_hands([]) == [[], [], []])
    TEST(deal_3_hands([2]) == [[2], [], []])
    TEST(deal_3_hands([2, 4]) == [[2], [4], []])
    TEST(deal_3_hands([2, 4, 'K']) == [[2], [4], ['K']])
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7']) ==
         [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '7']) ==
         [['1', '5', '7'], ['2', 'reverse'], ['3'], ['4']])
    
    TEST(uno_who_played_what(['1', '2', '3', 'skip', 'skip', '6', '7']) ==
         [['1', '7'], ['2', 'skip'], ['3'], ['skip', '6']])
    
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', '5',
                              'skip', '7']) == [['1'],
                                                ['2','reverse', '7'],
                                                ['reverse', '5'], ['skip']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', '7']) ==
         [['1', '5'], ['2', '6'], ['3', '7'], ['4']])
    
    TEST(uno_who_played_what([]) == [[], [], [], []])
    TEST(uno_who_played_what(['1']) == [['1'], [], [], []])
    TEST(uno_who_played_what(['1', '2']) == [['1'], ['2'], [], []])
    TEST(uno_who_played_what(['1', '2', 'skip']) == [['1'], ['2'], ['skip'], []])
    TEST(uno_who_played_what(['1', '2', 'skip', '4']) ==
         [['1', '4'], ['2'], ['skip'], []])
    print('End uno_who_played_what_TEST')
    print()
    


deal_3_hands_TEST()
uno_who_played_what_TEST()
