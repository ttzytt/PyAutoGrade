


import math



romeo_start = int(input('how much love do you want Romeo have for Juliet at the start?'))
juliet_start = int(input('how much love do you want Juliet have for Romeo at the start?'))  


time = int(input('how far back do you wanna see the prediction?(after x days)'))
list_love = []
point = (romeo_start, juliet_start)
e = 2.718281828459045



def love_and_love(point):
    Romeo = point[0]
    Juliet = point[1]
    Romeo_new = Romeo - 0*Romeo + 0.4*Juliet
    Juliet_new = Juliet - 0*Juliet - 0.2*Romeo


    return (Romeo_new, Juliet_new)



list_love.append((romeo_start,juliet_start))
for i in range(time):
    
    list_love.append(love_and_love(point))
    point = love_and_love(point)
    
print(list_love)

