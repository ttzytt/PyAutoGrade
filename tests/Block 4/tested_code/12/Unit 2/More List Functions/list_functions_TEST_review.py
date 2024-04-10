


from list_functions import *








def TEST(description, expected_result, actual_result):
    print(description,end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print(' Expected Result:', expected_result)
        print(' Actual Result:', actual_result)




def approx_equal(a, b):
    return abs(a - b) < 0.0001






def item_moved_to_end_TEST():
    my_list = [1, 2, 3]
    my_list_old = my_list[:]
    index = 1
    TEST('List with more than 1 element', [1, 3, 2], item_moved_to_end(my_list, index))
    if my_list == my_list_old:
        print("Preserved input test: pass")
    else:
        print("Preserved input test: FAIL")
    my_list = [1]
    index = 0
    TEST('List with 1 element', [1], item_moved_to_end(my_list, index))
    my_list = []
    index = 0
    TEST('Empty list', False, item_moved_to_end(my_list, index))
    my_list = [1, 2, 3]
    index = 2
    TEST('Last element has to be moved', [1, 2, 3], item_moved_to_end(my_list, index))
   

def move_item_to_end_TEST():

    
    my_list = [1, 2, 3]
    move_item_to_end(my_list, 1) 
    if my_list == [1, 3, 2]:
        print("Changed input test: pass")
    else:
        print("Changed inpu est: FAIL")

    
    ()
    
        

item_moved_to_end_TEST()

