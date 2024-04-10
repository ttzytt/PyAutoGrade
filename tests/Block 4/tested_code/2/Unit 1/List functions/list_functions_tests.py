




def count_number_larger_than_TEST():
    print('Start count_number_larger_than_TEST')
    TEST(count_number_larger_than(3, [1, 2, 5, 6]) == 2)
    TEST(count_number_larger_than(0, [10, -3, 4, 5, -1]) == 3)
    TEST(count_number_larger_than(3, []) == 0)
    TEST(count_number_larger_than(3, [3.1]) == 1)
    TEST(count_number_larger_than(3, [4, 3, 3, 1]) == 1)
    print('End count_number_larger_than_TEST')
    print()


def average_TEST():
    print('Start average_TEST')
    TEST(approx_equal(average([1.0, 3.0, 5.0]), 3))
    TEST(approx_equal(average([1, 2, 4]), 2.333333))
    TEST(approx_equal(average([-2]), -2))
    TEST(average([]) == None)
    print('End average_TEST')
    print()


def largest_element_TEST():
    print('Start largest_element_TEST')
    
    TEST(largest_element([1, 3, 5]) == 5)
    
    TEST(largest_element([3, 0, -4]) == 3)
    
    
    TEST(largest_element([-10, -3, -5, -9]) == -3)
    TEST(largest_element([-10]) == -10)
    TEST(largest_element([]) == None)
    print('End largest_element_TEST')
    print()

def all_equal_TEST():
    TEST(all_equal([1, 6, 9]) == False)
    TEST(all_equal([5, 5]) == True)
    TEST(all_equal([-6, 6, 6]) == False)
    TEST(all_equal([-8, -6, -9]) == False)
    TEST(all_equal([1]) == True)
    TEST(all_equal([]) == True)
    print('End all_equal_TEST')
    print()

def alternate_sum_TEST():
    TEST(alternate_sum([1, 2, 3, 4]) == -2)
    TEST(alternate_sum([-0.7, 8, 11.1, -6]) == 8.4)
    TEST(alternate_sum([-2, 4, 9]) == 3)
    TEST(alternate_sum([]) == 0)
    TEST(alternate_sum([5]) == 5)
    print('End alternate_sum_TEST')
    print()

def is_ordered_TEST():
    TEST(is_ordered([1, 3, 3, 7], True) == False)
    TEST(is_ordered([1, 3, 3, 7], False) == True)
    TEST(is_ordered([3, -2], True) == False)
    TEST(is_ordered([], False) == True)
    TEST(is_ordered([1], True) == True)
    print('End is_ordered_TEST')
    print()

def rotate_right_TEST():
    TEST(rotate_right(['you', 'me', 1, 'yay', 'boo']) == ['boo', 'you', 'me', 1, 'yay'])
    TEST(rotate_right(['yes', '1', -1, 1]) == [1, 'yes', '1', -1])
    TEST(rotate_right(['joy']) == ['joy'])
    TEST(rotate_right([]) == [])
    print('End rotate_right_TEST')
    print()

def weird_double_TEST():
    TEST(weird_double([1, 1, 1]) == [2, 2, 2])
    TEST(weird_double([1, 3, -2]) == [2, 3, -2])
    TEST(weird_double([7, 6, 5, 4, 3, 2, 1]) == [14, 6, 5, 4, 3, 4, 2])
    TEST(weird_double([7, 6, 5, 4, 2, 3, 1]) == [14, 6, 5, 4, 2, 3, 1])
    print('End weird_double_TEST')
    print()

def merge_ordered_lists_TEST():
    TEST(merge_ordered_lists([1, 3], [2, 2, 8]) == [1, 2, 2, 3, 8])
    TEST(merge_ordered_lists([-2, 4, 5], [-1]) == [-2, -1, 4, 5])
    TEST(merge_ordered_lists([], []) == [])
    TEST(merge_ordered_lists([2, 4], []) == [2, 4])
    print('End merge_ordered_lists_TEST')
    print()

def deal_3_hands_TEST():
    TEST(deal_3_hands([1, 2, 3, 4, 5, 6, 7]) == [ [1, 4, 7], [2, 5], [3, 6] ])
    TEST(deal_3_hands([]) == [ [], [], []])
    TEST(deal_3_hands([1]) == [ [1], [], []])
    TEST(deal_3_hands([3, -2, 5]) == [ [3], [-2], [5]])
    print('End deal_3_hands_TEST')
    print()



count_number_larger_than_TEST()
average_TEST()
largest_element_TEST()
all_equal_TEST()
alternate_sum_TEST()
is_ordered_TEST()
rotate_right_TEST()
weird_double_TEST()
merge_ordered_lists_TEST()
deal_3_hands_TEST()
