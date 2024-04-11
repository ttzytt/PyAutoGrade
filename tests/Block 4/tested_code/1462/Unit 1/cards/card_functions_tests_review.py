




from card_functions import *


def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')

def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [ [1, 4, 7], [2, 5], [3, 6] ])
    TEST(deal_3_hands([]) == [[], [], []]) 
    TEST(deal_3_hands([1, 2]) == [ [1], [2], [] ]) 
    
    TEST(deal_3_hands(['a', 'b', 'c', 'd', 'e' ]) == [ ['a', 'd'], ['b','e'], ['c'] ])
    print('End deal_3_hands_TEST')
    print()

def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what([]) == [[], [], [], []]) 
    TEST(uno_who_played_what(['1', '2', 'reverse', '2', 'skip', '3', '7']) == 
         [ ['1', 'skip'], ['2', '2', '7'], ['reverse', '3'], [] ]) 
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', 'reverse', '3', '7']) ==
         [ ['1', '7'], ['2', 'reverse', '3'], ['reverse', 'reverse'], [] ])
    TEST(uno_who_played_what(['1', 'skip', 'reverse', 'reverse', 'skip', '3', 'skip']) ==
         [ ['1'], ['skip', '3'], ['reverse', 'skip'], ['reverse', 'skip' ]])
    print('End uno_who_played_what_TEST')
    print()


deal_3_hands_TEST()
uno_who_played_what_TEST()

