


from card_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')



def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [ [1, 4, 7], [2, 5], [3, 6] ])
    
    TEST(deal_3_hands([2]) == [[2], [], []])
    TEST(deal_3_hands([]) == [[], [], []]) 
    
    
    TEST(deal_3_hands(['a', 'b', 'c']) == [ ['a'], ['b'], ['c'] ]) 
    TEST(deal_3_hands([285, 'c']) == [ [285], ['c'], [] ]) 
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    
    TEST(uno_who_played_what([1, 2, 3, 'skip', 5]) == [[1], [2, 5], [3], ['skip']])
    TEST(uno_who_played_what([1, 2, 3, 'reverse', 4, 5]) == [[1], [2, 5], [3, 4], ['reverse']])
    
    
    TEST(uno_who_played_what([1, 2, 3, 'reverse', 'skip', 6]) == [[1, 6], [2], [3, 'skip'], ['reverse']])
    TEST(uno_who_played_what([1, 2, 3, 'skip', 'reverse', 6]) == [[1, 6], [2, 'reverse'], [3], ['skip']])

    TEST(uno_who_played_what(['skip', 'reverse', 'reverse', 'skip', 'reverse', 6])
         == [['skip', 'reverse'], ['reverse'], ['reverse', 'skip'], [6]]) 
    TEST(uno_who_played_what([]) == [[], [], [], []]) 
    print('End uno_who_played_what_TEST')
    print()




deal_3_hands_TEST()
uno_who_played_what_TEST()
