




romeo = float(input('Input Romeo:'))
juliet = float(input('Input Juliet:'))
a = 0.2
b = 0.3
romeo_new = 0
juliet_new = 0
point = (romeo, juliet)
list_affection = []
list_affection.append(point)
def romeo_and_juliet(point):
    romeo = point[0]
    juliet = point[1]
    romeo_new = romeo - a*romeo + b*juliet
    juliet_new = juliet - a*juliet + b*romeo
    return (romeo_new, juliet_new)
for i in range(50):
    point = romeo_and_juliet(point)
    list_affection.append(point)
print(list_affection)

'''
The graph is scaled
'''
