





def item_moved_to_end(my_list, index):
    changed_my_list = my_list[:index] + my_list[index + 1:] + my_list[index:index + 1]
    return changed_my_list



def move_item_to_end(my_list, index):
    if len(my_list) != 0:
        stored_index = my_list[index]
        for i in range(index, len(my_list) - 1):
            my_list[i] = my_list[i + 1]
        my_list[-1] = stored_index
