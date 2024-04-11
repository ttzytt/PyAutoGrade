

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


    
'''
    # Inputs asking for starting love/hate values and constants
    romeo_input = float(input("What do you want Romeo to start as? "))
    juliet_input = float(input("What do you want Juliet to start as? "))

    starting_value = (romeo_input, juliet_input)
    a = float(input("What would you like a to be? "))
    b = float(input("What would you like b to be? "))

    # List_of_point keeps track of all tuples(starting off with the one that has been inputted)
    list_of_points = [starting_value]

    # Loop generates 50 points
    for i in range(50):

        romeo_new = starting_value[0] - a * starting_value[0] + b * starting_value[1]
        juliet_new = starting_value[1] - a * starting_value[1] + b * starting_value[0]

        starting_value = (romeo_new, juliet_new)
        list_of_points.append(starting_value)

    print(list_of_points)
'''
