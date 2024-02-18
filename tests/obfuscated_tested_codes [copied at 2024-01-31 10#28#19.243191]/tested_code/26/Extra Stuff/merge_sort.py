def merge(ordered_numbers_1, ordered_numbers_2):
    merged_list = []
    if ordered_numbers_1 == [] and ordered_numbers_2 == []: 
        return merged_list
    elif ordered_numbers_1 == []: 
        return ordered_numbers_2
    elif ordered_numbers_2 == []: 
        return ordered_numbers_1
    
    
    
    comparison_index_1 = 0
    comparison_index_2 = 0
    while comparison_index_1 < len(ordered_numbers_1) and \
          comparison_index_2 < len(ordered_numbers_2): 
                                                       
                                                       
        if ordered_numbers_1[comparison_index_1] < \
           ordered_numbers_2[comparison_index_2]:
            merged_list.append(ordered_numbers_1[comparison_index_1])
            comparison_index_1 += 1
        else: 
            merged_list.append(ordered_numbers_2[comparison_index_2])
            comparison_index_2 += 1

    
    if comparison_index_1 < len(ordered_numbers_1):
        
        for i in range(comparison_index_1, len(ordered_numbers_1)):
            merged_list.append(ordered_numbers_1[i])
    elif comparison_index_2 <= len(ordered_numbers_2):
        
        for i in range(comparison_index_2, len(ordered_numbers_2)):
            merged_list.append(ordered_numbers_2[i])
            
    return merged_list

def merge_sort(input_list):
    
