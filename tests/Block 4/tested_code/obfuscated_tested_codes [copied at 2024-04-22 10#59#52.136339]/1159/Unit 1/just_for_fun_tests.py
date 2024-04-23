'''
YOU MAY RUN THIS PROGRAM

'''



from just_for_fun import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def to_the_power_of_TEST():
    print('Start to_the_power_of_TEST')
    TEST(to_the_power_of(3,2) == 9)
    TEST(to_the_power_of(2,3) == 8)
    TEST(to_the_power_of(0,2) == None)
    TEST(to_the_power_of(5,0) == 1)
    TEST(to_the_power_of(2,5) == 32)
    
    print('End to_the_power_of_TEST')
    print()


def power_of_i_TEST():
    print('Start power_of_i_TEST')
    TEST(power_of_i(3) == '-i')
    TEST(power_of_i(4) == 1)
    print('End power_of_i_TEST')
    print()

'''def sqrt_TEST(): # Square root test
    print('Start sqrt_TEST')
    TEST(sqrt(4) == 2)
    TEST(sqrt(6.25) == 2.5)
    print('End sqrt_TEST')
    print()
'''

'''def quadratic_function_TEST():
    print('Start quadratic_function_TEST')
    TEST(quadratic_function(1,-2,1) == 1)
    print('End quadratic_function_TEST')
    print()
'''
def odd_even_count_TEST():
    print('Start odd_even_count_TEST')
    TEST(odd_even_count(1,2,3,4,5) == (3,2))
    TEST(odd_even_count(1,2,3,4) == (2,2))
    print('End odd_even_count_TEST')
    print()

    
def roots_TEST():
    print('Start roots_TEST')
    TEST(roots(1,-2,1) == 1)
    TEST(roots(1,4,4) == -2)
    TEST(roots(1,-2,0) == (2,0))
    TEST(roots(1,-4,0) == (4,0))
    print('End roots_TEST')
    print()


def transfer1_TEST(): 
    print('Start transfer1_TEST')
    TEST(transfer1(2,3,5) == (2, 0.75, 3.875))
    TEST(transfer1(-1,5,-6) == (-1, -2.5, 0.25))
    TEST(transfer1(1,-3,-4) == (1,-1.5,-6.25))
    TEST(transfer1(2,5,-3) == (2,1.25,-6.125))
    TEST(transfer1(3,3,-6) == (3,0.5,-6.75))
    print('End transfer1_TEST')
    print()


def transfer2_TEST(): 
    print('Start transfer2_TEST')
    TEST(transfer2(2, 0.75, 3.875) == (2,3,5))
    TEST(transfer2(-1, -2.5, 0.25) == (-1,5,-6))
    TEST(transfer2(1,-1.5,-6.25) == (1,-3,-4))
    TEST(transfer2(2,1.25,-6.125) == (2,5,-3))
    TEST(transfer2(3,0.5,-6.75) == (3,3,-6))
    print('End transfer2_TEST')
    print()





to_the_power_of_TEST()
power_of_i_TEST()


roots_TEST()
transfer1_TEST()
transfer2_TEST()
