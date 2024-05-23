





fruit_loop = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7, 'purple' : 4, 'green' : 6}



loop_color = (input("Input your fruit loop color ")).lower()

while 'break' not in loop_color:
    
    loop_number = 0
    for color in fruit_loop.keys(): 
        if color in loop_color:
            loop_number += fruit_loop[color]
    selected_colors = loop_color.split()
    for i in range (len(selected_colors)): 
        if selected_colors[i] == 'floor': 
            
            if selected_colors[i+1] in fruit_loop.keys(): 
                
                loop_number += 1 
                fruit_loop[selected_colors[i+1]] += 1
            else:
                fruit_loop[selected_colors[i+1]] = 1 
                loop_number += 1
    print (loop_number)
    loop_color = (input("Input your fruit loop color ")).lower()
