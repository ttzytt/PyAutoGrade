




"""
Function that takes a list my_list and creates and returns a new list that contains
the same items as my_list in the same order except my_list[index] which has been moved to
the end. Assume that the index is in range. If index is none, return the original list
"""
def item_moved_to_end(my_list, index):
    if index == None:
        return my_list 
    my_new_list = my_list[:index] + my_list[index + 1:]
    my_new_list.append(my_list[index])  
    
    return my_new_list


"""
Function that takes in a list my_list, moves the item at my_list[index] to the end
of the list,keeping the other elements in the same order as before. The function should
modify my_list directly, and should not return a value. Assume that the index is in range
If index is none, return the original list
"""
def move_item_to_end(my_list, index):
    if index == None:
        return my_list

    
    add_to_end = my_list[index]

    
    for i in range(index, len(my_list) - 1): 
        my_list[i] = my_list[i + 1]

    
    my_list[-1] = add_to_end 
    return my_list

  
