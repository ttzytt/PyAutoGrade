


def update_feelings(Romeo_current, Juliet_current):

    Romeo_new = Romeo_current - 0.3 * Romeo_current + 0.2 * Juliet_current
    Juliet_new = Juliet_current - 0.3 * Juliet_current + 0.2 * Romeo_current
    return (Romeo_new, Juliet_new)


feelings_over_time = [(0.09, 0.01)]

for i in range(55):

    Romeo_current = feelings_over_time[-1][0]
    Juliet_current = feelings_over_time[-1][1]
    new_feelings = update_feelings(Romeo_current, Juliet_current)
    feelings_over_time.append(new_feelings)

print(feelings_over_time)



