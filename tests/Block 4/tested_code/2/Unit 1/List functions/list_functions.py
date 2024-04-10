






def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count += 1
    return count  



def average(numbers):
    if len(numbers) == 0:
        return None
    sum_all = 0
    for i in range(len(numbers)):
        sum_all += numbers[i]
    average = sum_all/(len(numbers))
    return average



def largest_element(numbers):
    if len(numbers) < 1:
        return None
    elif len(numbers) < 2:
        return numbers[0]
    else:
        largest = numbers[0]
        for i in range (0,len(numbers)):
            if numbers[i] > largest:
                largest = numbers[i]
    return largest




def all_equal(my_list):
    if len(my_list) == 0:
        return True
    elif len(my_list) > 2:
        for i in range (len(my_list) - 1):
            if my_list[i] != my_list[0]:
                return False
    return True





def alternate_sum(numbers):
    
    alternate_sum = 0
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            alternate_sum = alternate_sum + numbers[i]
        else:
            alternate_sum = alternate_sum - numbers[i]

    return alternate_sum



def is_ordered(numbers, is_strict):
    if is_strict:
        
        for i in range(len(numbers) - 1):  
            if not (numbers[i] < numbers[i + 1]):
                return False

        return True
        
    else:
        for i in range(len(numbers) - 1):  
            if not (numbers[i] <= numbers[i + 1]):
                return False

        return True






def rotate_right(my_list):
    if len(my_list) <= 1:
        return my_list
    last = my_list[-1]
    
    for i in range(len(my_list) - 1, 0, -1):
         my_list[i] = my_list[i - 1]

    my_list[0] = last

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
    index_1 = 0
    index_2 = 0
    new_list = []

    if len(ordered_numbers_1) < 1 and len(ordered_numbers_2) < 1:
        return new_list

    while len(ordered_numbers_1) > index_1 and len(ordered_numbers_2) > index_2:
        if ordered_numbers_1[index_1] < ordered_numbers_2[index_2]:
            new_list.append(ordered_numbers_1[index_1])
            index_1 = index_1 + 1
        else: 
            new_list.append(ordered_numbers_2[index_2])
            index_2 = index_2 + 1
    
    while index_2 < len(ordered_numbers_2):
        new_list.append(ordered_numbers_2[index_2])
        index_2 = index_2 + 1
        
    while index_1 < len(ordered_numbers_1):
        new_list.append(ordered_numbers_1[index_1])
        index_1 = index_1 + 1
    
    return new_list






    
