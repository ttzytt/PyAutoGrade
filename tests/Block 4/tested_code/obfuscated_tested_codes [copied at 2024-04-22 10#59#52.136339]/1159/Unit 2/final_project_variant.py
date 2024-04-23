


days = int(input('days: '))
rabbits = int(input('rabbits: '))
sheep = int(input('sheep: '))

for count in range(days):

    rabbits_new = rabbits + 0.1*rabbits*(3-rabbits) - 0.2*rabbits*sheep
    sheep_new = sheep + 0.1*sheep*(2-sheep) - 0.1*rabbits*sheep

    rabbits = round(rabbits_new*100)/100
    sheep = round(sheep_new*100)/100

    print('('+str(rabbits)+','+str(sheep)+')', end = ', ')
