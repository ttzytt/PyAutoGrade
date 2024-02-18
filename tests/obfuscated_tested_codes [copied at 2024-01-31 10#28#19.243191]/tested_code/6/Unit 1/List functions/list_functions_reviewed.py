






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
    


