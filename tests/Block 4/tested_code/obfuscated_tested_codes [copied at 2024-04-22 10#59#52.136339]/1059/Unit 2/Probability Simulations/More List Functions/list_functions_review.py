






def item_moved_to_end(my_list, index):
    if len(my_list) < index: 
                                                                    
        print()
        return 0
    
    list_ = my_list
    list_ = my_list[0:(index)] + my_list[(index+1):]
    x = my_list[index]
    list_.append(x)
    return list_




def move_item_to_end(my_list, index):
	x = my_list[index]
	for i in range(index,len(my_list)-2): 
		my_list[i] = my_list[i+1]
	my_list.append(x)
	return my_list
	
