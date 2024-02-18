





my_list = [10,1,2,3,4,5,6,7,8,9]
index = 5
def item_moved_to_end(my_list, index):
    if len(my_list) < index:
        print()
        return 0
    
    list_ = my_list
    list_ = my_list[0:(index-1)] + my_list[(index+1):]
    x = my_list[index]
    print(x)
    list_.append(x)
    print(list_)
    return list_


def move_item_to_end(my_list, index):
    my_list = my_list + my_list[(index):(index+1)]
    my_list.pop(index)
    print(my_list)
    return my_list  
item_moved_to_end(my_list, index)
