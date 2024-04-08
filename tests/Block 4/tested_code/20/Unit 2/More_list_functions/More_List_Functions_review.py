




 


def item_moved_to_end(my_list, index):

    if 0 < index < len(my_list):
        
        item_moved = my_list[index]
        
        
        final_list = my_list[:index] + my_list[index+1:]
        
        
        final_list.append(item_moved)
        return final_list
    else:
        return "INVALID INDEX" 



        
def move_item_to_end(my_list, index):

    if 0 <= index < len(my_list):
        item_moved = my_list[index]
        
        
        final_list = my_list[:index] + my_list[index+1:]
        
        
        final_list.append(item_moved)
        
        
        my_list[:] = final_list
    else:
        return "INVALID INDEX"

