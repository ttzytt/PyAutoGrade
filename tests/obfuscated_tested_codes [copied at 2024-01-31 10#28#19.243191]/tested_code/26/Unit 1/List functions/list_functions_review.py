






def count_number_larger_than(target, numbers):
    greater_count = 0 
    for number in numbers: 
        if number > target:
            greater_count += 1
    return greater_count




def average(numbers):
    average = 0
    if len(numbers) == 0:
        return "Empty list" 
                            
                            
    for number in numbers:
        average += number 
    average /= len(numbers) 
                            
                            
    return average



def largest_element(numbers):
    if len(numbers) == 0:
        return "Empty list"
    
    maximum = numbers[0] 
    for number in numbers:
        if number > maximum: 
            maximum = number 
                             
    return maximum




def all_equal(my_list):
    if len(my_list) == 0:
        return "Empty list"


    comparison_value = my_list[0] 
                                  
    for element in my_list:
        if element is not comparison_value: 
                                            
            return False
    return True 
