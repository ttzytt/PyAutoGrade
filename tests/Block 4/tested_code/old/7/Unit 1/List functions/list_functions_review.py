






def count_number_larger_than(target, numbers):
    number_larger = 0
    for i in range(0, len(numbers)):
        if numbers[i] > target:
            number_larger += 1
    return number_larger




def average(numbers):
    total_sum = 0
    if len(numbers) == 0:
        return None
    elif len(numbers) > 0:
        for i in range(0,len(numbers)):
            total_sum += numbers[i]
    return total_sum/len(numbers)



def largest_element(numbers):
    largest = numbers[0]
    if len(numbers) == 0:
        return None
    else:
        for i in range(0, len(numbers)):
            if largest < numbers[i]:
                largest = numbers[i]
    return largest



def all_equal(my_list):
    if len(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] is not my_list[0]:
                return False
    return True
    
