'''
DO NOT RUN THIS PROGRAM

'''






def count_number_larger_than(target, numbers):
    total = 0
    for count in range(len(numbers)):
        if numbers[count] > target:
            total += 1
    return total
    
            



def average(numbers):
    total = 0
    if len(numbers) == 0:
        return None
    
    for count in range(len(numbers)):
        total += numbers[count] 
    return total/len(numbers) 




def largest_element(numbers):
    if len(numbers) == 0:
        return None
    
    max = numbers[0]
    
    for count in range(len(numbers)):
        if numbers[count] >= max: 
            max = numbers[count] 
    return max




def all_equal(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return True
    for count in range(len(numbers)-1):
          if numbers[count] != numbers[count+1]:
              return False 
    return True 



def alternate_sum(nums):
    total = 0
    if len(nums) == 0:
        return None
    
    
    for count in range(len(nums)):
        
        if count == 0 or count % 2 == 0: 
            total += nums[count]
        elif count % 2 == 1: 
            total -= nums[count]
    return total




def is_ordered(numbers, is_strict):
    
    if is_strict == True: 
        for count in range(len(numbers)-1):
            if numbers[count] >= numbers[count+1]:
                return False
    elif is_strict == False: 
        for count in range(len(numbers)-1):
            if numbers[count] > numbers[count+1]:
                return False
    return True
    
  


def rotate_right(my_list): 
    
    
    count = 0
    f = my_list[0]
    
    
    my_list[0] = my_list[len(my_list)-1]
    for count in range(1,len(my_list)):
        g = my_list[count]
        my_list[count] = f
        count += 1
        f = g
    return my_list




def weird_double(numbers):
    count = 0
    while count < len(numbers):
        if numbers[count] % 3 == 0:
            numbers[count] += 0
            count += 3 
        else:
            numbers[count] *= 2
        count += 1 
    return numbers



def merge_ordered_lists(numbers1, numbers2):
    
    if len(numbers1) == 0 or len(numbers2) == 0: 
        if len(numbers1) == 0 and len(numbers2) == 0:
            return None
        elif len(numbers1) == 0 and len(numbers2) != 0:
            return numbers2
        elif len(numbers1) != 0 and len(numbers2) == 0:
            return numbers1

    
    
    
    output = []
    c1 = 0
    c2 = 0
    
    
    while c1 < len(numbers1) and c2 < len(numbers2):
        if numbers1[c1] >= numbers2[c2]: 
            output.append(numbers2[c2])
            c2 += 1
            
        elif numbers1[c1] < numbers2[c2]:
            output.append(numbers1[c1])
            c1 += 1
            
    
    
    if c1 == len(numbers1):
        while c2 < len(numbers2): 
            output.append(numbers2[c2])
            c2 += 1
            
    elif c2 == len(numbers2):
        while c1 < len(numbers1):
            output.append(numbers1[c1])
            c1 += 1

    return output


'''
When writing a code, when one variable decides whether to shut
the program or proceed, such as return False if a different v-
alue is detected, that variable should be placed at first, br-
eak is not recommended.
'''


