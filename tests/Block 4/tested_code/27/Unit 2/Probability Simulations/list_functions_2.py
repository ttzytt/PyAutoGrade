





def largest_element(numbers):
    
    numbers.sort()
    return numbers[-1]

def alternate_sum(numbers):
    
    return sum(numbers[0::2])-sum(numbers[1::2])

def rotate_right(numbers):
    last_value = [numbers[-1]] 
    return last_value + numbers[:-1] 

def deal_3_hands(deck):
    
    return [deck[::3],deck[1::3],deck[2::3]]
