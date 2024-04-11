






def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count += 1
        else:
            count += 0
    return count



def average(numbers):
    if len(numbers) >= 2:
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i]
        return sum / len(numbers)
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return 0



def largest_element(numbers):
    if len(numbers) >= 2:
        max = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] > max:
                max = numbers[i]
        return max
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return 0


def all_equal(my_list):
    x = True
    if len(my_list) >= 2:
        counter = 0
        while counter <= len(my_list) and x == True :
            if my_list[counter] == my_list[counter + 1]:
                x = True
            else:
                x = False
            return x
    elif len(my_list) == 1:
        return True
    else:
        return False

def alternate_sum(numbers):
    if len(numbers) == 0:
        return []
    sum = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            sum += numbers[i]
        else:
            sum -= numbers[i]
    return sum


def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return False
    counter = 0
    x = True
    if is_strict == False:
        while x == True and counter <= (len(numbers) - 2):
            if numbers[counter] <= numbers[counter + 1]:
                x = True
            else:
                x = False
            counter += 1
        return x
    else:
        while x == True and counter <= (len(numbers) - 2):
            if numbers[counter] < numbers[counter + 1]:
                x = True
            else:
                x = False
            counter += 1
        return x 


def rotate_right(numbers):
    if len(numbers) == 2:
        return [numbers[1], numbers[0]]
    elif len(numbers) == 1:
        return [numbers[0]]
    elif len(numbers) == 0:
        return "Empty list"
    else:
        new_set = list(range(len(numbers)))
        for i in range(1, len(numbers)):
            new_set[i] = numbers[i - 1]
        new_set[0] = numbers[len(numbers) - 1]
        return new_set


def weird_double(numbers):
    if len(numbers) == 0:
        return "Empty list"
    counter = 0
    while counter < len(numbers):
        if numbers[counter] % 3 == 0:
            counter += 4
        else:
            numbers[counter] *= 2
            counter += 1
    return numbers

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    new_list = []
    counter_1 = 0
    counter_2 = 0
    while counter_1 < (len(ordered_numbers_1)) and (counter_2 < len(ordered_numbers_2)):
        if ordered_numbers_1[counter_1] < ordered_numbers_2[counter_2]:
            new_list.append (ordered_numbers_1[counter_1])
            counter_1 += 1
        else:
            new_list.append(ordered_numbers_2[counter_2])
            counter_2 += 1
    if counter_2 < len(ordered_numbers_2):
        for i in range(counter_2, len(ordered_numbers_2)):
            new_list.append(ordered_numbers_2[i])
    elif counter_1 < len(ordered_numbers_1):
        for i in range(counter_1, len(ordered_numbers_1)):
            new_list.append(ordered_numbers_1[i])
    return new_list

    
        
