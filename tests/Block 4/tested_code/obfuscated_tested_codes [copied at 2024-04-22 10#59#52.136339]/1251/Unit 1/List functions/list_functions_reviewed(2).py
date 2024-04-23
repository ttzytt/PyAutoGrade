




def count_number_larger_than(target, numbers):
    result = 0
    for i in range(0,len(numbers)):
        if numbers[i] > target:
            result += 1
    return result



def average(numbers):
    if len(numbers) != 0:
        sum_ = 0
        for i in range(0,len(numbers)):
            sum_ = sum_ + numbers[i]
        return sum_ / len(numbers)
    else:
        return 0



def largest_element(numbers):
    if len(numbers) != 0:
        maximum = numbers[0]
        for i in range(0,len(numbers)-1):
            if numbers[i+1] > numbers[i]:
                maximum = numbers[i+1]
        return maximum
    else:
        return 0


def all_equal(my_list):
    if len(my_list) > 1:
        for i in range(0,len(my_list)):
            if my_list[i] != my_list[i-1]: 
                return False
                break
        return True
    else:
        return True

def alternate_sum(numbers):
    
    if len(numbers) == 0:
        return None

    
    result = 0
    for i in range(0,len(numbers)):
        result = result + numbers[i] * ((-1)**i)
    return result





def is_ordered(nums, is_strict):
    if len(nums) == 0:
        return True
    
    
    if is_strict == True:
        for i in range(0,len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
    else:
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True



def rotate_right(my_list):
    if len(my_list) <= 1:
        return my_list
    X=[1]
    X[0]=my_list[len(my_list)-1]   
    for i in range(1,len(my_list)):
        X.append(my_list[i-1])
             
    return X

def count_number_larger_than(target, numbers):
    result = 0
    for i in range(0,len(numbers)):
        if numbers[i] > target:
            result += 1
    return result



def average(numbers):
    if len(numbers) != 0:
        sum_ = 0
        for i in range(0,len(numbers)):
            sum_ = sum_ + numbers[i]
        return sum_ / len(numbers)
    else:
        return 0



def largest_element(numbers):
    if len(numbers) != 0:
        maximum = numbers[0]
        for i in range(0,len(numbers)-1):
            if numbers[i+1] > numbers[i]:
                maximum = numbers[i+1]
        return maximum
    else:
        return 0


def all_equal(my_list):
    if len(my_list) > 1:
        for i in range(0,len(my_list)):
            if my_list[i] != my_list[i-1]: 
                return False
                break
        return True
    else:
        return True

def alternate_sum(numbers):
    
    if len(numbers) == 0:
        return None

    
    result = 0
    for i in range(0,len(numbers)):
        result = result + numbers[i] * ((-1)**i)
    return result





def is_ordered(nums, is_strict):
    
    if len(nums) == 0:
        return True
    
    
    if is_strict == True:
        for i in range(0,len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
    else:
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True



def rotate_right(my_list):
    if len(my_list) <= 1:
        return my_list
    X=[1]
    X[0]=my_list[len(my_list)-1]   
    for i in range(1,len(my_list)):
        X.append(my_list[i-1])
             
    return X


def weird_double(numbers):
    
    if len(numbers) == 0:
        return None

    i =0
    
    while i <= len(numbers)-1:
        if numbers[i]  % 3 ==0:
             i = i + 4
        else:
            numbers[i] = numbers[i]*2
            i = i + 1
    return numbers

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    if len(ordered_numbers_1) == 0:
        return ordered_numbers_2
    elif len(ordered_numbers_2) == 0:
        return ordered_numbers_1
    
    index_1 = 0
    index_2 = 0
    
    Results = []
    while index_1 < len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        
        
        if ordered_numbers_1[index_1] >=  ordered_numbers_2[index_2]:
            Results.append(ordered_numbers_2[index_2])
            index_2 += 1
            
        else:
            Results.append(ordered_numbers_1[index_1])
            index_1 += 1
    
    if index_1 == len(ordered_numbers_1):
        for i in range(index_2,len(ordered_numbers_2)):
            Results.append(ordered_numbers_2[i])
    else:
        for i in range(index_1,len(ordered_numbers_1)):
            Results.append(ordered_numbers_1[i])
    return Results
    
    
    
        
