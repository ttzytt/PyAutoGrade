


def new_rabbits_and_sheep(rabbits, sheep):
    new_rabbits = rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep
    new_sheep = sheep + 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep
    if new_rabbits < 0:
        new_rabbits = 0
    if new_sheep < 0:
        new_sheep = 0
    return (new_rabbits, new_sheep)

rabbits = 5
sheep = 3
list_of_points = [(rabbits, sheep)]

for i in range(100):
    list_of_points.append(new_rabbits_and_sheep(rabbits, sheep))
    rabbits = list_of_points[i+1][0]
    sheep = list_of_points[i+1][1]

print(list_of_points[99])

