








def count_number_larger_than(target, numbers):
    current_position = 0
    total = 0
    while current_position < len(numbers):
        if numbers[current_position] > target:
            total += 1
            current_position += 1
        else:
            current_position += 1
    return total  



def average(numbers):
    
    if len(numbers) == 0:
        return None

    
    current_position = 0
    add = 0
    while current_position < len(numbers):
        add += numbers[current_position]
        current_position += 1
    return (add/len(numbers))





def largest_element(numbers):
    current_position = 0
    count_1 = 0
    
    
       
                            
    
    
    if len(numbers) == 0:
        return None
    
    else:
        max_1 = numbers[0]
        min_1 = numbers[0]
        while current_position < len(numbers):
            if numbers[current_position] > max_1:
                max_1 = numbers[current_position]
                current_position = current_position + 1
            else:
                current_position += 1
        return max_1
    
    



def all_equal(my_list):
    


    if len(my_list) == 0:
        return None
    current_position = 0
    current_index = my_list[0]




    while current_position < len(my_list):
        if current_index == my_list[current_position]:
         current_position += 1
        else:
            return False
    return True






def alternate_sum(numbers):


    current_position = 0
    alternate_sum = 0 
    if len(numbers) == 0: 
        return None
    else:
        for current_position in range(len(numbers)):
            if current_position % 2 == 0:
                alternate_sum += numbers[current_position]
            elif current_position % 2 == 1:
                alternate_sum -= numbers[current_position]
        return alternate_sum








def is_ordered(numbers, is_strict):

    if len(numbers) == 0:
        return None
    current_position = 1
    
    
    small = numbers[0]
    if is_strict:
        while current_position < len(numbers):
            if small < numbers[current_position]:
                return_value = 1 
                small = numbers[current_position]
                current_position += 1
            else:
                return False
    else:
        while current_position < len(numbers):
            if small <= numbers[current_position]:
                return_value = 1
                small = numbers[current_position]
                current_position += 1
            else:
                return False
    if return_value == 1:
        return True





def rotate_right(my_list):
    
    if len(my_list) == 0:
        return []
    
    
    numbers = []
    numbers.append(my_list[len(my_list)-1])
    current_position = 0


    while current_position < len(my_list)-1:
        numbers.append(my_list[current_position]) 
        current_position += 1
    return numbers






def weird_double(numbers):


    if len(numbers) == 0:
        return []
    current_position = 0
    a = 0
    b = 0
    nums = []
    while current_position < len(numbers):
        if numbers[current_position] %3 == 0:
            current_position += 4
        else:
            numbers[current_position] = numbers[current_position]*2
            current_position += 1
    return numbers





def merge_ordered_lists(ordered_number_1,ordered_number_2):


    current_position_1 = 0
    current_position_2 = 0
    list_merged = []
    while current_position_1 < len(ordered_number_1):
        if current_position_2 >= len(ordered_number_2):
            break

        if (ordered_number_1[current_position_1] > ordered_number_2[current_position_2]):
            list_merged.append(ordered_number_2[current_position_2])
            current_position_2 += 1
        elif (ordered_number_1[current_position_1] < ordered_number_2[current_position_2]):
            list_merged.append(ordered_number_1[current_position_1])
            current_position_1 += 1
        elif (ordered_number_1[current_position_1] == ordered_number_2[current_position_2]):
            list_merged.append(ordered_number_1[current_position_1])
            list_merged.append(ordered_number_2[current_position_2])

            current_position_1 += 1
            current_position_2 += 2

            
    
    
    if current_position_2 < len(ordered_number_2):
        while current_position_2<len(ordered_number_2):
            list_merged.append(ordered_number_2[current_position_2])
            current_position_2 += 1
    if current_position_1 < len(ordered_number_1):
        while current_position_1<len(ordered_number_1):
            list_merged.append(ordered_number_1[current_position_1])
            current_position_1 += 1
    return list_merged



        
    


