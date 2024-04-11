





def count_number_larger_than(target, numbers):
    num_integers = 0
    if len(numbers) == 0:
        return 0
    
    for i in range(len(numbers)):
        if numbers[i] > target:
            num_integers += 1
    return num_integers




def average(numbers):
    if len(numbers) == 0:
        return None
    
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum/len(numbers)




def largest_element(numbers):
    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    
    for i in range(len(numbers)):
        if numbers[i] >= largest:
            largest = numbers[i]

    return largest
    




def all_equal(my_list):
    if len(my_list) == 0:
        return None
    
    for i in range(1,len(my_list)):
        if my_list[i] != my_list[0]:
            return False
    return True





def alternate_sum(numbers):
    if len(numbers) == 0:
        return 0

    end_val = 0
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            end_val += numbers[i]
        else:
            end_val -= numbers[i]
            
    return end_val






def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return None

    prev_number = numbers[0]

    
    
    if is_strict == False:
        for i in range(1,len(numbers)):
            if numbers[i] < prev_number:
                return False
            prev_number = numbers[i]
    
    
    
    else:
        for i in range(1,len(numbers)):
            if numbers[i] <= prev_number:
                return False
            prev_number = numbers[i]
    return True

('''            
def rotate_right(my_list):
    if len(my_list) == 0:
        return None

    prev_element = my_list[0]
    last_element = my_list[len(my_list) - 1]

    for i in range(1, len(my_list)):
        saved_element = my_list[i]
        my_list[i] = prev_element
        prev_element = saved_element

    my_list[0] = last_element

    return my_list
''')




def rotate_right(my_list):
    if len(my_list) == 0:
        return None
    
    last_element = my_list[len(my_list) - 1]

    
    for i in range(len(my_list) - 1, 0 , -1):
        
        my_list[i] = my_list[i - 1]

    my_list[0] = last_element

    return my_list

        



def weird_double(numbers):
    
    if len(numbers) == 0:
        return None
    
    i = 0
    
    while i < len(numbers):
        
        if numbers[i] % 3 != 0:
            numbers[i] *= 2
            
            i += 1
        else:
            
            i += 4
            
    return numbers
            

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    
    if ordered_numbers_1 == [] and ordered_numbers_2 == []:
        return None
    
    if ordered_numbers_2 == []:
        return ordered_numbers_1
    
    if ordered_numbers_1 == []:
        return ordered_numbers_2

    
    new_list = []
    
    
    i_1 = 0
    i_2 = 0
    
    saved_number = 0

    
    
    while i_1 < len(ordered_numbers_1) and i_2 < len(ordered_numbers_2):
        
        if ordered_numbers_1[i_1] < ordered_numbers_2[i_2]:
            saved_number = ordered_numbers_2[i_2]
            new_list.append(ordered_numbers_1[i_1])
            i_1 += 1

        
        
        else:                                                                                                                                                                                                                                                                                                                                                        
            saved_number = ordered_numbers_1[i_1]
            new_list.append(ordered_numbers_2[i_2])
            i_2 += 1

    
    if i_1 != len(ordered_numbers_1):
        for i in range(i_1, len(ordered_numbers_1)):
            new_list.append(ordered_numbers_1[i])
            
    elif i_2 != len(ordered_numbers_2):
        for i in range(i_2, len(ordered_numbers_2)):
            new_list.append(ordered_numbers_2[i])

    return new_list













print(weird_double([7, 6, 5, 4, 3, 2, 1]))
print(merge_ordered_lists([1, 2, 3, 10], [5, 6, 7]))
print(merge_ordered_lists([1, 2, 3, 10, 20, 30], [6, 7, 8]))
print(merge_ordered_lists([10], [1, 4, 100]))
