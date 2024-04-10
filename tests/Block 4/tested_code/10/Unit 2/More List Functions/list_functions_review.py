




def item_moved_to_end(my_list, index):
    if index == None:
        return my_list 
    my_new_list = my_list[:index] + my_list[index + 1:]
    my_new_list.append(my_list[index])  
    
    return my_new_list



def move_item_to_end(my_list, index):
    if index == None:
        return my_list

    
    add_to_end = my_list[index]

    
    for i in range(index, len(my_list) - 1): 
        my_list[i] = my_list[i + 1]

    
    my_list[-1] = add_to_end 
    return my_list


  
