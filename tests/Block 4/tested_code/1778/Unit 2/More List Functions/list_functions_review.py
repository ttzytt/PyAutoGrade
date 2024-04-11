







def item_moved_to_end(my_list, index):
    
    
    if len(my_list) == 0:
        return False
    return my_list[ : index] + my_list[index + 1 : ] + [my_list[index]]


def move_item_to_end(my_list, index):
    index_value = my_list[index]
    
    for i in range(index, len(my_list) - 1):
        my_list[i] = my_list[i+1]
    
    
    my_list[len(my_list) - 1] = index_value


