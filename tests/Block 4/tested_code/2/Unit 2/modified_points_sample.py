







def rotate_and_expand(point):
    x = point[0]
    y = point[1]
    new_x = 1.1 * y
    new_y = -1.1 * x
    return (new_x, new_y)


current_point = (0.3, 0.1)
list_of_points = [(0.3, 0.1)]
def generate_points(current_point, list_of_points):
    for _ in range(50):
        list_of_points.append(rotate_and_expand(current_point))
        current_point = rotate_and_expand(current_point)
    return list_of_points


