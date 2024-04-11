


'''
 The variable "number_n" is going to store the input number at first,
 and it's going to be the number that is going through operation.
 It is also going to be the triangular number in the last
 The variable "countdown" is going to store the value of number n-1
 The first operation is going to be n + n-1
'''


number_n = int(input("Input the number you want to triangularize: "))




countdown = number_n - 1


while countdown > 0:
    number_n = number_n + countdown
    countdown = countdown - 1



print("The triangular number of your number is " + str(number_n))


