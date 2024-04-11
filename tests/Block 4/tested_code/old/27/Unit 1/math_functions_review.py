


input_number = int(input("Enter an integer: "))
number_f = input_number

def factorial(number_f):
    
    number_1 = number_f - 1
    while number_1 > 1:
            number_f = number_f * number_1
            number_1 = number_1 - 1
    return number_f	

number_t = input_number
def triangular_number(number_t):
    countdown = number_t - 1

    while countdown > 0:
        number_t = number_t + countdown
        countdown = countdown - 1
    return number_t



number_n = input_number
def new_triangular_number(number_n):
    countdown = number_n - 2


    while countdown > 0:
        number_n = number_n + countdown
        countdown = countdown - 2
    return number_n


print( )
print(str(input_number) + "! is " + str(factorial(number_f)))
print("Triangular number: " + str(triangular_number(number_t)))
print( + str(new_triangular_number(number_n)))
        


