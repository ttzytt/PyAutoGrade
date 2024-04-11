

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
    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7'], 4, 2) ==
         [['4', '7'], ['1', '5'], ['2', 'skip'], ['3']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '7'], 4, 3) ==
         [['3'], ['4'], ['1', '5', '7'], ['2', 'reverse']])
    
    TEST(uno_who_played_what(['1', '2', '3', 'skip', 'skip', '6', '7'], 5, 2) ==
         [[], ['1', 'skip'], ['2'], ['3', '6'], ['skip', '7']])
    
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', '5',
                              'skip', '7'], 3, 3) == [['2', 'reverse'],
                                                      ['reverse', '5', '7'],
                                                      ['1','skip']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', '7'], 6, 5) ==
         [['3'], ['4'], ['5'], ['6'], ['1', '7'], ['2']])
    
    TEST(uno_who_played_what(['reverse', '1', '2', '3', '4'], 4, 2) ==
         [['1'], ['reverse', '4'], ['3'], ['2']])
    
    TEST(uno_who_played_what([], 3, 1) == [[], [], []])
    TEST(uno_who_played_what(['1'], 4, 4) == [[], [], [], ['1']])
    TEST(uno_who_played_what(['1', '2'], 2, 2) == [['2'], ['1']])
    TEST(uno_who_played_what(['1', '2', 'skip'], 5, 3) ==
         [[], [], ['1'], ['2'], ['skip']])
    TEST(uno_who_played_what(['1', '2', 'skip', '4'], 4, 2) ==
         [[], ['1', '4'], ['2'], ['skip']])



    print('End uno_who_played_what_TEST')
    print()


def catch_cheater_TEST():
    print('Start catch_cheater_TEST')
    

    
    TEST(catch_cheater([['red', '1'], ['red', 'skip'], ['red', '7']],
                             ['red', '4'], 4, 2) == None)
    
    TEST(catch_cheater([['blue', '1'], ['green', '1'], ['yellow', '1']],
                             ['red', '1'], 3, 1) == None)
    
    TEST(catch_cheater([['red', '1'], ['red', 'skip'], ['blue', '7']],
                             ['red', '4'], 5, 2) == 5)
    
    TEST(catch_cheater([['red', '1'], ['red', 'reverse'], ['red', '7'],
                        ['blue', '7'], ['blue', 'skip'], ['red', '2']],
                             ['red', '4'], 3, 2) == 1)
    
    TEST(catch_cheater([['red', '1'], ['red', 'reverse'], ['red', '7'],
                        ['blue', '7'], ['blue', 'skip'], ['red', '2']],
                             ['blue', '4'], 8, 4) == 4)
    
    TEST(catch_cheater([['red', 'skip'], ['blue','76']],
                             ['blue', 'skip'], 3, 1) == 1)
    
    TEST(catch_cheater([['blue', 'skip'], ['blue','7'], ['red', '7'],
                         ['red', 'skip'], ['yellow', '3']],
                             ['blue', 'reverse'], 3, 2) == 2)
    
    TEST(catch_cheater([['blue', 'skip']],
                             ['blue', 'reverse'], 10, 8) == None)
    TEST(catch_cheater([['green', '3']],
                             ['blue', 'skip'], 10, 8) == 9)
    TEST(catch_cheater([], ['blue', 'reverse'], 4, 2) == None)

    print('End catch_cheater_TEST')
    print()
    


deal_3_hands_TEST()
uno_who_played_what_TEST()
catch_cheater_TEST()
