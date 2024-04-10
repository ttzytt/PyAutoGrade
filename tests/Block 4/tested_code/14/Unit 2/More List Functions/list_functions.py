






def item_moved_to_end_wrong(my_list, index):

    new_list = my_list
    
    item_be_moved = my_list[index]

    for i in range(index, len(my_list) - 1):
        new_list[i] = my_list[i + 1]

    new_list[-1] = item_be_moved
    
    return new_list





def item_moved_to_end(my_list, index):

    
    if len(my_list) == 0 or index > (len(my_list) - 1):
        return None

    return my_list[:index] + my_list[index + 1: len(my_list)] + [my_list[index]]




def move_item_to_end(my_list, index):

    
    if len(my_list) == 0 or index > (len(my_list) - 1):
        return None

    item_be_moved = my_list[index]

    
    for i in range(index, len(my_list) - 1):
        my_list[i] = my_list[i + 1]

    
    my_list[-1] = item_be_moved
