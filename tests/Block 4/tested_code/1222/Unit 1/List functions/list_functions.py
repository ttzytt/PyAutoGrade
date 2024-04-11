





def count_number_larger_than(target, numbers):
    if len(numbers) == 0:
        return 0
    count = 0
    for i in range(0,len(numbers)):
        if numbers[i] > target:
            count += 1
        elif numbers[i] <= target: 
            count == count
    return count




def average(numbers):
    if len(numbers) == 0:
        return 0
    
    sum = 0
    for i in list(numbers):
        sum += i
    return (sum) / (len(numbers)) 




def largest_element(numbers):
    if len(numbers) == 0:
        return 0
    
    max_value = numbers[0]
    for i in numbers:
        if (i > max_value):
           max_value = i
    return max_value





def all_equal(my_list):
    if len(my_list) == 0:
        return True
    elif len(my_list) == 1:
        return True

    first = my_list[0]
    for i in range(1,len(my_list)):
        if first != my_list[i]:
            return False
    return True



def alternate_sum(numbers):
    result = 0
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result += numbers[i]
        else:
            result -= numbers[i]
            
    return result




def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return None

    previous_number = numbers[0]
    
    if is_strict == True:
        for i in range(1, len(numbers)):
            if previous_number >= numbers[i]:
                return False
    else:
        for i in range(1, len(numbers)):
            if previous_number > numbers[i]:
                return True
    return True
            



def rotate_right(my_list):
    if len(my_list) == 0:
        return None
    
    
    rotated = []

    
    rotated.append(my_list[len(my_list)-1])
    
    for i in range(len(my_list)-1):
        rotated.append(my_list[i])
        
    return rotated




def weird_double(numbers):
    if len(numbers) == 0:
        return None
    
    
    i = 0
    
    while i < len(numbers):
        
        if numbers[i] % 3 == 0:
            i += 4
        
        elif numbers[i] % 3 != 0:
            numbers[i] *= 2
            i += 1
    return numbers


def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):

    new_list = []
    count_1 = 0
    count_2 = 0
    list_1 = ordered_numbers_1
    list_2 = ordered_numbers_2
    
    while count_1 < len(list_1) and count_2 < len(list_2):
        
        
        if list_1[count_1] < list_2[count_2]:
            new_list.append(list_1[count_1])
            count_1 += 1
        
        else:
            new_list.append(list_2[count_2])
            count_2 += 1
            
    
    i_1 = count_1
    i_2 = count_2

    
    if i_1 < len(list_1):
        for i_1 in range(i_1, len(list_1)):
            new_list.append(list_1[i_1])
    
    elif i_2 < len(list_2):
        for i_2 in range(i_2, len(list_2)):
            new_list.append(list_2[i_2])

    return new_list



    





    
    
    
