





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




        
    










