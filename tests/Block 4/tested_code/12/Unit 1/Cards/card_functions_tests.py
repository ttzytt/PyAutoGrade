

from card_functions import *






def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')



def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [[1, 4, 7], [2, 5], [3, 6]])
    TEST(deal_3_hands(['A', 'B', 'C', 'D', 'E', 'F']) == [['A', 'D'], ['B', 'E'], ['C', 'F']])
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 4, 7], [2, 5, 8], [3, 6]])    
    print('End deal_3_hands_TEST')

def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6']) == [['1', '5'], ['2', '6'], ['3'], ['4']])
    TEST(uno_who_played_what(['1', 'skip', '3', '4', '5', '6']) == [['1', '4'], ['skip', '5'], ['6'], ['3']])
    TEST(uno_who_played_what(['1', 'reverse', '3', '4', '5']) == [['1', '3'], ['reverse'], ['5'], ['4']])
    TEST(uno_who_played_what(['1', 'skip', '3', 'reverse', '5']) == [['1', 'reverse'], ['skip'], [], ['3', '5']])
    print('End uno_who_played_what_TEST')
    print()



deal_3_hands_TEST()
uno_who_played_what_TEST()
