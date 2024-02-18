








def count_number_larger_than(target, numbers):
    n = int(target)
    x = 0
    for i in numbers:
        if i > n:
            x += 1
    return x




def average(numbers):
    if len(numbers) == 0:
        return False

    count_number_larger_than = 0
    for i in range(len(numbers)):
        count_number_larger_than = count_number_larger_than + numbers[i]
    return count_number_larger_than/len(numbers)



def largest_element(numbers):
    if len(numbers) == 0:
        return False
    n = numbers[0]
    for i in numbers:
        if i > n:
            n = i
    return n
    



def all_equal(my_list):
    if len(my_list) == 0:
        return False
    for i in range(len(my_list)):
        if my_list[i] == '1':
            return False
        first = my_list[0]
        if first != my_list[i]:
            return False
    return True




def is_ordered(numbers, is_strict):
    if len(numbers) == 0 or len(numbers) == 1:
        return True
    for i in range(len(numbers)):
        first = 0
        second = 1
        if numbers[first] <= numbers[second]:
            first += 1
            second += 1
        else:
            return 0
    return True




def alternate_sum(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    odd = 0
    even = 0
    i = 0
    while i < len(nums):
        odd += nums[i]
        i += 2
    i = 1
    while i < len(nums):
        even += nums[i]
        i += 2
    sum = odd - even
    return sum





def rotate_right(my_list):
    output_list = []
    if len(my_list) == 0:
        return []
    for i in range(len(my_list)-1, len(my_list)):
        output_list.append(my_list[i])
    for i in range(0, len(my_list)-1):
        output_list.append(my_list[i])
    return output_list





def weird_double(numbers):
    skip = 0
    output = []
    for i in range(len(numbers)):
        if skip > 0:
            output.append(numbers[i])
            skip = skip - 1
        elif numbers[i] % 3 == 0:
            skip = 3
            output.append(numbers[i])
        else:
            output.append(numbers[i] * 2)
    return output






def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    merge_ordered_lists = ordered_numbers_1 + ordered_numbers_2
    merge_ordered_lists.sort()
    return(merge_ordered_lists)
