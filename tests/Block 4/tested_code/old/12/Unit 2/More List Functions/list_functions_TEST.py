


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
    print('Start item_moved_to_end_TEST')
    
    my_list = ['Rachel', 'Valentine', 'Dr. Deionno', 'Amy', 'Echo']
    TEST('create new list', ['Rachel', 'Valentine', 'Amy', 'Echo', 'Dr. Deionno'], item_moved_to_end(my_list, 2))
    TEST('keep original list', ['Rachel', 'Valentine', 'Dr. Deionno', 'Amy', 'Echo'], my_list)

    my_list_2 = [1, 2, 3, 4, 5]
    TEST('create new list', [1, 3, 4, 5, 2], item_moved_to_end(my_list_2, 1))
    TEST('keep original list', [1, 2, 3, 4, 5], my_list_2)

def move_item_to_end_TEST():
    print('Start move_item_to_end_TEST')

    my_list = ['Rachel', 'Valentine', 'Dr. Deionno', 'Amy', 'Echo']
    TEST('modify on original list', None, move_item_to_end(my_list, 1))
    TEST('current list', ['Rachel', 'Dr. Deionno', 'Amy', 'Echo', 'Valentine'], my_list)

    my_list_2 = [1, 2, 3, 4, 5]
    TEST('modify on original list', None, move_item_to_end(my_list_2, 2))
    TEST('current list', [1, 2, 4, 5, 3], my_list_2)



item_moved_to_end_TEST()
move_item_to_end_TEST()
