



def largest_element(numbers):
    numbers.sort()
    return numbers[-1]



def alternate_sum(numbers):
    return(sum(numbers[0:len(numbers)+1:2]) - sum(numbers[1:len(numbers)+1:2]))




def rotate_right(my_list):
    return(my_list[-1:] + my_list[:-1]) 





def deal_3_hands(deck):
    return(deck[0:-1:3], deck[1:-1:3], deck[2:-1:3])




    
    



