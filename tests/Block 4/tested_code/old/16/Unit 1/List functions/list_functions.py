





def count_number_larger_than(target, numbers):
    count_larger_than = 0
    for i in range (len(numbers)):
        if numbers[i] > target:
            count_larger_than += 1
    return count_larger_than




def average(numbers):
    if len(numbers) < 1:
        return None

    sum_of_all = 0
    for i in range (len(numbers)): 
        sum_of_all += numbers[i]
    average = sum_of_all/(len(numbers))
    return average



def largest_element(numbers):
    if len(numbers) < 1:
        return None
    elif len(numbers) < 2:
        return numbers[0]

    
    else:
        largest_num = numbers[0]
        for i in range (0,len(numbers)):
            if numbers[i] > largest_num:
                largest_num = numbers[i]
        
    return largest_num



def all_equal(my_list):
    if len(my_list) < 1:
        return True
    elif len(my_list) < 2:
        return True

    for i in range (len(my_list) - 1):
        if my_list[i] != my_list[0]:
            return False
        
    return True
    

    


def alternate_sum(numbers):
    total_sum = 0
    for i in range (len(numbers)):
        if i % 2 == 0:
            total_sum += numbers[i]
        elif i % 2 == 1:
            total_sum -= numbers[i]

    return total_sum





def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return None

    
    if is_strict:
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i+1]:
                return False
        return True
    else:  
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                return False
        return True




def rotate_right(my_list):
    if len(my_list) == 0:
        return my_list

    last_index = len(my_list) - 1
    storage_bin = my_list[last_index]
    i = last_index
    while i < len(my_list) and i >= 1:
        my_list[i] = my_list[i-1]
        i -= 1
    my_list[0] = storage_bin
    return my_list






def weird_double(numbers):
    current_term = 0
    while current_term < len(numbers):
        if numbers[current_term] % 3 == 0:
            current_term += 3 
        else:
            numbers[current_term] = numbers[current_term] * 2

        current_term += 1
        
    return numbers







def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    new_ordered_numbers = [] 
    count_1 = 0
    count_2 = 0
    
    while count_1 < len(ordered_numbers_1) and count_2 < len(ordered_numbers_2):
        if ordered_numbers_1[count_1] >= ordered_numbers_2[count_2]:
            new_ordered_numbers.append(ordered_numbers_2[count_2])
            count_2 += 1
        elif ordered_numbers_1[count_1] < ordered_numbers_2[count_2]:
            new_ordered_numbers.append(ordered_numbers_1[count_1])
            count_1 += 1


    
    if len(ordered_numbers_1) > len(ordered_numbers_2):
        while count_1 < len(ordered_numbers_1):
            new_ordered_numbers.append(ordered_numbers_1[count_1])
            count_1 += 1
    else:
        while count_2 < len(ordered_numbers_2):
            new_ordered_numbers.append(ordered_numbers_2[count_2])
            count_2 += 1
    return new_ordered_numbers



            
            








