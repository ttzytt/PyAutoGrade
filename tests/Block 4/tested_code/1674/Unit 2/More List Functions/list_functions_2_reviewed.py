






def largest_element(numbers):
    if numbers == []:
        return None  

    numbers.sort()
    max_element = numbers[-1] 

    return max_element

        


def alternate_sum(numbers):
    result = 0
    result = sum(numbers[::2]) - sum(numbers[1::2])
    return result








def rotate_right(my_list):
   return [my_list[-1]] + my_list[:-1]


def deal_3_hands(cards_list):
    return [cards_list[ : :3]] + [cards_list[1: :3]] + [cards_list[2: :3]]




  
        









  
