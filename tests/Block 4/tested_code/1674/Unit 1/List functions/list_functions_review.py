






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

    for num in numbers:
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







  
