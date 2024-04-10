










def item_moved_to_end(my_list, index):
    new_list = []
    last_element = my_list[index]
    for i in range(len(my_list)-1): 
        if i >= index:
            new_list.append(my_list[i+1])
        else:
            new_list.append(my_list[i])
    new_list.append(last_element)
    return new_list





def move_item_to_end(my_list, index):
    last_element = my_list[index] 
    for i in range(index,len(my_list)-1):
        my_list[i] = my_list[i + 1] 
    my_list[-1] = last_element
    return


    
