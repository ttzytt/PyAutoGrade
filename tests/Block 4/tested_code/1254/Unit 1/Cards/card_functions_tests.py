

from card_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def deal_3_hands_TEST():
    print('Start deal_3_hands_TEST')
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) ==  [ [1, 4, 7], [2, 5], [3, 6] ])
    TEST(deal_3_hands([4, 7, 8, 10, 300, -3, -800]) ==  [ [4, 10, -800], [7, 300], [8, -3] ])
    TEST(deal_3_hands([]) ==  [ [], [], [] ])
    TEST(deal_3_hands([3]) ==  [ [3], [], [] ])
    
    


         
def uno_who_played_what_TEST():
    print('Start uno_who_played_what_TEST')

    
    print("No special cards")
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', '7', '8'])
         == [['1', '5'], ['2', '6'], ['3', '7'], ['4', '8']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5'])
         == [['1', '5'], ['2'], ['3'], ['4']])

    
    print("Single skip")
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7' ])
         == [['1', '5'], ['2', 'skip'], ['3'], ['4', '7']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', 'skip'])
         == [['1', '5'], ['2', '6'], ['3', 'skip'], ['4']])
    TEST(uno_who_played_what(['1', '2', 'skip', '3', '4'])
         == [['1', '3'], ['2', '4'], ['skip'], []]) 
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip'])
         == [['1', '5'], ['2', 'skip'], ['3'], ['4']])
    TEST(uno_who_played_what(['1', '2', '3', 'skip', '4'])
         == [['1'], ['2', '4'], ['3'], ['skip']])
    TEST(uno_who_played_what(['skip', '2', '3', '4'])
         == [['skip', '4'], [], ['2'], ['3']])


    
    print("Multiple skip")
    TEST(uno_who_played_what(['skip', 'skip', '7' ])
         == [['skip', '7'], [], ['skip'], []])
    TEST(uno_who_played_what(['1', 'skip', 'skip', '4'])
         == [['1', ], ['skip', '4'], [], ['skip']])
    TEST(uno_who_played_what(['1', '2', 'skip', 'skip', 'skip', '3', '7'])
         == [ ['1', 'skip', '3'], ['2', '7'], ['skip', 'skip'], [] ])
    TEST(uno_who_played_what(['skip', 3, 'skip', 7, 'skip', 10])
         == [['skip', 10], [7], [3, 'skip'], ['skip']])
    TEST(uno_who_played_what(['skip', 'skip', 'skip', 'skip'])
         == [['skip', 'skip'], [], ['skip', 'skip'], []])

    
    print("Single reverse")
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '7' ])
         == [['1', '5', '7'], ['2', 'reverse'], ['3'], ['4']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', 'reverse'])
         == [['1', '5'], ['2', '6'], ['3', 'reverse'], ['4']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '6', '7'])
         == [['1', '5', '6'], ['2', 'reverse'], ['3'], ['4', '7']])
    TEST(uno_who_played_what(['1', 'reverse', '3', '4'])
         == [['1', '3'], ['reverse'], [], ['4']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '9', '10'])
         == [['1', '5', '9'], ['2', 'reverse'], ['3'], ['4', '10']])

    
    print("Multiple reverse")
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', 'reverse', '3', '7'])
         == [ ['1', '7'], ['2', 'reverse', '3'], ['reverse', 'reverse'], [] ])
    TEST(uno_who_played_what(['reverse', 'reverse', 'reverse', 'reverse'])
         == [['reverse', 'reverse'], [], [], ['reverse', 'reverse']])
    TEST(uno_who_played_what(['1', 'reverse', 'reverse', '4'])
         == [['1', 'reverse'], ['reverse', '4'], [], []])
    TEST(uno_who_played_what(['1', '2', 'reverse', '3', '4', 'reverse', '5'])
         == [['1', '4', '5'], ['2', '3'], ['reverse'], ['reverse']])
    TEST(uno_who_played_what(['6', 'reverse', 'reverse'])
         == [['6', 'reverse'], ['reverse'], [], []])                                                                 
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', 'reverse', '8'])
        == [['1', '5', 'reverse'], ['2', 'reverse', '8'], ['3'], ['4']])
    TEST(uno_who_played_what(['reverse', 'reverse', 'reverse', 'reverse', 'reverse'])
         == [['reverse', 'reverse', 'reverse'], [], [], ['reverse', 'reverse']])
    TEST(uno_who_played_what(['reverse', 1, 2, 3, 'reverse', 4, 5, 6])
         == [['reverse', 'reverse'], [3, 4], [2, 5], [1, 6]])

    
    print("Small card piles")
    TEST(uno_who_played_what([])
         == [[], [], [], []])
    TEST(uno_who_played_what(['1', '5'])
         == [['1'], ['5'], [], []])
    TEST(uno_who_played_what(['reverse', 'reverse'])
         == [['reverse'], [], [], ['reverse']])
    TEST(uno_who_played_what(['skip', 'reverse'])
         == [['skip'], [], ['reverse'], []])
    TEST(uno_who_played_what(['skip', 'skip', '1'])
         == [['skip', '1'], [], ['skip'], []])

    
    print("skip, then reverse")
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', 'reverse', '9', '10'])
         == [['1', '5'], ['2', 'skip', '10'], ['3', '9'], ['4', 'reverse']])
    TEST(uno_who_played_what(['1', '2', '3', 'skip', '4', 'reverse', '5', '6'])
          == [['1', '6'], ['2', '4', '5'], ['3', 'reverse'], ['skip']])
    TEST(uno_who_played_what([1, 2, 3, 'skip', 'reverse', 6])
         == [[1, 6], [2, 'reverse'], [3], ['skip']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', 'reverse', '8'])
         == [['1', '5'], ['2', 'skip'], ['3', '8'], ['4', 'reverse']])

    
    print("reverse, then skip")
    TEST(uno_who_played_what(['1', '2', 'reverse', '2', 'skip', '3', '7'])
         == [ ['1', 'skip'], ['2', '2', '7'], ['reverse', '3'], [] ])
    TEST(uno_who_played_what(['1', '2', '3', 'reverse', '4', 'skip'])
         == [['1'], ['2', 'skip'], ['3', '4'], ['reverse']])
    TEST(uno_who_played_what(['1', '2', '3', 'reverse', '4', '5', 'skip', '6'])
          == [['1', 'skip'], ['2', '5'], ['3', '4', '6'], ['reverse']])
    TEST(uno_who_played_what(['reverse', '1', 'skip', '2', '3', '10'])
         == [['reverse', '2'], [], ['skip', '10'], ['1', '3']])
    TEST(uno_who_played_what([1, 2, 3, 'reverse', 'skip', 6])
         == [[1, 6], [2], [3, 'skip'], ['reverse']])

    
    print("complex combinations of skip and reverse")
    TEST(uno_who_played_what(['1', '2', 'reverse', 'reverse', '5', 'skip', '7'])
         == [['1'], ['2', 'reverse', '7'], ['reverse', '5'], ['skip']])
    TEST(uno_who_played_what(['1', 'skip', 'reverse', 'reverse', 'skip', '3', 'skip'])
         == [ ['1'], ['skip', '3'], ['reverse', 'skip'], ['reverse', 'skip' ]])
    TEST(uno_who_played_what(['13', 'skip', '4', 'reverse', '5', '6', 'skip', '8'])
         == [['13', 'reverse'], ['skip', 'skip'], ['6'], ['4', '5', '8']])
    TEST(uno_who_played_what(['reverse', '1', 'reverse', 'skip', '2', '3'])
        == [['reverse'], ['2'], ['reverse', '3'], ['1', 'skip']])
    TEST(uno_who_played_what(['skip', 'reverse', 'reverse', 'skip', 'reverse', 6])
         == [['skip', 'reverse'], ['reverse'], ['reverse', 'skip'], [6]])
    TEST(uno_who_played_what(['1', 'skip', '3', 'reverse', '4', 'skip', 'reverse', '5'])
         == [['1', 'reverse', 'reverse'], ['skip', '5'], ['skip'], ['3', '4']])
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', '6', 'reverse', 'skip', 'reverse', '7', '8', '9'])
         == [['1', '5', '7'], ['2', '6', 'skip', '8'], ['3', 'reverse', '9'], ['4', 'reverse']])

    print('End uno_who_played_what_TEST')
    print()

deal_3_hands_TEST()
uno_who_played_what_TEST()




