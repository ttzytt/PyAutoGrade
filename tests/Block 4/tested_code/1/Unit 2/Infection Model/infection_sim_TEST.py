



def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)

def infection_probability_percent_TEST():
    print('start infection_probability_percent_TEST')
    board = [ ['0', '0', '0'],
              ['0', '1', '0'],
              ['0', '1', '0'] ]
    TEST("for the middle one", infection_probability_percent(
def to_get_them_infected_TEST():
    print('start to_get_them_infected_TEST')
    
