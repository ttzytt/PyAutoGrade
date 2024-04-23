


from list_functions import *


def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)


def item_moved_to_end_TEST():
    my_list = [1, 2, 3, 4, 5]
    my_list_old = my_list[:]
    index = 2
    TEST('Moving number to back test', [1, 2, 4, 5, 3], item_moved_to_end(my_list, index))
    if my_list_old == my_list:
        print('my_list stayed the same: pass')

    my_list = []
    my_list_old = my_list[:]        
    index = 0
    TEST('Empty list test', False, item_moved_to_end(my_list, index))
    if my_list_old == my_list:
        print('my_list stayed the same: pass')

    my_list = [1]
    my_list_old = my_list[:]        
    index = 0
    TEST('List with a length of 1', [1], item_moved_to_end(my_list, index))  
    if my_list_old == my_list:
        print('my_list stayed the same: pass')

def move_item_to_end_TEST():

    my_list = [1, 2, 3, 4, 5]
    index = 2
    move_item_to_end(my_list, index)
    if my_list == [1, 2, 4, 5, 3]:
        print('Moving number to back test: pass')
    else:
        print('Moving number to back test: fail')

    my_list = []
    index = 0
    if move_item_to_end(my_list, index) == False:
        print('Empty list test: pass')
    else:
        print('Empty list test: fail')
        
    my_list = [1]
    index = 0
    move_item_to_end(my_list, index)
    if my_list == [1]:
        print('Empty list test: pass')
    else: 
        print('Empty list test: fail')

    
    ('''
    my_list = [1, 2, 3, 4, 5]
    TEST("tests if it returns", None, move_item_to_end(my_list, 1))
    TEST("test if my_list changed", [2, 3, 4, 5, 1], my_list)
    ''')
       
item_moved_to_end_TEST()
move_item_to_end_TEST()
