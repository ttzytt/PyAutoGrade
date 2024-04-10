




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
            sum += ((-1) ** i) * numbers[i] 

        return sum 

    return None






def is_ordered(numbers, is_strict):
    if(is_strict): 
        for i in range(len(numbers)-1):
            if(numbers[i] >= numbers[i + 1]): 

                return numbers[i] < numbers[i + 1]

    else: 
        for i in range(len(numbers)-1):
            if(numbers[i] > numbers[i + 1]):  

                return numbers[i] <= numbers[i + 1]

    return True 





def rotate_right(my_list):

    new_list = []
    if(len(my_list) != 0):
        
        new_list = [my_list[len(my_list) - 1]]
        for i in range(len(my_list) - 1):
            new_list.append(my_list[i]) 
    return new_list 





def weird_double(numbers):
    weird_double = []
    i = 0 
    while(i < len(numbers)):
        if(numbers[i] % 3 == 0):
            j = 0 
            while((j < 4) and (i < len(numbers))):
                weird_double.append(numbers[i])
                i += 1
                j += 1
        else:
            weird_double.append(numbers[i] * 2)
            i+= 1

    return weird_double
        




def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    index_1 = 0
    index_2 = 0
    lists_merged = []

    while((index_1 < len(ordered_numbers_1)) and
          (index_2 < len(ordered_numbers_2))): 
        
        if(ordered_numbers_1[index_1] < ordered_numbers_2[index_2]): 
            lists_merged.append(ordered_numbers_1[index_1])
            index_1 += 1
        else:
            lists_merged.append(ordered_numbers_2[index_2])
            index_2 += 1
    
    if(index_2 < len(ordered_numbers_2)):
        while(index_2 < len(ordered_numbers_2)):
            lists_merged.append(ordered_numbers_2[index_2])
            index_2 += 1
    
    elif(index_1 < len(ordered_numbers_1)):
        while(index_1 < len(ordered_numbers_1)):
            lists_merged.append(ordered_numbers_1[index_1])
            index_1 += 1


    return lists_merged






        
