


a = [10]
b = a
a = [12]
print(a,b)


a = [10]
b = a
a[0] = 12
print(a,b)


a = [10]
b = a[:]
a[0] = 12
print(a,b)







a = 'hi'
b = a
a = 'pi'
print(a,b)






my_list = [1,2,3,4]
for i in range(len(my_list)): 
    my_list[i] += 1
last_index = i
print(my_list)
print(i)


my_list = [1,2,3,4]
for x in my_list:
    x += 1
last = x
print(my_list) 
print(x)


def func_1(x):
    x[0] = 5
L = [1,2,3]
print(func_1(L))

