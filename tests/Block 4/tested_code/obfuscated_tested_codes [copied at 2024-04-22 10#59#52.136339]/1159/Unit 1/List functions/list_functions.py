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

    if len(numbers) == 0:
        return None

    total = 0
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



def alternate_sum(numbers): 
    
    if len(numbers) == 0:
        return None

    alternate_sum = 0
    for count in range(len(numbers)):
        
        if count % 2 == 0: 
            alternate_sum += numbers[count]
            
        else: 
            alternate_sum -= numbers[count]
            
    return alternate_sum




def is_ordered(numbers, is_strict): 

    if len(numbers) == 0: 
        return None
    
    if is_strict == True: 
        for count in range(len(numbers)-1):
            if numbers[count+1] <= numbers[count]:
                return False
            
    elif is_strict == False: 
        for count in range(len(numbers)-1):
            if numbers[count+1] < numbers[count]:
                return False
            
    return True 
    
  


def rotate_right(my_list): 

    new_list = [] 

    new_list.append(my_list[len(my_list)-1])
    
    for count in range(len(my_list)-1):
        new_list.append(my_list[count])

    return new_list
        

    '''
    count = 0
    store_1 = my_list[0]
    my_list[0] = my_list[len(my_list)-1]
    # I set up few variables (e.g. store_1 & store_2) so that when I rotate the numbers,
    # the original value can be stored
        
    for count in range(1,len(my_list)):
        
        store_2 = my_list[count]
        my_list[count] = store_1
        count += 1
        store_1 = store_2
        
    return my_list
    '''




def weird_double(numbers): 
    
    count = 0
    while count < len(numbers):
        
        if numbers[count] % 3 == 0: 
            count += 3 
            
        else:
            numbers[count] *= 2
            
        count += 1 
        
    return numbers


'''
Thanks to Mark Zhao for helping me adding comments
'''

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2): 
    
    if len(ordered_numbers_1) == 0 or len(ordered_numbers_2) == 0: 
        if len(ordered_numbers_1) == 0 and len(ordered_numbers_2) == 0:
            return None
        elif len(ordered_numbers_1) == 0 and len(ordered_numbers_2) != 0:
            return ordered_numbers_2
        elif len(ordered_numbers_1) != 0 and len(ordered_numbers_2) == 0:
            return ordered_numbers_1

    
    
    
    output = []
    count_1 = 0
    count_2 = 0
    
    
    
    while count_1 < len(ordered_numbers_1) and count_2 < len(ordered_numbers_2):
        
        if ordered_numbers_1[count_1] >= ordered_numbers_2[count_2]: 
            output.append(ordered_numbers_2[count_2])
            count_2 += 1
            
            
        else:
            output.append(ordered_numbers_1[count_1])
            count_1 += 1
            
    
    
    if count_1 == len(ordered_numbers_1):
        for count_2 in range(count_2,len(ordered_numbers_2)):
            output.append(ordered_numbers_2[count_2])
            
    elif count_2 == len(ordered_numbers_2):
        for count_1 in range(count_1,len(ordered_numbers_1)):
            output.append(ordered_numbers_1[count_1])

    return output




'''
When writing a code, when one variable decides whether to shut
the program or proceed, such as return False if a different v-
alue is detected, that variable should be placed at first

'''

