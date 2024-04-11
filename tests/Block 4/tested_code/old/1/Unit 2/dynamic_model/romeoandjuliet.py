


import math



romeo_start = int(input('how much love do you want Romeo have for Juliet at the start?'))
juliet_start = int(input('how much love do you want Juliet have for Romeo at the start?'))  
a = int(input('how much more or less do you want Romeo to love Juliet every day?'))*0.1
b = int(input('how much more or less do you want Juliet to love Romeo every day?'))*0.1
time = int(input('how far back do you wanna see the prediction?(after x days)'))
list_love = []
point = (romeo_start, juliet_start)
e = 2.718281828459045



def love_and_love(point):
    Romeo = point[0]
    Juliet = point[1]
    Romeo_new = Romeo - a*Romeo + b*Juliet
    Juliet_new = Juliet - a*Juliet + b*Romeo


    return (Romeo_new, Juliet_new)



list_love.append((romeo_start,juliet_start))
for i in range(time):
    
    list_love.append(love_and_love(point))
    point = love_and_love(point)
    
print(list_love)

