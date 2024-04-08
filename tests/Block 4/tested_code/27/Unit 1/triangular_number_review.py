










number_n = int(input("Input your number n: "))






number_n_minus_1 = number_n - 1


while number_n_minus_1 > 0:
    number_n = number_n + number_n_minus_1
    number_n_minus_1 = number_n_minus_1 - 1



print("Your triangular number is " + str(number_n))


