

from card_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')



def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([1,2,3,4,5,6,7]) == [[1,4,7],[2,5],[3,6]])
    print('End deal_3_hands_TEST')
    print()

def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')
    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7' ],4,0) == \
         [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '7' ],4,0) == \
         [['1', '5','7'], ['2', 'reverse'], ['3'], ['4']])
    
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', '5', 'skip', '7'],4,0) == \
         [['1'], ['2','reverse','7'], ['reverse','5'], ['skip']])
    
    print('End uno_who_played_what_TEST')
    print()

def catch_cheater_TEST():
    print('Start catch_cheater_TEST')
    
    TEST(catch_cheater([['red', '1'],
                        ['red', '2'],
                        ['red', '3']], ['red','9'], 3, 0) == None)
    
    TEST(catch_cheater([['blue', '1'],
                        ['red', '1'],
                        ['green','1']], ['yellow','1'], 3, 0) == None)
    
    TEST(catch_cheater([['red', '1'],
                        ['blue', '2']], ['red','9'], 2, 1) == 0)
    
    TEST(catch_cheater([['blue', 'skip'],
                        ['red', '1'],
                        ['green','1']], ['blue','1'], 3, 0) == 2)
    
    TEST(catch_cheater([['blue', 'reverse'],
                        ['red', '1'],
                        ['green','1']], ['blue','1'], 4, 0) == 3)
    
    TEST(catch_cheater([], ['blue','1'], 4, 0) == None)
    print('End catch_cheater_TEST')
    print()



deal_3_hands_TEST()
uno_who_played_what_TEST()
catch_cheater_TEST()
