





def item_moved_to_end(my_list, index):  
    new_list = []
    if len(my_list) == 0:
        return False
    new_list = []
    for i in range(len(my_list)):
        if i != index:
            new_list.append(my_list[i])
        i += 1

    new_list.append(my_list[index])
    
    return new_list
    


def move_item_to_end(my_list, index):
    if len(my_list) == 0:
        return False
    
    my_index = my_list[index]
    
    for i in range(index, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list[len(my_list) - 1] = my_index


