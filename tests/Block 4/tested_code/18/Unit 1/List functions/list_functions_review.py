



def count_number_larger_than(target, numbers):
    count = 0  
    for i in range(len(numbers)):
        if numbers[i] > target: 
            count += 1 
    return count 

  



def average(numbers):
    if len(numbers) == 0:
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
    
    for i in range(len(my_list) - 1):
        if my_list[i] is my_list[i+1]:
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
        if i % 2 == 0:  
            result += numbers[i] 
        else:  
            result -= numbers[i]

    return result





def is_ordered(numbers, is_strict):
    if len(numbers) < 1: 
        return True
    
    for i in range(1, len(numbers)):
        if is_strict: 
            if numbers[i] <= numbers[i-1]: 
                return False
        else:
            if numbers[i] < numbers[i-1]:
                return False

    return True



def rotate_right(my_list):
    if len(my_list) == 0:
        return my_list  

    
    last_element = my_list[-1]

    
    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]

    
    my_list[0] = last_element

    return my_list




def weird_double(numbers):
    i = 0  
    result = []
    if len(numbers) == 0: 
        return 

    while i < len(numbers):
        if numbers[i] % 3 == 0:
            
            result += [numbers[i]]
            i += 1  
            skip = 0
            while skip < 3 and i < len(numbers):  
                result += [numbers[i]]
                i += 1
                skip += 1
        else:
            result += [numbers[i] * 2]
            i += 1

    return result


def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    if len(ordered_numbers_1) == 0: 
        return ordered_numbers_2
    elif len(ordered_numbers_2) == 0: 
        return ordered_numbers_1

    index_1 = 0 
    index_2 = 0 
    return_list = []

    while index_1 < len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        if ordered_numbers_1[index_1] < ordered_numbers_2[index_2]:
            return_list += [ordered_numbers_1[index_1]] 
            index_1 += 1 
        elif ordered_numbers_1[index_1] > ordered_numbers_2[index_2]:
            return_list += [ordered_numbers_2[index_2]]
            index_2 += 1
        else:
            return_list += [ordered_numbers_1[index_1], ordered_numbers_2[index_2]]
            index_1 += 1
            index_2 += 1

    while index_1 < len(ordered_numbers_1):
        return_list += [ordered_numbers_1[index_1]]
        index_1 += 1

    while index_2 < len(ordered_numbers_2):
        return_list += [ordered_numbers_2[index_2]]
        index_2 += 1

    return return_list
