





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
    return sum / len(numbers)




def largest_element(numbers):
     
    if len(numbers) == 0:
        return None
    
    greatest_element = numbers[0]
    for i in range(len(numbers)): 
        if numbers[i] > greatest_element:
            greatest_element = numbers[i]
    return greatest_element





def all_equal(my_list):
    
    if len(my_list) == 0:
        return None

    
    
    for i in range(len(my_list)):
        if my_list[0] != my_list[i]:
            return False
    return True






def alternate_sum(numbers):
    
    if len(numbers) == 0:
        return 0
    
    sum = 0 
    for i in range(len(numbers)):
        if i % 2 == 0: 
            sum += numbers[i]
        else: 
            sum -= numbers[i]
    return sum



def is_ordered(numbers, is_strict):
    
    if len(numbers) == 0:
        return True
    
    if is_strict is False:
        
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                return False
    
    else: 
        for i in range(1, len(numbers)):
            
            if numbers[i] <= numbers[i - 1]:
                return False
    
    
    return True



def rotate_right(my_list):
    
    
    if len(my_list) <= 1:
        return my_list

    
    store = my_list[len(my_list) - 1]
    for i in range(len(my_list) - 1, 0, -1):
        
        my_list[i] = my_list[i - 1]

    
    my_list[0] = store
    return my_list



def weird_double(numbers):
    if len(numbers) == 0:
        return numbers
    
    i = 0 
    while i < len(numbers): 
        
        if numbers[i] % 3 != 0:
            numbers[i] *= 2
            i += 1 
        else:
            i += 4 
       
    return numbers



def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    if len(ordered_numbers_1) == 0:
        return ordered_numbers_2
    if len(ordered_numbers_2) == 0:
        return ordered_numbers_1
    
    i = 0
    j = 0
    combined_list = []
    while i < len(ordered_numbers_1) and j < len(ordered_numbers_2):
        
        if ordered_numbers_1[i] < ordered_numbers_2[j]:
            combined_list.append(ordered_numbers_1[i])
            i += 1
            if i == len(ordered_numbers_1):
                
                
                while j < len(ordered_numbers_2):
                    combined_list.append(ordered_numbers_2[j])
                    j += 1
        else:
            
            combined_list.append(ordered_numbers_2[j])
            j += 1
            if j == len(ordered_numbers_2):
                while i < len(ordered_numbers_1):
                    combined_list.append(ordered_numbers_1[i])
                    i += 1

    return combined_list
        


            
            
