







def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count = count + 1         
    return count  



def average(numbers):
    if len(numbers) == 0:
        return None
    
    total = 0
    for i in range(len(numbers)):
        total = numbers[i] + total
    return (total / len(numbers))



def largest_element(numbers):
    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest




def all_equal(my_list):
    if len(my_list) == 0: 
        return None
    for i in range(len(my_list) - 1):
        
        if my_list[i] != my_list[i + 1]:
           return False
    return True 




def alternate_sum(numbers):
    sums = 0
    for i in range(len(numbers)):
        
        if i % 2 == 0:  
            sums = sums + numbers[i] 
        elif i % 2 == 1:  
            sums = sums - numbers[i]
    return sums




def is_ordered(numbers, is_strict):
    if len(numbers) == 0 or len(numbers) == 1:
        return None
    
    count = 0 
    for i in range(len(numbers) - 1):
        if is_strict: 
            if numbers[i] < numbers[i + 1]:
                count = count + 1
            else:
                return False 
        else:  
            if numbers[i] <= numbers[i + 1]:
                count = count + 1
            else:
                return False 

    
    
    if count == len(numbers) - 1:
       return True
    


def rotate_right(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list
    temp = my_list[len(my_list) - 1] 
                                     
    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]   
    my_list[0] = temp
    print(my_list)
    return my_list 

def weird_double(numbers):
    index = 0
    
    while(index < len(numbers)):
        if numbers[index] % 3 == 0:
            index = index + 3
            
        else:
            numbers[index] = 2 * numbers[index]
        index = index + 1
        
    print(numbers)
    return numbers
        
def merge_ordered_list(ordered_numbers_1, ordered_numbers_2):
    list_1 = ordered_numbers_1
    list_2 = ordered_numbers_2
    list_merged = []
    
    index_1 = 0
    index_2 = 0

    
    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1] <= list_2[index_2]:
            list_merged.append(list_1[index_1])
            index_1 = index_1 + 1
        else:
            list_merged.append(list_2[index_2])
            index_2 = index_2 + 1
            
    while index_2 < len(list_2):
        list_merged.append(list_2[index_2])
        index_2 = index_2 + 1

    while index_1 < len(list_1):
        list_merged.append(list_1[index_1])
        index_1 = index_1 + 1
        
    print(list_merged)
    return list_merged    
        
             
