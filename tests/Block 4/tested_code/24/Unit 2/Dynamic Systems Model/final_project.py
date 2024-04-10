




def get_next_point(point, a, b):
    Romeo = point[0]
    Juliet = point[1]
    
    Romeo_new = Romeo + a * Romeo + b * Juliet
    Juliet_new = Juliet + a * Juliet + b * Romeo
    
    return (Romeo_new, Juliet_new)


def list_of_points(point):
    list_of_points = []
    count = 50 
    list_of_points.append(point)
    
    for _ in range(count):
        point = get_next_point(point, a, b)
        list_of_points.append(point)
    return list_of_points




initial_point = (1, -2)
a = 0.3
b = 0.3
print(list_of_points(initial_point))
