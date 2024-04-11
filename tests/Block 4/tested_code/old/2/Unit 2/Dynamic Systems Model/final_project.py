




num_rabbits = int(input('Number of rabbits: '))
num_foxes = int(input('Number of foxes: '))
days = int(input('Days of simulation: '))


def simulate_model(num_rabbits, num_foxes):
    x = num_rabbits
    y = num_foxes
    
    new_rabbits = round(x + 0.01 * x - 0.01 * x * y, 3)
    new_foxes = round(y - 0.02 * y + 0.01 * x * y, 3)
    
    if new_rabbits < 0 : 
        new_rabbits = 0
    if new_foxes < 0 :
        new_foxes = 0
    return (new_rabbits, new_foxes)


current_point = (num_rabbits, num_foxes)
list_of_points = [(num_rabbits, num_foxes)]


def generate_points(current_point, list_of_points, days):
    for _ in range(days):
        
        current_point = simulate_model(current_point[0], current_point[1])
        
        list_of_points.append(current_point)



generate_points(current_point, list_of_points, days)

print(list_of_points)
