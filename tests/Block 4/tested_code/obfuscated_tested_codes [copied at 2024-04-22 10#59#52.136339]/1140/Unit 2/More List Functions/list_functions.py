









def item_moved_to_end(my_list, index):
    
    new_list = my_list[:index] + my_list[(index + 1):]
    
    new_list.append(my_list[index])
    
    return new_list





def move_item_to_end(my_list, index):
    
    moved_item = my_list[index]
    
    for i in range(index + 1, len(my_list)):
        my_list[i-1] = my_list[i]
    my_list[-1] = moved_item


    



