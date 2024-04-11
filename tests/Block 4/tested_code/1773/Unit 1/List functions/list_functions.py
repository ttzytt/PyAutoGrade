






def count_number_larger_than(target, numbers):
    counter = 0                             
    for i in range(len(numbers)):           
        if numbers[i] > target:             
            counter += 1                    
    return counter                          




def average(numbers):                       
    if not numbers:                         
        return None                         
    total = 0                               
    counter = len(numbers)                  
    for i in range(counter):                
        total += numbers[i]                 
    average = total/counter                 
    return average                          




def largest_element(numbers):               
    if not numbers:                         
        return None                         
    largest_element = numbers[0]            
    for i in range(len(numbers)):           
        if numbers[i] > largest_element:    
            largest_element = numbers[i]    
    return largest_element                  
        




def all_equal(my_list):
    if not my_list:                         
        return None                         
    counter = 0                             
    all_equal = my_list[0]                  
    for i in range(len(my_list)):           
        if my_list[i] == all_equal:         
            counter += 1                    
        else:                               
            counter = counter               
        if counter == (len(my_list)):       
            return True                     
        else:                               
            return False                    



def alternate_sum(numbers):                 
    if not (numbers):                               
        return 0
    sum = 0
    counter = len(numbers)                          
    for i in range(counter):                        
        if i % 2 == 0:                          
            sum += numbers[i]        
        else:                               
            sum -= numbers[i]     
    return sum                             



def is_ordered(numbers, is_strict):
    if not (numbers):
        return None
    
    prev_number = numbers[0]
    
    if is_strict:
        for i in range(1, len(numbers)):
            if numbers[i] <= prev_number:
                return False
            else:
                prev_number = numbers[i]

    if not is_strict:
        for i in range(1, len(numbers)):
            if numbers[i] < prev_number:
                return False
            else:
                prev_number = numbers[i]


        return True


def rotate_right1(my_list)
    if nums < 2:
        return None
    

    for i in range(n)
    
    
    
