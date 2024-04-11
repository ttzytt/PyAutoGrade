





number_n = int(input("Input the number you want to triangularize: "))




countdown = number_n - 1


while countdown > 0:
    number_n = number_n + countdown
    countdown = countdown - 1



print("The triangular number of your number is " + str(number_n))


