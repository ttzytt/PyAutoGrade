'''
DO NOT RUN THIS PROGRAM

'''




def to_the_power_of(base,power):
    if base == 0:
        return None
    elif power == 0:
        return 1
        
    product = base
    for count in range(1,power):
        product = product * base
    return product


'''
def power_of_i(comnum,power):
    if comnum == 'i':
        if power == 1 or power % 4 == 1:
            return i
        elif power == 2 or power % 4 == 2:
            return -1
        elif power == 3 or power % 4 == 3:
            return -i
        elif power == 4 or power % 4 == 0:
            return 1
'''

def power_of_i(power):
    if power == 1 or power % 4 == 1:
        return 'i'
    elif power == 2 or power % 4 == 2:
        return -1
    elif power == 3 or power % 4 == 3:
        return '-i'
    elif power % 4 == 0:
        return 1


'''def quadratic_function(a,b,c):
    x = 0
    while a*x*x + b*x + c != 0:
        x += 0.01
    return x
'''

def odd_even_count(nums):
    odd = 0
    even = 0
    for count in range(len(nums)):
        if nums[count] % 2 == 1: 
            odd += 1
        elif nums[count] % 2 == 0: 
            even += 1
    return odd,even


def roots(a,b,c):
    disc = b**2 - 4*a*c 
    if disc > 0:
        return ((-b + disc**0.5)/(2*a),(-b - disc**0.5)/(2*a))
    elif disc == 0:
        return -b/(2*a)
    elif disc < 0:
        return 'This function has no real roots'


def transfer1(a,b,c): 
    x = a
    y = b/(2*a)
    z = c - a*(y**2)
    return x,y,z


def transfer2(x,y,z):
    a = x
    b = 2*a*y
    c = z + a*(y**2)
    return a,b,c

'''
def derivative_slope(a,b,c): # ax^2 + bx + c
    m = 1
    delta = 1
    def qua(a,b,c,m):
        return a*(m**2) + b*m + c
    def delta(a,b,c,m,delta):
        return a*((m+delta)**2) + b*(m+delta) + c
    return (delta(a,b,c,m,delta)-qua(a,b,c,m))/delta
'''
    


