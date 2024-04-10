




def item_moved_to_end(my_list, index):
    if len(my_list) < 2:
        return my_list
    
    else:
        
        new_list = []
        
        new_list = my_list[:index] + my_list[(index + 1):]
        
        new_list.append(my_list[index])
        return new_list


def move_item_to_end(my_list, index):
    if len(my_list) < 2:
        return None
    
    else:
        
        moved = my_list[index]
        
        
        
        my_list[index:len(my_list)-1] = my_list[index+1:len(my_list)]
        
        my_list[len(my_list)-1] = moved
