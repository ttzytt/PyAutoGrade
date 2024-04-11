





def item_moved_to_end(my_list, index):
    new_list = []
    new_index = my_list[index]
    for i in range(len(my_list)):
        if i != index:
            new_list.append(my_list[i])                   
    new_list.append(new_index)
    return new_list


def move_item_to_end(my_list, index):
    if len(my_list) != 0:
        stored_index = my_list[index]
        for i in range(index, len(my_list)- 1):
            my_list[i] = my_list[i + 1]

