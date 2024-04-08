

def romeo_and_juliet(point, a, b):
    romeo = point[0]
    juliet = point[1]
    
    romeo_new = romeo - a * romeo + b * juliet
    juliet_new = juliet - a * juliet + b * romeo
    
    return (romeo_new,juliet_new)
a = float(input("What would you like a to be? "))
b = float(input("What would you like b to be? "))

while True:
    romeo_starting = float(input("How would you like romeo to start? "))
    juliet_starting = float(input("How would you like juliet to start? "))
    list_of_points = [(romeo_starting, juliet_starting)]
    for i in range(50):
        list_of_points.append(romeo_and_juliet(list_of_points[-1], a, b))

    for i in range(len(list_of_points)):
        point_to_be_changed = list_of_points[i]
        list_of_points[i] = (round(point_to_be_changed[0], 4), round(point_to_be_changed[1], 4))

    print(list_of_points)


    

