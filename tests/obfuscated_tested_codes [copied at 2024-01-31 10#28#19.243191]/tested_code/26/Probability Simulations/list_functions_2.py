





def largest_element(input_list):
    if len(input_list) == 0:
        return "Empty list"
    
    input_list.sort()
    return input_list[-1]






def alternate_sum(input_list):
    return sum(input_list[::2]) - sum(input_list[1::2])






def rotate_right(input_list):
    if len(input_list) == 0:
        return []
    
    return [input_list[-1]] + input_list[:-1]






def deal_3_hands(deck):
    return [deck[::3], deck[1::3], deck[2::3]]
    
