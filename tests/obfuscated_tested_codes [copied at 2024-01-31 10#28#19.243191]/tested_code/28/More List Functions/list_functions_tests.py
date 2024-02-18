


from list_functions import*









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
    index = 2
    TEST('accept legal operation',[1, 2, 4, 5, 3], item_moved_to_end(my_list, index))
    expected_list = [1, 2, 4, 5, 3]
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))

    
    my_list = [1, 2]
    index = 0
    TEST('accept legal operation',[2, 1], item_moved_to_end(my_list, index))
    expected_list = [2, 1]
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))

    
    my_list = ['cat','dog','rat','snake','bird']
    index = 3
    TEST('accept legal operation',['cat','dog', 'rat','bird','snake'], item_moved_to_end(my_list, index))
    expected_list = ['cat','dog', 'rat','bird','snake']
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))

def move_item_to_end_TEST():
    
    
    my_list = [1, 2, 3, 4, 5]
    index = 2
    TEST('accept legal operation',None, item_moved_to_end(my_list, index))
    expected_list = [1, 2, 4, 5, 3]
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))

    
    my_list = [1, 2]
    index = 0
    TEST('accept legal operation',None, item_moved_to_end(my_list, index))
    expected_list = [2, 1]
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))

    
    my_list = ['cat','dog','rat','snake','bird']
    index = 3
    TEST('accept legal operation',None, item_moved_to_end(my_list, index))
    expected_list = ['cat','dog', 'rat','bird','snake']
    TEST('make legal operation', expected_list, item_moved_to_end(my_list, index))



item_moved_to_end_TEST()
move_item_to_end_TEST()
