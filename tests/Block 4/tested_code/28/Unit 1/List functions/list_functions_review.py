






def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count += 1
    return count
    


def average(numbers):
    if len(numbers) == 0:
        return None
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    average = sum / len(numbers)
    return average


def largest_element(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number



def all_equal(my_list):
    if len(my_list) == 0:
        return None
    
    
    target_value = my_list[0]
    
    
    
    
    is_bool = type(my_list[0]) == bool 
    for i in range(len(my_list)):
        
        if not (type(my_list[i]) == bool) == is_bool:
            return False
        if not my_list[i] == target_value:
            return False
    
    
    
    return True

    
    
    
    
    
    
    
