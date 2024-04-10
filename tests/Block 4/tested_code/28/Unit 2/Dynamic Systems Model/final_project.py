




import pyperclip






def format_data_to_desmos(data):
    copying = []
    for point in data:
       copying.append("	".join(convert_points_to_strings(point)))
    pyperclip.copy("\n".join(copying))










def run_model(rabbits = 5, sheep = 1, max_days = 50):
    day = 1
    while day <= max_days:
        new_rabbits = rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep
        new_sheep = sheep + 0.1 * (2 - sheep) * sheep - 0.1 * rabbits * sheep
        if new_rabbits < 0:
            new_rabbits = 0
        if new_sheep < 0:
            new_sheep = 0
        rabbits = new_rabbits
        sheep = new_sheep
        day += 1
    return rabbits, sheep










def run_model_2(rabbits = 5, sheep = 1, max_days = 50):
    day = 1
    while day <= max_days:
        new_rabbits = rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep
        new_sheep = sheep + 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep
        if new_rabbits < 0:
            new_rabbits = 0
        if new_sheep < 0:
            new_sheep = 0
        rabbits = new_rabbits
        sheep = new_sheep
        day += 1
    return rabbits, sheep



def check_for_negative(point):
    return point[0] < 0 or point[1] < 0





def convert_points_to_strings(point):
    return map(str,map(lambda x: round(x,4), point))

data = []
max_days = 1000
for days in range(max_days):
    data.append(tuple(run_model_2(3,1.25,days)))

format_data_to_desmos(data)

assert False

data = []
max_days = 50
for rabbits in range(1,15):
    print(rabbits, end = ': ')
    for sheep in range(1,15):
        point = run_model(rabbits,sheep,max_days)
        if check_for_negative(point):
            print("negative")
        
        if (round(point[0],5),round(point[1],5)) == (0,0):
           data.append((rabbits, sheep))

format_data_to_desmos(data)

input()

data = []
for rabbits in range(1,100):
    print(rabbits)
    for sheep in range(1,100):
        point = run_model_2(rabbits,sheep,max_days)
        if check_for_negative(point):
            print("negative")
        if (round(point[0],5),round(point[1],5)) == (0,0):
           data.append((rabbits, sheep))

format_data_to_desmos(data)


   

