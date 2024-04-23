




"""
Creates a new list which is exactly the same with the original
function but moves the index to the end of the list

"""


def item_moved_to_end(my_list, index):

    if 0 < index < len(my_list):
        
        item_moved = my_list[index]
        
        
        final_list = my_list[:index] + my_list[index+1:]
        
        
        final_list.append(item_moved)
        return final_list
    else:
        return "INVALID INDEX" 



"""
makes the index change in the original list, and doesn't change
other things at all
"""        
def move_item_to_end(my_list, index):

    if 0 <= index < len(my_list):
        item_moved = my_list[index]
        
        
        final_list = my_list[:index] + my_list[index+1:]
        
        
        final_list.append(item_moved)
        
        
        my_list[:] = final_list
    else:
        return "INVALID INDEX"

