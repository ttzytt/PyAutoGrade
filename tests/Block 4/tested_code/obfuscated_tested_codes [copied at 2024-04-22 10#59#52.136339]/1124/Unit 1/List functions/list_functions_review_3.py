





def count_number_larger_than(target, numbers):
    number_larger = 0
    for i in range(0, len(numbers)):
        if numbers[i] > target:
            number_larger += 1
    return number_larger




def average(numbers):
    
    if len(numbers) == 0:
        return None
    elif len(numbers) > 0:
        total_sum = 0
        for i in range(0,len(numbers)):
            total_sum += numbers[i]
    return total_sum/len(numbers)


def largest_element(numbers):
    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    for i in range(0, len(numbers)):
        if largest < numbers[i]:
            largest = numbers[i]
    return largest




def all_equal(my_list):
    if len(my_list) == 0:
        return True
    else:
        for i in range(0, len(my_list)):
            if my_list[i] != my_list[0]:
                return False
    return True
    



def alternate_sum(numbers):
    total_sum = 0
    if len(numbers) == 0:
        return None
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            total_sum += numbers[i]
        elif i % 2 == 1:
            total_sum -= numbers[i]
    return total_sum




def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return True
    
    
    is_ordered_so_far = True
    if is_strict == True:
        for i in range(0, len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                is_ordered_so_far = True
            elif numbers[i] >= numbers[i+1]:
                return False
    if is_strict == False: 
        for i in range(0, len(numbers)-1):
            if numbers[i] <= numbers[i+1]:
                is_ordered_so_far = True
            elif numbers[i] > numbers[i+1]:
                return False
    return is_ordered_so_far



def rotate_right(my_list):
    if len(my_list) == 0:
        return []
    
    
    nums = []
    last_term = my_list[len(my_list) - 1]
    nums.append(last_term)
    for i in range(0, len(my_list) - 1):
        nums.append(my_list[i])
    return nums



def weird_double(numbers):
    if len(numbers) == 0:
        return None
    
    current_term = 0
    while current_term < len(numbers):
        
        if numbers[current_term] % 3 == 0:
            current_term += 4
        elif numbers[current_term] % 3 != 0:
            numbers[current_term] = numbers[current_term] * 2
            current_term += 1
    return numbers


def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    current_term_1 = 0
    current_term_2 = 0

    
    merged_list = []

    
    
    while current_term_1 < len(ordered_numbers_1) and current_term_2 < len(ordered_numbers_2):
        if ordered_numbers_1[current_term_1] <= ordered_numbers_2[current_term_2]:
            merged_list.append(ordered_numbers_1[current_term_1])
            current_term_1 += 1
        elif ordered_numbers_2[current_term_2] < ordered_numbers_1[current_term_1]:
            merged_list.append(ordered_numbers_2[current_term_2])
            current_term_2 += 1
            
    
    
    if current_term_1 == len(ordered_numbers_1):
        for i in range(current_term_2, len(ordered_numbers_2)):
            merged_list.append(ordered_numbers_2[i])

    elif current_term_2 == len(ordered_numbers_2):
        for i in range(current_term_1, len(ordered_numbers_1)):
            merged_list.append(ordered_numbers_1[i])

    
    return merged_list
