


n = int(input("Enter an integer: "))

'''
 n is a global variable that will store the input number of the user
 number_f is the variable that is going to operate in factorial n
 number_1 is one less than number_f
 number_t is the variable that will go into the operation of number_t
 number_n is the variable that will go into the operation in triangular_number
'''


def factorial(n):
    number_f = n
    number_1 = number_f - 1
    while number_1 > 1:
            number_f = number_f * number_1
            number_1 = number_1 - 1
    return number_f	


def triangular_number(n):
    number_t = n
    countdown = number_t - 1

    while countdown > 0:
        number_t = number_t + countdown
        countdown = countdown - 1
    return number_t




def new_triangular_number(n):
    number_n = n
    countdown = number_n - 2


    while countdown > 0:
        number_n = number_n + countdown
        countdown = countdown - 2
    return number_n



print( )
print(str(n) + "! is " + str(factorial(n)))

print("Triangular number: " + str(triangular_number(n)))
print('''"New" triangular number: ''' + str(new_triangular_number(n)))
