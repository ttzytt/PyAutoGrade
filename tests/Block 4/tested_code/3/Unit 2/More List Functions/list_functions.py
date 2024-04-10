





def item_moved_to_end(my_list, index):

    
    new_list = my_list[:index] + my_list[(index + 1):] + [my_list[index]]

    return new_list


def move_item_to_end(my_list, index):

    
    chosen_number = my_list[index]

    for i in range(len(my_list) - index - 1):

        my_list[index + i] = my_list[index + i + 1]

    my_list[-1] = chosen_number

    
