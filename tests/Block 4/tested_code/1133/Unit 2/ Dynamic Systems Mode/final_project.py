

def rotate_and_expand_1(point):
    rabbits = point[0]
    sheep = point[1]
    new_rabbits = max(0, rabbits + 0.1 * (3 - rabbits) * rabbits)
    new_sheep = max(0, sheep + 0.1 * (2 - sheep) * sheep)
    return (new_rabbits, new_sheep)

def rotate_and_expand_2(point):
    rabbits = point[0]
    sheep = point[1]
    new_rabbits = max(0, rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep)
    new_sheep = max(0, sheep + 0.1 * (2 - sheep) * sheep - 0.1 * rabbits * sheep)
    return (new_rabbits, new_sheep)

def rotate_and_expand_3(point):
    rabbits = point[0]
    sheep = point[1]
    new_rabbits = max(0, rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep)
    new_sheep = max(0, sheep + 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep)
    return (new_rabbits, new_sheep)


'''
list_of_points_1 = [(2, 1)] # Include initial point

point = (2, 1)
for _ in range(50):  
    point = rotate_and_expand_1(point)
    list_of_points_1.append(point)

print(list_of_points_1)
'''

list_of_points_2 = [(2, 1)] 

point = (2, 1)
for _ in range(50):  
    point = rotate_and_expand_2(point)
    list_of_points_2.append(point)

print(list_of_points_2)

list_of_points_3 = [(2, 1)] 

point = (2, 1)
for _ in range(50):  
    point = rotate_and_expand_3(point)
    list_of_points_3.append(point)

print(list_of_points_3)


