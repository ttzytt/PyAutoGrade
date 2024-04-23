








def count_number_larger_than(target, numbers):
    n = int(target)
    x = 0
    for i in numbers:
        if i > n:
            x += 1
    return x
            
        



def average(numbers):
    if len(numbers) == 0:
        return False

    count_number_larger_than = 0
    for i in range(len(numbers)):
        count_number_larger_than = count_number_larger_than + numbers[i]
    return count_number_larger_than/len(numbers)



def largest_element(numbers):
    import math
    if len(numbers) == 0:
        return False
    n = -math.inf
    for i in numbers:
        if i > n:
            n = i
    return n
    



def all_equal(my_list):
    if len(my_list) == 0:
        return False
    for i in range(len(my_list)):
        n = my_list[0]
        while i < len(my_list): 
            if my_list[i] == n:
                i += 1
            else:
                return False
        return True
