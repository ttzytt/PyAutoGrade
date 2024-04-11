


import math



romeo_start = int(input('how much love do you want Romeo have for Juliet at the start?'))
juliet_start = int(input('how much love do you want Juliet have for Romeo at the start?'))  
a = int(input('how much more or less do you want Romeo to love Juliet every day?'))*0.1
b = int(input('how much more or less do you want Juliet to love Romeo every day?'))*0.1
time = int(input('how far back do you wanna see the prediction?(after x days)'))
list_love = []
point = (romeo_start, juliet_start)
e = 2.718281828459045
'''
def love_predict(days):
    romeo_new = romeo_start*e**((1-a+b)*days) - juliet_start*e**((1-a-b)*days)
    juliet_new = romeo_start*e**((1-a+b)*days) + juliet_start*e**((1-a-b)*days)
    return (romeo_new, juliet_new)
    

#for i in range(time):
   # list_love.append(love_predict(i))




print(list_love)
'''


def love_and_love(point):
    Romeo = point[0]
    Juliet = point[1]
    Romeo_new = Romeo - a*Romeo + b*Juliet
    Juliet_new = Juliet - a*Juliet + b*Romeo


    return (Romeo_new, Juliet_new)



list_love.append((romeo_start,juliet_start))
for i in range(time):
    '''
    if 'e' in str(love_and_love(point)[0]):
        exponent = str(love_and_love(point)[0]).split('e')[1]
        number = str(love_and_love(point)[0]).split('e')[0]
        formatted_Romeo = str(number) + ('*10^(')+ exponent + ')'
    else:
        formatted_Romeo = love_and_love(point)[0]
     
    if 'e' in str(love_and_love(point)[1]):
        exponent = str(love_and_love(point)[1]).split('e')[1]
        number = str(love_and_love(point)[1]).split('e')[0]
        formatted_Juliet = str(number) + ('*10^(')+ exponent + ')'
    else:
        formatted_Juliet = love_and_love(point)[1]
    formatted_love = (formatted_Romeo, formatted_Juliet)
    list_love.append(formatted_love)
    '''
    list_love.append(love_and_love(point))
    point = love_and_love(point)
    
print(list_love)

