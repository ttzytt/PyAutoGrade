









def count_number_larger_than(target, numbers):
    count = 0 
    for i in range(len(numbers)):
        if numbers[i] > target : 
            count += 1 
    return count


def average(numbers):
    if len(numbers) == 0: 
        return 0
      
    
    sum_function = 0 
    for i in numbers:
        sum_function = i + sum_function
    return sum_function/len(numbers) 



def largest_element(numbers):
    
    if len(numbers) == 0: 
        return 0
      
    else: 
        max_value = numbers[0] 
        for i in numbers: 
            if (i > max_value): 
                max_value = i
        return max_value




def all_equal(my_list):
    
    if len(my_list) <= 1:
        return True
    
    
    for i in range(1, len(my_list)):
        if my_list[0] != my_list[i]:
            return False
    return True




        

def alternate_sum(numbers):
    total_sum = 0 
    for i in range(len(numbers)):
        if i % 2 == 0: 
            total_sum += numbers[i] 
        else: 
            total_sum -= numbers[i] 
    return total_sum




def is_ordered(numbers, is_strict):
    is_ordered = True

    if len(numbers) <= 1:
        return True
    
    for number in range(1,len(numbers)-1):
        if is_strict == True:
            if numbers[number] >= numbers[number + 1]:
                return False
            
        elif is_strict == False:
            if numbers[number] > numbers[number + 1]:
                return False
            
        else: 
            if numbers[number] < numbers[number+1]:
                return True
    return True




def rotate_right(my_list):
    if len(my_list) <= 1:
        return my_list

    new_list = []

    new_list.append(my_list[len(my_list)-1])
    for i in range(len(my_list)-1):
      new_list.append(my_list[i])  
        
    return new_list
        



def weird_double(numbers):
    if len(numbers) <= 1:
        return numbers
    
    new_list = []
    skip_number = 0
    i = 0
    while i < len(numbers):
        if numbers[i] % 3 == 0:
            i += 4
        else:
            numbers[i] *= 2
            i += 1
    return numbers

def merge_ordered_lists(ordered_numbers_1,ordered_numbers_2):
    if (len(ordered_numbers_1) <= 1) and (len(ordered_numbers_2)) <= 1: 

        if ((len(ordered_numbers_1)) and (len(ordered_numbers_2))) == 1:
            return ordered_numbers_1 + ordered_numbers_2 
        
        elif (len(ordered_numbers_1)) == 0:
            
            return ordered_numbers_2
        
        else:
            return ordered_numbers_1

    
    point_1 = 0
    point_2 = 0
    my_list = []
    list_1_lastelement = ordered_numbers_1[len(ordered_numbers_1) - 1]
    list_2_lastelement = ordered_numbers_2[len(ordered_numbers_2) - 1]

    
    if list_1_lastelement <= list_2_lastelement: 
        while point_2 < len(ordered_numbers_2): 
            if ordered_numbers_1[point_1] <= ordered_numbers_2[point_2]:
                my_list.append(ordered_numbers_1[point_1]) 
                point_1 += 1
                if point_1 == len(ordered_numbers_1):
                    while point_2 < len(ordered_numbers_2):
                        my_list.append(ordered_numbers_2[point_2])
                        point_2 += 1
            else:
                my_list.append(ordered_numbers_2[point_2])
                point_2 += 1
            
        
    else:
        while point_1 < len(ordered_numbers_1):
            if ordered_numbers_2[point_2] <= ordered_numbers_1[point_1]:
                my_list.append(ordered_numbers_2[point_2])
                point_2 += 1
                if point_2 == len(ordered_numbers_2):
                    while point_1 < len(ordered_numbers_1):
                        my_list.append(ordered_numbers_1[point_1])
                        point_1 += 1
            else:
                my_list.append(ordered_numbers_1[point_1])
                point_1 += 1

    return my_list
        
                

    


        
    
            


