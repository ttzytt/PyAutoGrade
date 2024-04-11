





def item_moved_to_end(my_list, index):
    
    if len(my_list) < 2:
        return my_list
    else:
        
        front_of_list = my_list[:index]
        back_of_list = []
        
        
        for i in range(index + 1, len(my_list)):
            back_of_list.append(my_list[i])
    
        new_list = front_of_list + back_of_list + [my_list[index]]
        return new_list
    

def move_item_to_end(my_list, index):
    if len(my_list) < 2:
        my_list = my_list
    else:
    
        if index >= 0 and index < len(my_list):
            
            temp_store = my_list[index]
            
            my_list[index:len(my_list)-1] = my_list[index + 1:len(my_list)]
            
            my_list[len(my_list)-1] = temp_store

                 
