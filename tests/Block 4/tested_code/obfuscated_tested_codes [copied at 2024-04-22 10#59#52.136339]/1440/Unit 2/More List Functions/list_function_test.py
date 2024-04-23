

from list_function import * 


def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)

print('Start item_moved_to_end_TEST') 

TEST('number',[1,2,4,5,6,3],item_moved_to_end([1,2,3,4,5,6],2))
TEST('string',['ya','ha','hehe','ww','ye','wu'],item_moved_to_end(['ya','ha','wu','hehe','ww','ye'],2))
 
print('Start moved_to_end_TEST')

TEST('number',[1,2,4,5,6,3],item_moved_to_end([1,2,3,4,5,6],2))
TEST('string',['ya','ha','hehe','ww','ye','wu'],item_moved_to_end(['ya','ha','wu','hehe','ww','ye'],2))
