point = (0.3, 0.1)
def rotate_and_expand(point):
    x = point[0]
    y = point[1]
    new_x = 1.1 * y
    new_y = -1.1 * x
    point = (new_x, new_y)
    return point
    
list_of_points = []
for i in range(50):
	point = rotate_and_expand(point)
	list_of_points.append(point)
print (list_of_points)
