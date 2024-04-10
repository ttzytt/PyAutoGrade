






def largest_element(numbers):
    if not numbers: 
        return None
    
    return max(numbers) 




def alternate_sum(numbers):
    return sum(numbers[::2]) - sum(numbers[1::2])








def rotate_right(my_list):
    return my_list[-1:] + my_list[:-1]



def deal_3_hands(deck):
    return [deck[i::3] for i in range(3)]
