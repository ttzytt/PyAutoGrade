






def count_number_larger_than(target, numbers):
    nums = 0
    parameter = int(target)
    for i in range(len(numbers)):
        if numbers[i] > parameter:
            nums += 1
    return nums
        

    

def average(numbers):
    if numbers == []:
        return 0
    
    avg = 0
    for i in range(len(numbers)):
        avg = avg + numbers[i]
    return avg/len(numbers)



def largest_element(numbers):
    if numbers == []:
        return None  

    max_element = numbers[0] 

    for num in range(len(numbers)):
        if num > max_element:
            max_element = num  

    return max_element

        




def all_equal(my_list):
    for i in range(len(my_list)- 1):
        if my_list[i] != my_list[i + 1]:
            return False   
    return True



def alternate_sum(numbers):
    result = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            result += numbers[i]  
        else:
            result -= numbers[i]  
    return result






def is_ordered(numbers, is_strict):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            return False
        elif numbers[i] == numbers[i + 1]:
            if is_strict:
                return False
        
    return True










def rotate_right(my_list):
    if len(my_list) <= 1:
        return my_list
    last_element = my_list[-1]  

    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]

    my_list[0] = last_element  

    return my_list






def weird_double(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] % 3 == 0:
            i += 4
        else:
            numbers[i] *= 2
            i += 1

    return numbers



def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    merged_list = []
    first_list = second_list = 0

    while first_list < len(ordered_numbers_1) and second_list < len(ordered_numbers_2):
        if ordered_numbers_1[first_list] < ordered_numbers_2[second_list]:
            merged_list.append(ordered_numbers_1[first_list])
            first_list += 1
        else:
            merged_list.append(ordered_numbers_2[second_list])
            second_list += 1

    while first_list < len(ordered_numbers_1):
        merged_list.append(ordered_numbers_1[first_list])
        first_list += 1
        
    while second_list < len(ordered_numbers_2):
        merged_list.append(ordered_numbers_2[second_list])
        second_list += 1

    return merged_list
        
        









  
