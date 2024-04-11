







def item_moved_to_end(my_list, index):
    new_list = []
    if len(my_list) == 0:
        return my_list
    
    return (my_list[:index] + my_list[index + 1:] + [my_list[index]])



def move_item_to_end(my_list, index):
    if len(my_list) == 0:
        my_list
    
    my_index = my_list[index]
    
    for i in range(index, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list[len(my_list) - 1] = my_index

