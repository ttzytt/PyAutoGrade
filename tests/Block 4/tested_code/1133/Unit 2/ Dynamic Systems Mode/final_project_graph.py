
import numpy as np
import matplotlib.pyplot as plt

def rotate_and_expand_3(point):
    rabbits = point[0]
    sheep = point[1]
    new_rabbits = max(0, rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep)
    new_sheep = max(0, sheep + 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep)
    return (new_rabbits, new_sheep) 

list_of_points_3 = [(2, 3)] 

point = (2, 3)
for i in range(100000):  
    point = rotate_and_expand_3(point)
    list_of_points_3.append(point)


def generate_and_plot(starting_points, iterations=10000):
    plt.figure(figsize=(10, 10))

    for start_point in starting_points:
        points = [start_point]
        point = start_point
        for _ in range(iterations):
            point = rotate_and_expand_3(point)
            points.append(point)

        
        rabbits, sheep = zip(*points)
        plt.plot(rabbits, sheep, label=f"Start: {start_point}")

    plt.title('Rabbits vs Sheep Population Dynamics for Multiple Starting Points')
    plt.xlabel('Rabbits')
    plt.ylabel('Sheep')
    plt.legend()
    plt.grid(True)
    plt.show()


// starting_points = [(-1.0, 2.5)]


generate_and_plot(starting_points, iterations=10000)
