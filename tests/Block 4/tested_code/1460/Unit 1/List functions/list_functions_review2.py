




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

    
    
    
    
    
    
    



def alternate_sum(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    
    for i in range(0,len(numbers),2):
        total += numbers[i]
    
    for i in range(1,len(numbers),2):
        total -= numbers[i]
    return total











def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return True
    if is_strict:
        for i in range(1,len(numbers)):
            if not numbers[i] > numbers[i-1]:
                return False
        return True
    
    for i in range(1,len(numbers)):
        if not numbers[i] >= numbers[i-1]:
            return False
    return True



def rotate_right(my_list):
    if len(my_list) == 0:
        return my_list
    
    
    last_element = my_list[len(my_list)-1]
    rotated_list = [last_element]
    for i in range(len(my_list)-1): 
        rotated_list.append(my_list[i])
    return rotated_list
