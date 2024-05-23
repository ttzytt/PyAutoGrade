





fruit_loop = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7, 'purple' : 4, 'green' : 6}





while True:
    loop_color = (input("Input your fruit loop color ")).lower()
    loop_number = 0
    for color in fruit_loop.keys(): 
        if color in loop_color:
            loop_number += fruit_loop[color]
    
    list_1 = loop_color.split()
    
    
    for i in range (len(list_1)): 
        if list_1[i] == 'floor': 
            
            if list_1[i+1] in fruit_loop.keys(): 
                
                loop_number += 1 
                fruit_loop[list_1[i+1]] += 1
            else:
                fruit_loop[list_1[i+1]] = 1 
                loop_number += 1
    print (loop_number)
    
    if 'break' in loop_color:
        break
