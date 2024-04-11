








def count_number_larger_than(target, numbers):
    if len(numbers) == 0:
        return 0
    count = 0
    for i in range(0,len(numbers)):
        if numbers[i] > target:
            count += 1
        elif numbers[i] < target: 
            count == count
    return count




def average(numbers):
    if len(numbers) == 0:
        return 0
    
    sum = 0
    for i in list(numbers):
        sum += i
    return (sum) / (len(numbers)) 




def largest_element(numbers):
    if len(numbers) == 0:
        return 0
    
    max_value = numbers[0]
    for i in numbers:
        if (i > max_value):
           max_value = i
    return max_value





def all_equal(my_list):
    if len(my_list) == 0:
        return True
    elif len(my_list) == 1:
        return True

    first = my_list[0]
    for i in range(1,len(my_list)):
        if first != my_list[i]:
            return False
    return True



def alternate_sum(numbers):
    result = 0
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result += numbers[i]
        else:
            result -= numbers[i]
            
    return result




def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return None

    previous_number = numbers[0]
    
    if is_strict == True:
        for i in range(1, len(numbers)):
            if previous_number >= numbers[i]:
                return False
    else:
        for i in range(1, len(numbers)):
            if previous_number > numbers[i]:
                return True
    return True
            




def rotate_right(my_list):
    if len(my_list) == 0:
        return None
    
    
    blank = []
    rotated = blank

    
    rotated.append(my_list[len(my_list)-1])
    
    for i in range(len(my_list)-1):
        rotated.append(my_list[i])
        
    return rotated




    
    
    
