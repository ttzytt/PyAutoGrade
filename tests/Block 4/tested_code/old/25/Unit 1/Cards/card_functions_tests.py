


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
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6]) == [[1, 4], [2, 5], [3, 6]])
    TEST(deal_3_hands([1, 2, 3, 4, 5]) == [[1, 4], [2, 5], [3]])
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 12, 15, 35, 43]) == [[1, 4, 12, 43], [2, 5, 15], [3, 6, 35]])
    print()

def uno_played_what_TEST():
    print('Start uno_played_what_TEST')
    TEST(uno_played_what([1, 2, 3, 4, 5, 6, 7, 'skip']) == [[1, 5], [2, 6], [3, 7], [4, 'skip']])
    TEST(uno_played_what([1, 2, 3, 4, 5, 'skip', 6, 7, 2, 3, 5]) == [[1, 5, 7], [2, 'skip', 2], [3, 3], [4, 6, 5]])
    TEST(uno_played_what([1, 2, 3, 4, 5, 'reverse', 7, 'skip']) == [[1, 5, 7], [2, 'reverse'], [3], [4, 'skip']])
    TEST(uno_played_what([1, 2, 3, 4, 'reverse', 'reverse', 7, 'skip']) == [[1, 'reverse', 7], [2, 'skip'], [3], [4, 'reverse']])
    TEST(uno_played_what(['reverse', 1, 3, 5, 6, 'skip', 3, 4, 4, 'reverse', 8, 1]) == [['reverse', 6, 4, 1], [5, 3], [3, 'reverse'], [1, 'skip', 4, 8]])

deal_3_hands_TEST()
uno_played_what_TEST()
