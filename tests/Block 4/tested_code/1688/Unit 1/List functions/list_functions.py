






def approx_equal(a, b):
    return abs(a - b) < 0.0001

def count_number_larger_than(target, numbers):
    count = 0
    
    for i in range(len(numbers)):
        if numbers[i] > target:
            count += 1
    return count



def average(numbers):
    sum = 0
    
    if numbers == []:
        return None
    
    for i in range(len(numbers)):
        sum += numbers[i]

    return sum / len(numbers)
    




def largest_element(numbers):

    if numbers == []:
        return None
    
    max_val_so_far = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_val_so_far:
            max_val_so_far = numbers[i]

    return max_val_so_far





def all_equal(my_list):
    for i in range(len(my_list)):
        if my_list[i] != my_list[0]:
            return False

    return True
        



def alternate_sum(numbers):

    alternate_sum = 0

    for i in range(len(numbers)):
        if i % 2 == 0:
            alternate_sum += numbers[i]

        else:
            alternate_sum -= numbers[i]

    return alternate_sum
        





def is_ordered(numbers, is_strict):
    if is_strict == True:
        for i in range(len(numbers)-1):
            if numbers[i] >= numbers[i+1]:
                return False

    else:
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                return False

    return True
    





def rotate_right(my_list):
    store_val = my_list[len(my_list)-1]
    for i in range(1, len(my_list)):
        my_list[len(my_list)-i] = my_list[len(my_list)-i-1]
    my_list[0] = store_val
    return my_list








def weird_double(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] % 3 == 0:
            i += 4
            continue

        numbers[i] *= 2
        i += 1
    return numbers

        



def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    merged_ordered = []
    i = 0
    j = 0
    while i < len(ordered_numbers_1) and j < len(ordered_numbers_2):
        if ordered_numbers_1[i] < ordered_numbers_2[j]:
            merged_ordered.append(ordered_numbers_1[i])
            i += 1
        else:
            merged_ordered.append(ordered_numbers_2[j])
            j += 1

    while i < len(ordered_numbers_1):
        merged_ordered.append(ordered_numbers_1[i])
        i += 1
    while j < len(ordered_numbers_2):
        merged_ordered.append(ordered_numbers_2[j])
        j += 1
        
    return merged_ordered
                           













