




def count_numbers_larger_than(target, numbers):
    count = 0
    for number in numbers:
        if number > target:
            count += 1
    return count



def average(numbers):
    if not numbers:
        return None
    total = 0
    
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)



def largest_element(numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num



def all_equal(my_list):
    if len(my_list) < 1:
        return None
    elif len(my_list) < 2:
        return True 
    for i in range(len(my_List) - 1):
        if my_list[i] is mylist[i+1]:
            equal = 'yes'
        else:
            equal = 'no'
    if equal == 'yes':
        return True
    else:
        return False



def alternate_sum(numbers):
    result = 0
    for i in range(len(numbers)):
        if i % 2 ==0:
            result += numbers[i]
        else:
            result -= numbers[i]
    return result


def is_ordered(numbers, is_strict):
    if not numbers:
        return True

    for i in range(1, len(numbers)):
        if is_strict:
            if numbers[i] <= numbers[i - 1]:
                return False
        else:
            if numbers[i] < numbers[i - 1]:
                return False

    return True




def rotate_right(my_list):
    if len(my_list) > 1:
        last_element = my_list[-1]
        for i in range(len(my_list) - 1, 0, -1):
            my_list[i] = my_list[i - 1]
        my_list[0] = last_element

rotate_right(my_list)

for i in range(len(my_list)):
    print(my_list[i])



def weird_double(numbers):
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 3 == 0:
            result.append(numbers[i])
            i += 4
        else:
            result.append(numbers[i] * 2)
            i += 1
    return result


new_numbers = weird_double(numbers)


for i in range(len(new_numbers)):
    print(new_numbers[i])


"""
# 
def count_numbers_larger_than(target, numbers):
    count = 0
    for number in numbers:
        if number > target:
            count += 1
    return count



def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

def find_largest_element(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num


def are_all_elements_equal(my_list):
    if len(my_list) < 1:
        return None
    elif len(my_list) < 2:
        return True

    for i in range(len(my_list) - 1):
        if my_list[i] != my_list[i + 1]:
            return False

    return True


def is_ordered(numbers, is_strict):
    if not numbers:
        return True

    for i in range(1, len(numbers)):
        if is_strict:
            if numbers[i] <= numbers[i - 1]:
                return False
        else:
            if numbers[i] < numbers[i - 1]:
                return False

    return True

def rotate_right(my_list):
    if not my_list:
        return my_list
    
    rotated_list = [my_list[-1]] + my_list[:-1]
    return rotated_list

def weird_double(numbers):
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 3 == 0:
            result.append(numbers[i])
            i += 4
        else:
            result.append(numbers[i] * 2)
            i += 1
    return result

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    merged_list = []
    i = 0
    j = 0

    while i < len(ordered_numbers_1) and j < len(ordered_numbers_2):
        element_1 = ordered_numbers_1[i]
        element_2 = ordered_numbers_2[j]

        if element_1 <= element_2:
            merged_list = merged_list + [element_1]
            i += 1
        else:
            merged_list = merged_list + [element_2]
            j += 1

    # Add any remaining elements from the input lists
    while i < len(ordered_numbers_1):
        merged_list = merged_list + [ordered_numbers_1[i]]
        i += 1

    while j < len(ordered_numbers_2):
        merged_list = merged_list + [ordered_numbers_2[j]]
        j += 1

    return merged_list

"""

