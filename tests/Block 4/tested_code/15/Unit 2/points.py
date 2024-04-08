







def rotate_and_expand(point):
    x = point[0]
    y = point[1]
    new_x = 1.1 * y
    new_y = -1.1 * x
    return (new_x, new_y)
initial_point = (0.3, 0.1)
list_of_points = [(0.3, 0.1)]

initial_point = rotate_and_expand(initial_point)
initial_point.append(current_point)



