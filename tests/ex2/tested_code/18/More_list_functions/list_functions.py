



def rotate_right(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list
    temp = my_list[len(my_list) - 1] 
                                     
    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]   
    my_list[0] = temp
    print(my_list)
    return my_list

def item_moved_to_end(my_list, index):
    new_list = my_list[index:index + 1]
    new_list = my_list[:index] + my_list[index + 1:] + new_list
    return new_list

def move_item_to_end(my_list, index):
    while my_list[index] != my_list[len(my_list) - 1]:



    
    for i in range(len(my_list)):
        rotate_right(my_list)
            



