





def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count = count + 1
    return count




def average(numbers):
    
    if numbers == []:
        return None
    
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i] 
    average = sum / len(numbers) 
    return average





def largest_element(numbers):
    
    if numbers == []:
        return None

    largest = numbers[0]
    for i in range(len(numbers)):
        
        
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

    



def all_equal(my_list):

    for i in range(len(my_list) - 1): 
        if my_list[i] != my_list[i + 1]: 
            return False
    return True





def alternate_sum(numbers):
    
    result = 0
    for i in range(len(numbers)):
        
        
        result = result + (numbers[i] * ((-1) ** i))
    return result







def is_ordered(numbers, is_strict):
    
    if is_strict == True:
        
        
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i + 1]:
                return False
            
    
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True





def rotate_right(my_list):
    
    if my_list == []:
        return my_list

    
    my_new_list = []
    for i in range(len(my_list)):
        my_new_list.append(my_list[i - 1])
    return my_new_list







def weird_double(numbers):
    
    if numbers == []:
        return numbers
    
    element = 0
    while element < len(numbers):
        if numbers[element] % 3 == 0:
            element = element + 4 
        else:
            numbers[element] = 2 * numbers[element]
            element = element + 1 
    return numbers
 




def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    new_list = []
    element_1 = 0
    element_2 = 0

    
    
    
    while element_1 < len(ordered_numbers_1) and element_2 < len(ordered_numbers_2):
        if ordered_numbers_1[element_1] >= ordered_numbers_2[element_2]:
            new_list.append(ordered_numbers_2[element_2])
            element_2 = element_2 + 1
        else:
            new_list.append(ordered_numbers_1[element_1])
            element_1 = element_1 + 1

    
    
    
    if element_1 < len(ordered_numbers_1):
        for not_add_1 in range(element_1,len(ordered_numbers_1)):
            new_list.append(ordered_numbers_1[not_add_1])
    else:
        for not_add_2 in range(element_2,len(ordered_numbers_2)):
            new_list.append(ordered_numbers_2[not_add_2])
        
    return new_list       
  
