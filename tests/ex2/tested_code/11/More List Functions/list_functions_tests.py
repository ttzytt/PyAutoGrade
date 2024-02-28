


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
    
    
    L = [1,2,3,4,5]
    TEST('moving first element to end',[2,3,4,5,1], item_moved_to_end(L,0))
    TEST('does list stay the same', [1,2,3,4,5], L)

    
    L = [1,2,3,4,5]
    TEST('moving middle element to end',[1,2,4,5,3], item_moved_to_end(L,2))
    TEST('does list stay the same', [1,2,3,4,5], L)

    
    L = [1,2,3,4,5]
    TEST('moving last element to end',[1,2,3,4,5], item_moved_to_end(L,4))
    TEST('does list stay the same', [1,2,3,4,5], L)

    
    L = ['a','b','c','d','e','f','g']
    TEST('moving middle element to end with strings',['a','b','d','e','f','g','c'], item_moved_to_end(L,2))
    TEST('does list stay the same', ['a','b','c','d','e','f','g'], L)

    
    
    L = [1]
    TEST('one-element lists',[1], item_moved_to_end(L,0))
    TEST('does list stay the same', [1], L)

    
    L = [1,'a',True]
    TEST('mixed arrays',['a',True, 1], item_moved_to_end(L,0))
    TEST('does list stay the same', [1,'a',True], L)
    
    
def move_item_to_end_TEST():
    
    
    L = [1,2,3,4,5]
    TEST('function returns None:', None, move_item_to_end(L,0))
    TEST('list changed correctly:', [2,3,4,5,1], L)

    
    L = [1,2,3,4,5]
    TEST('function returns None:', None, move_item_to_end(L,2))
    TEST('list changed correctly:', [1,2,4,5,3], L)

    
    L = [1,2,3,4,5]
    TEST('function returns None:', None, move_item_to_end(L,4))
    TEST('list changed correctly:', [1,2,3,4,5], L)

    
    L = ['a','b','c','d','e','f','g']
    TEST('function returns None:', None, move_item_to_end(L,2))
    TEST('list changed correctly:', ['a','b','d','e','f','g','c'], L)

    
    
    L = [1]
    TEST('function returns None:', None, move_item_to_end(L,0))
    TEST('list changed correctly:', [1], L)

    
    L = [1,'a',True]
    TEST('function returns None:', None, move_item_to_end(L,0))
    TEST('list changed correctly:', ['a',True, 1], L)

item_moved_to_end_TEST()
move_item_to_end_TEST()
        
    
