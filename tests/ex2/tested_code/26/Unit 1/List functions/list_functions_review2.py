





def count_number_larger_than(target, numbers):
    greater_count = 0 
    for i in range(len(numbers)):
        if numbers[i] > target:
            greater_count += 1
    return greater_count




def average(numbers):
    average = 0
    if len(numbers) == 0:
        return "Empty list" 
                            
                            
    for i in range(len(numbers)):
        average += numbers[i] 
    average /= len(numbers)
    return average



def largest_element(numbers):
    if len(numbers) == 0:
        return "Empty list"
    
    current_maximum = numbers[0] 
    for i in range(len(numbers)):
        if numbers[i] > current_maximum: 
            current_maximum = numbers[i] 
                                         
                                         
    return current_maximum




def all_equal(my_list):
    if len(my_list) == 0:
        
        return "Empty list"


    comparison_value = my_list[0] 
                                  
    for i in range(len(my_list)):
        if my_list[i] is not comparison_value: 
                                               
            return False
    return True 





def alternate_sum(numbers):
    
    
    
    
    
    
    alternating_sum = 0
    for i in range(len(numbers)):
        if i % 2 == 0: 
            alternating_sum += numbers[i]
        else: 
            alternating_sum -= numbers[i]
    return alternating_sum






def is_ordered(numbers, is_strict):
    if is_strict:
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i + 1]: 
                return False                
                                            
    else:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]: 
                return False

    return True




def rotate_right(my_list):
    if len(my_list) == 0:
        return []
    
    rotated_list = []
    rotated_list.append(my_list[len(my_list) - 1]) 
                                                   
                                                   
                                                   
    for i in range(len(my_list) - 1): 
        rotated_list.append(my_list[i])
    return rotated_list









