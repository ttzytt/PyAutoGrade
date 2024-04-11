






def largest_element(numbers):
    if (len(numbers) > 0):
        numbers.sort()
        return numbers[-1]

    return None




def alternate_sum(numbers):
    if(len(numbers) > 0):
        return sum(numbers[::2]) - sum(numbers[1::2])
    return None





def rotate_right(my_list):
    if (len(my_list) > 0):
        return [my_list[-1]] + my_list[:-1]
    return my_list




def deal_3_hands(deck):
    return [deck[::3], deck[1::3], deck[2::3]]
