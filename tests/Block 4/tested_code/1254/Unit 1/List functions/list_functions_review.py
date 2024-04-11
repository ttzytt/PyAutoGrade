





def count_number_larger_than(target, numbers):
    i = 0
    count_larger_than = 0
    for i in range (len(numbers)):
        if numbers[i] > target:
            count_larger_than += 1
    return count_larger_than




def average(numbers):
    if len(numbers) < 1:
        return None
    i = 0
    sum_of_all = 0
    for i in range (len(numbers)): 
        sum_of_all += numbers[i]
    average = sum_of_all/(len(numbers))
    return average



def largest_element(numbers):
    if len(numbers) < 1:
        return None
    elif len(numbers) < 2:
        return numbers[0]
    else:
        i = 0
        if numbers[0] < numbers[1]:
                                    
            largest_num = numbers[1]
        elif numbers[0] > numbers[1]:
            largest_num = numbers[0]
        for i in range (2,len(numbers)):
            if numbers[i] > largest_num:
                largest_num = numbers[i]
        
    return largest_num  




def all_equal(my_list):
    if len(my_list) < 1:
        return False
    elif len(my_list) < 2:
        return True
    i = 0
    for i in range (len(my_list) - 1):
        if my_list[i] is my_list[i+1]:
            equal_or_not = 'yes'
        else:
            equal_or_not = 'no'

    if equal_or_not == 'yes':
        return True
    else:
        return False

