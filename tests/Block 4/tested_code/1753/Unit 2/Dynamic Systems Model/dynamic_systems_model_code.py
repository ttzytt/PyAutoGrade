







def rotate_and_expand(point):
    rabbits = point[0]
    foxes = point[1]
    new_rabbits = rabbits + 0.01 * rabbits - 0.01 * rabbits * foxes
    new_foxes = foxes - 0.02 * foxes + 0.01 * rabbits * foxes
    return (new_rabbits, new_foxes)

starting_point = (2.01, 1.01)
coordinates = []
coordinates.append(starting_point)
point = starting_point
for i in range(1000):
    rotate_and_expand(point)
    if i % 10 == 0:
        coordinates.append(rotate_and_expand(point))
    point = rotate_and_expand(point)
for i in range(len(coordinates)):
    round(coordinates[i][0], 3)
    round(coordinates[i][1], 3)


print(coordinates)
print()



