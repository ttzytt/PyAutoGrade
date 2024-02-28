

from silly_function import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def approx_equal(a, b):
    return abs(a - b) < 0.0001




def silly_function_test():
    TEST(silly_function(123) == True)
    TEST(silly_function('poop') == 'poop')
    TEST(silly_function('pneumonoultramicroscopicsilicovolcanoconiosis') == 'sisoinoconaclovociliscipocsorcimartluonomuenp')
    TEST(silly_function(321) == '')
    TEST(silly_function(True) == 'banana')




silly_function_test()
