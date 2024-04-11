


        
rabbits = int(input("How many rabbits would you like? "))
foxes = int(input("How many foxes would you like? "))
days = int(input("How many days are you going to run? "))
point = (rabbits, foxes)

def total_animals(point):
    new_rabbits = point[0] + (0.01 * point[0]) - ((0.01 * point[0]) * point[1])
    new_foxes = point[1] - (0.02 * point[1]) + ((0.01 * point[0]) * point[1])
    new_rabbits = round(new_rabbits, 4)
    new_foxes = round(new_foxes, 4)

    return (new_rabbits, new_foxes)

rabbits_foxes = [point]

for i in range(1, days + 1):
    if i % 10 == 0:
        point = total_animals(point)
        rabbits_foxes.append(point)
        
print(rabbits_foxes)
