







def largest_element(numbers):
    
    if numbers == []:
        return None

    numbers.sort()
    return numbers[-1]




def alternate_sum(numbers):
    result = sum(numbers[::2]) - sum(numbers[1::2])
    return result
    



def rotate_right(my_list):
    
    if my_list == []:
        return my_list

    my_new_list = [my_list[-1]] + my_list[:-1]
    return my_new_list



def deal_3_hands(deck):
    hands = [deck[::3], deck[1::3], deck[2::3]]
    return hands




