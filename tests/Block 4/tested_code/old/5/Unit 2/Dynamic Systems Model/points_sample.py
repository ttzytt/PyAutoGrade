







def rotate_and_expand(point):
    x = point[0]
    y = point[1]
    new_x = 1.1 * y
    new_y = -1.1 * x
    return (new_x, new_y)

def list_of_points():
    point = (0.3, 0.1)
    list_of_points = []
    count = 0
    list_of_points.append(point)
    while count < 50:
        point = rotate_and_expand(point)
        list_of_points.append(point)
        count += 1
    return list_of_points
        






