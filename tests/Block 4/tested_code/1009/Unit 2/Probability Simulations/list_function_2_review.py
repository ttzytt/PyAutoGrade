



def largest_element(numbers):
    if not numbers:
        return None  

    largest = numbers[0]  

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest

def alternate_sum(input_list):
    even_sum = sum(input_list[::2])
    odd_sum = sum(input_list[1::2])
    return even_sum - odd_sum

   
def rotate_right(my_list):
    
    if not my_list or len(my_list) == 1:
        return my_list  

    
    rotated_list = [my_list[-1]]

    
    rotated_list.extend(my_list[:-1])

    return rotated_list

def deal_3_hands(deck):
    
    hands = [[], [], []]

    
    hand_index = 0

    
    for card in deck:
        
        hands[hand_index].append(card)

        
        hand_index = (hand_index + 1) % 3

    
    return hands


