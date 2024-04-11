







def count_number_larger_than(target, numbers):
    counter = 0
    return_value = 0
    while counter < len(numbers):
        if numbers[counter] > target:
            return_value = return_value + 1
        counter = counter + 1
    return return_value  




def average(numbers):
    if len(numbers) == 0:
        return 0

    counter = 0
    return_value = 0
    while counter < len(numbers):
        return_value = numbers[counter] + return_value
        counter = counter + 1
    return return_value / len(numbers)



def largest_element(numbers):
    counter = 0
    return_value = 0
    maximum = -99999
    if len(numbers) == 0:
        return 0
    
    while counter < len(numbers):
        maximum = max(maximum,numbers[counter])
        counter = counter + 1

    return maximum




def all_equal(my_list):
    counter = 0
    return_value = 0
    if len(my_list) == 0:
        return True
    
    firstvalue = my_list[0]
    while counter < len(my_list):
        if firstvalue != my_list[counter]:
            return False
        counter = counter + 1
    return True




def alternate_sum(numbers):
    return_value = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            return_value += numbers[i]
        else:
            return_value -= numbers[i]
    return return_value


def is_ordered(numbers,is_strict):
    if len(numbers) == 0:
        return False
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1] and is_strict == False:
            return False
        elif numbers[i] <= numbers[i - 1] and is_strict == True:
            return False
    return True



def rotate_right(my_list):
    temp_list = my_list.copy()
    
    
    
    
    if len(temp_list) == 0:
        return 0
    for i in range(1,len(my_list)):
        my_list[i] = temp_list[i-1]
    my_list[0] = temp_list[len(temp_list) - 1]
    return my_list


def weird_double(numbers):
    if len(numbers) == 0:
        return 0
    counter = 0
    while counter <= len(numbers) - 1:
        if numbers[counter] % 3 != 0:
            numbers[counter] *= 2
            counter += 1
        else:
            counter += 4
    return numbers


def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    if len(ordered_numbers_1) == 0 or len(ordered_numbers_2) == 0:
        return 0

    index_1 = 0
    index_2 = 0
    new_list = []

    while index_1 < len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        if ordered_numbers_1[index_1] <= ordered_numbers_2[index_2]:
            new_list.append(ordered_numbers_1[index_1])
            index_1 += 1
        else:
            new_list.append(ordered_numbers_2[index_2])
            index_2 += 1

    if len(ordered_numbers_1) == index_1:
        while index_2 < len(ordered_numbers_2):
            new_list.append(ordered_numbers_2[index_2])
            index_2 = index_2 + 1
    else:
        while index_1 < len(ordered_numbers_1):
            new_list.append(ordered_numbers_1[index_1])
            index_1 = index_1 + 1
    return new_list

