



def item_moved_to_end(my_list, index):
    new_list = []
    number = my_list[index]
    for i in range(len(my_list)):
        if i != index:
            new_list.append(my_list[i])
    new_list.append(number)
    return new_list


def move_item_to_end(my_list, index):
    number = my_list[index]
    time = 0
    for i in range(len(my_list)):
        if i == len(my_list)-1:
            my_list[i] = number
            time += 1
        elif i >= index and i < len(my_list) -1:
            my_list[i] = my_list[i+1]
            time += 1
