






def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count = count + 1         
    return count  
                  



def average(numbers):
    if len(numbers) == 0:
        return None
    
    total = 0
    for i in range(len(numbers)):
        total = numbers[i] + total
    return (total / len(numbers))



def largest_element(numbers):
    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest  




def all_equal(my_list):
    if len(my_list) == 0:
        return None
    for i in range(len(my_list) - 1):
        if my_list[i] != my_list[i + 1]:
           return False
    return True
