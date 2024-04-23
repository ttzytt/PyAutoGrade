

from card_functions import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def deal_3_hands_TEST():
    print("Start_deal_3_hands_TEST")
    TEST(deal_3_hands([1, 3, 2]) == ([[1], [3], [2]]))
    TEST(deal_3_hands([1, 6, 7, 10, 3, 2]) == ([[1, 10], [6, 3], [7, 2]]))
    TEST(deal_3_hands([1, 3, 2, 7]) == ([[1, 7], [3], [2]]))
    TEST(deal_3_hands([1, 3, 2, 7, 9]) == ([[1, 7], [3, 9], [2]]))
    TEST(deal_3_hands([1]) == ([[1], [], []]))
    TEST(deal_3_hands(["Hello", "Python", "World"]) == ([["Hello"], ["Python"], ["World"]]))
    print('End deal_3_hands_TEST')
    print()

def uno_who_played_what_TEST():
    print("Start_uno_who_played_what_TEST")
    TEST(uno_who_played_what(['1', '2', '3', '4', '5']) == ([['1', '5'], ['2'], ['3'], ['4']]))
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'skip', 'reverse', '9', '10']) == ([['1', '5'], ['2', 'skip', '10'], ['3', '9'], ['4', 'reverse']]))
    TEST(uno_who_played_what(['1', '2', '3', '4', '5', 'reverse', '9', '10']) == ([['1', '5', '9'], ['2', 'reverse'], ['3'], ['4', '10']]))
    TEST(uno_who_played_what(['1', '2', '3', 'skip', '4']) == ([['1'], ['2', '4'], ['3'], ['skip']]))
    
    print('End_uno_who_played_what_TEST')
    print()



deal_3_hands_TEST()
uno_who_played_what_TEST()


