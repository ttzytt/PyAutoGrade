






def count_number_larger_than(target, numbers):

    count = 0

    for i in range(0, len(numbers)):
        if numbers[i] > target:
            count += 1

    return count



def average(numbers):

    if len(numbers) == 0:
        return None

    else:
        count = 0
        total = 0

        for i in range(0, len(numbers)):
            count += 1
            total += numbers[i]

        return (total / count)



def largest_element(numbers):

    if len(numbers) == 0:
        return None
    else:
        large = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] > large:
                large = numbers[i]

        return large





def all_equal(my_list):

    if len(my_list) == 0:
        return True

    constant = my_list[0]
    
    for i in range(1, len(my_list)):
        if my_list[i] != constant:
            return False       

    return True



def alternate_sum(numbers):

    if len(numbers) == 0:
        return None

    else:
        total = 0
        even = 0
        odd = 0

        for i in range(0, len(numbers), 2):
            odd += numbers[i]
        for i in range(1, len(numbers), 2):
            even += numbers[i]

        total = even - odd
        return (total)






def is_ordered(numbers, is_strict):

    if len(numbers) == 0:
        return True
    elif len(numbers) == 1:
        return True

    for i in range(1, len(numbers)):
        if is_strict == True:
            if numbers[i] <= numbers[i-1]:
                return False
        else:
            if numbers[i] < numbers[i-1]:
                return False

    return True




def rotate_right(my_list):

    if len(my_list) == 0:
        return('N/A')

    a = my_list[len(my_list) - 1]
    n = len(my_list) - 1
    
    while n > 0 :
        my_list[n] = my_list[n-1]
        n -= 1

    my_list[0] = a

    return (my_list)




def weird_double(numbers):

    i = 0

    while i < len(numbers):
        if numbers[i] % 3 != 0:
            numbers[i] = (2 * numbers[i])
        else:
            i += 3
        i += 1

    return (numbers)



def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):

    index_1 = 0
    index_2 = 0
    index_new = 0

    ordered_numbers_new = []

    while index_1 < len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        if ordered_numbers_1[index_1] < ordered_numbers_2[index_2]:
            ordered_numbers_new.append(ordered_numbers_1[index_1])
            index_1 += 1
        elif ordered_numbers_1[index_1] == ordered_numbers_2[index_2]:
            ordered_numbers_new.append(ordered_numbers_1[index_1])
            ordered_numbers_new.append(ordered_numbers_2[index_2])
            index_1 += 1
            index_2 += 1
        else:
            ordered_numbers_new.append(ordered_numbers_2[index_2])
            index_2 += 1


    if index_1 == len(ordered_numbers_1) and index_2 < len(ordered_numbers_2):
        for index_new in range(index_2, len(ordered_numbers_2)):
            ordered_numbers_new.append(ordered_numbers_2[index_new])
    elif index_1 < len(ordered_numbers_1) and index_2 == len(ordered_numbers_2):
        for index_new in range(index_1, len(ordered_numbers_1)):
            ordered_numbers_new.append(ordered_numbers_1[index_new])

    return (ordered_numbers_new)













 







































    
