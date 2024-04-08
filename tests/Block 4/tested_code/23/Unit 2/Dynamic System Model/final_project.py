



def r_and_j(point_old):

    R_old = point_old[0]
    J_old = point_old[1]
    R_new = R_old + 0.4 * J_old
    J_new = J_old - 0.2 * R_old
    return (R_new, J_new)

def r_and_j_altered(point_old):

    R_old = point_old[0]
    J_old = point_old[1]
    R_new = 0.9 * R_old + 0.4 * J_old
    J_new = J_old - 0.2 * R_old
    return (R_new, J_new)
    



def simulation(point_old, f):
    list_of_points = [(point_old)]

    
    for _ in range(100):

        point_new = f(point_old)
        list_of_points.append(point_new)
    
        point_old, point_new = point_new, point_old
        
    print(list_of_points)


x_value = float(input('Starting x value: '))
y_value = float(input('Starting y value: '))
simulation((x_value, y_value), r_and_j)
        

