



def count_number_larger_than(target, numbers):
    count = 0 
    for i in range(len(numbers)):
        if numbers[i] > target:
            count = count + 1
            
    return count


def average(numbers):
    sum_now = 0
    if len(numbers) != 0:
        for i in range(len(numbers)):
            sum_now += numbers[i] 
        return sum_now/len(numbers) 
    else: 
        return 0 


def largest_element(numbers):
    
    
    if len(numbers) == 0:
        return 0
    
    largest = numbers[0]
    for i in range(len(numbers)):
        
        if numbers[i] > largest:
            
            largest = numbers[i]
    return largest

 
def all_equal(my_list):
    for i in range(len(my_list)):
        
        if my_list[0] != my_list[i]:
            return False
        
    return True 


def alternative_sum(nums):
    sums = 0
    for i in range(len(nums)):
         if i % 2 == 0: 
             sums = sums + nums[i]
             
         elif i % 2 == 1: 
            sums = sums - nums[i]
    return sums


def is_ordered(numbers, is_strict):
    
    
    if is_strict == True:
        for i in range(len(numbers)-1):
            if numbers[i] >= numbers[i+1]:
                return False
        return True
    
    
    else:
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                return False
        return True


def rotate_right(lists):
    
    A = [lists[-1]] 
    
    for i in range(0,len(lists)-1):
        
        
        
        A.append(lists[i])
    return A


def weird_double(numbers):
    count = 0 
    while count < len(numbers):
        if numbers[count] % 3 == 0: 
            count += 3 
        else:
            numbers[count] *= 2 
        count += 1
    return numbers



def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(ordered_numbers_1) and j < len(ordered_numbers_2):
        if ordered_numbers_1[i] < ordered_numbers_2[j]:
            merged_list.append(ordered_numbers_1[i])
            i += 1
        else:
            merged_list.append(ordered_numbers_2[j])
            j += 1
    
    while i < len(ordered_numbers_1):
        merged_list.append(ordered_numbers_1[i])
        i += 1

    while j < len(ordered_numbers_2):
        merged_list.append(ordered_numbers_2[j])
        j += 1
    
    return merged_list
