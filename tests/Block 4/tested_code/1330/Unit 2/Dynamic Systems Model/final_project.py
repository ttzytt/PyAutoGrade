



A = 0.1
B = 0.2
C = 0.1
D = 0.02
K_1 = 3
K_2 = 1

T = 0.5



def model():
    time = 0
    rabbit = 3
    sheep = 3
    while time < 200:
        new_rabbit = rabbit + (A * (K_1-rabbit) * rabbit-B * rabbit * sheep)*T
        new_sheep = sheep + (C * (K_2 -sheep) * sheep - D * rabbit * sheep)*T
        rabbit = new_rabbit
        sheep = new_sheep
        time += 1

        print('(' + str(new_rabbit) + ', ' + str(new_sheep) + ')', end = ', ' )


def compare_model():
    time = 0
    rabbit = 1
    sheep = 2
    while time < 100:
        new_rabbit = rabbit + 0.1 * (3-rabbit) * rabbit-0.2 * rabbit * sheep
        new_sheep = sheep + 0.1 * (1-sheep) * sheep - 0.02 * rabbit * sheep
        rabbit = new_rabbit
        sheep = new_sheep
        time += 1

        print('(' + str(round(new_rabbit*100)/100) + ', ' + str(round(new_sheep*100)/100) + ')', end = ', ' )

