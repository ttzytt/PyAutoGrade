







def count_number_larger_than(target, numbers):
    count = 0 
    for i in range(len(numbers)): 
        if numbers[i] > target: 
            count += 1 

    return count 


def average(numbers):
    average = 0 
    for i in range(len(numbers)): 
        average += numbers[i]

    if(len(numbers) > 0): 
        
        average /= len(numbers)
        return average 

    return None


def largest_element(numbers):
    if (len(numbers) > 0):
        largest_element = numbers[0]
        for i in range(1, len(numbers)):
            if (numbers[i] > largest_element):
                largest_element = numbers[i]
        return largest_element

    return None




def all_equal(my_list):
    if(len(my_list) > 0): 
        for i in range(len(my_list) - 1):
            if(my_list[i] != my_list[i+1]): 
                return my_list[i] == my_list[i+1] 

        return True 

    return None 



def alternate_sum(numbers):
    if(len(numbers) > 0):
        sum = 0 

        for i in range(len(numbers)):
            if(i % 2 == 0): 
                sum += numbers[i] 
            else:
                sum -= numbers[i] 

        return sum 

    return None





        
