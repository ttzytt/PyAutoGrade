



def item_moved_to_end(my_list, index):

    i = 0
    my_new_list = []
    

    while i < len(my_list):

        if i != index:
            my_new_list.append(my_list[i])

        i += 1


    my_new_list.append(my_list[index])

    return my_new_list



def move_item_to_end(my_list, index):

    i = index
    x = my_list[index]

    while i >= index and i < (len(my_list) - 1):
        my_list[i] = my_list[i+1]
        i += 1

    my_list[-1] = x
