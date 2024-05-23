





fruit_loop = {'red' : 6,
           'blue' : 5,
           'yellow' : 7,
           'orange' : 7,
           'purple' : 4,
           'green' : 6,
          }


loop_color = (input("Input your fruit loop color ")).lower()
loop_number = 0 
for color in fruit_loop.keys(): 
    if color in loop_color: 
        loop_number += fruit_loop[color] 
print (loop_number)
