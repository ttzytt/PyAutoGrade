


def item_moved_to_end(my_list,index):
    
    if len(my_list) == 0 or len(my_list) == 1 or index ==                                        len(my_list)-1:
        return my_list
    
    return my_list[0:index]+my_list[index+1:]+ [my_list[index]]




def move_item_to_end(my_list,index):
    temp = my_list[index]
    for i in range(index,len(my_list)-1):
        my_list[i] = my_list[i+1]
    my_list[-1] = temp
    
