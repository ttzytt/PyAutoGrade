



def item_moved_to_end(my_list, index):
    list_2 = my_list[:index:1]
    list_1 = my_list[index + 1:len(my_list)]
    list3 = list_2 + list_1
    list3.append(my_list[index])
    return list3




def moved_to_end(my_list, index):
    list_2 = my_list[:index:1]
    list_1 = my_list[index + 1:len(my_list)]
    end_guy = my_list[index]
    my_list = list_2 + list_1
    my_list.append(end_guy)
    print(my_list)

