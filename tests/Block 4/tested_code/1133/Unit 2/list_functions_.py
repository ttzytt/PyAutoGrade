



def item_moved_to_end(my_list, index):
    """
   
    It does not modify the original list but returns a new list with the element moved.

    """
    my_new_list = my_list[:index] + my_list[index + 1:] + [my_list[index]]
    return my_new_list


def move_item_to_end(my_list, index):
    """ 
    It uses an in-place algorithm to shift the elements of the list, thereby not creating a new list.
    
  
    """
    item = my_list[index] 
    for i in range(index, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list[-1] = item  
