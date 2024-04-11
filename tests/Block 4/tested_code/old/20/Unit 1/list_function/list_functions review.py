







def count_number_larger_than(target, numbers):
    count = 0
    for number in numbers:
        if number > target:
            count += 1
    return count



def average(numbers):
    if not numbers:
        return 0  
    
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    return total / count


def largest_element(numbers):
    if not numbers:
        return None  

    largest = numbers[0]  

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest



def all_equal(my_list):
    
    if not my_list:
        return True
    
    
    first_element = my_list[0]
    return all(element == first_element for element in my_list)





def alternate_sum(numbers):
    return sum(numbers[::2]) - sum(numbers[1::2])

def is_ordered(numbers, is_strict):
    
    if not numbers or len(numbers) == 1:
        return True  

    
    for i in range(1, len(numbers)):
        if is_strict and numbers[i] <= numbers[i - 1]:
            return False  
        elif not is_strict and numbers[i] < numbers[i - 1]:
            return False  

    return True

def rotate_right(my_list):
    
    if not my_list or len(my_list) == 1:
        return my_list  

    
    rotated_list = [my_list[-1]]

    
    rotated_list.extend(my_list[:-1])

    return rotated_list

def weird_double(numbers):
    index = 0  

    
    while index < len(numbers):
        
        if numbers[index] % 3 == 0:
            
            count_to_skip = 3 if len(numbers) - index >= 3 else len(numbers) - index
            
            index += count_to_skip
        else:
            
            numbers[index] *= 2
            index += 1  

    return numbers

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    index_1 = 0
    index_2 = 0
    result = []

    while index_1 < len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        if ordered_numbers_1[index_1] < ordered_numbers_2[index_2]:
            result += [ordered_numbers_1[index_1]]
            index_1 += 1
        else:
            result += [ordered_numbers_2[index_2]]
            index_2 += 1

    
    while index_1 < len(ordered_numbers_1):
        result += [ordered_numbers_1[index_1]]
        index_1 += 1

    while index_2 < len(ordered_numbers_2):
        result += [ordered_numbers_2[index_2]]
        index_2 += 1

    return result


    
