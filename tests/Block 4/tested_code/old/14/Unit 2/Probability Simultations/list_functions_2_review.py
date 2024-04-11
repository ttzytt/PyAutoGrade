








def largest_element(numbers):
    if len(numbers) == 0:
        return None
    numbers.sort()
    return numbers[-1]
    



def alternate_sum(numbers):
    return sum(numbers[::2]) - sum(numbers[1::2])



def rotate_right(my_list):
    if len(my_list) == 0:
        return []
    return [my_list[-1]] + my_list[:-1:]


def deal_3_hands(deck):
    return [deck[0::3],deck[1::3],deck[2::3]]



