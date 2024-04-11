


def count_number_larger_than(target, numbers):
    i = 0
    total = 0
    while i < len(numbers):
        if numbers[i] > target:
            total += 1
            i += 1
        else:
            total += 0  
            i += 1
    return total  


def average(numbers):
    i_2 = 0
    sum_1 = 0
    
    
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    
    else:
        while i_2 < len(numbers):
            sum_1 += numbers[i_2]
            i_2 += 1
        return (sum_1/len(numbers))


def largest_element(numbers):
    i = 0
    i_1 = 0
    
    
    max_1 = -999999999999999
    min_1 = 9999999         
                            
    
    
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    
    while i < len(numbers):
        if numbers[i] > max_1:
            max_1 = numbers[i]
            i = i + 1
        else:
            i += 1
    return max_1
    
    


def all_equal(my_list):
    i_3 = 0
    sum_2 = 0
    i_4 = 0
    while i_3 < len(my_list):
        sum_2 += my_list[i_3]
        i_3 += 1
    
    while i_4 < len(my_list):
        if my_list[i_4] != (sum_2/(len(my_list))):
            return False
        i_4 += 1
    return True


    
    


