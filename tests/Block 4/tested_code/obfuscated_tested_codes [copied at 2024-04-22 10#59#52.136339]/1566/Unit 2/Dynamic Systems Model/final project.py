



'''

'''
       

def fox_rabbit(point):
    rabbits = point[0]
    foxes = point[1]
    
    if rabbits <= 0 and foxes <= 0:
        return (0, 0)
    else:   
    
        
        new_rabbits = round(rabbits + 0.01 * rabbits  - 0.01 * rabbits * foxes, 4)
        new_foxes = round(foxes - 0.02 * foxes + 0.01 * rabbits * foxes, 4)
    
        
        if new_rabbits > 0 and new_foxes > 0:
            return (new_rabbits, new_foxes)
        else:
            return (0, 0)

def list_of_points():
    
    
    point = (16,1)
    list_of_points = []
    count = 0
    list_of_points.append(point)
    while count < 1000:
        point = fox_rabbit(point)
        list_of_points.append(point)
        count += 1
    return list_of_points



print(list_of_points())


