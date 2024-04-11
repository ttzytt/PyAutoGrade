







def love_hate(love, a, b):
    romeo = love[0]
    juliet = love[1]
    romeo_new = romeo - a * romeo + b * juliet
    juliet_new = juliet - a * juliet + b * romeo
    return (round(romeo_new, 4), round(juliet_new, 4))



def love_hate_simulation(a, b, time, romeo_start, juliet_start):
    love_meter = [(romeo_start, juliet_start)]

    for i in range(time):
        love_meter.append(love_hate(love_meter[i], a, b))

    print(love_meter)


a = 0.3
b = 0.2
romeo_start = 5
juliet_start = -5
time = 50
love_hate_simulation(a, b, time, romeo_start, juliet_start)

